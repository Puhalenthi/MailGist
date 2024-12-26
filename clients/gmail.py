import base64
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# TODO: Use push notifications instead of time-based
class Gmail:
    def __init__(self, client_secret):
        self.client_secret = client_secret
        creds = None

        SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
                creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
                token.write(creds.to_json())

        self.creds = creds

    def parse_email(self, email):
        payload = email.get("payload", {})
        headers = payload.get("headers", [])

        # if mimeType is a direct child of payload
        if payload.get("mimeType") == "text/plain":
            data = payload.get("body", {}).get("data")
            return base64.urlsafe_b64decode(data).decode("utf-8")

        # if mimeType is not a direct child of payload, iterate through all parts to find the relevant part
        parts = payload.get("parts", [])
        for part in parts:
            if part.get("mimeType") == "text/plain":
                data = part.get("body", {}).get("data")
                return base64.urlsafe_b64decode(data).decode("utf-8")

        return "No plain text email body found."

    def get_new_email(self):
        try:
            # Call the Gmail API
            service = build("gmail", "v1", credentials=self.creds)
            results = (
                service.users()
                .messages()
                .list(userId="me", maxResults=1, q="category:primary")
                .execute()
            )
            messages = results.get("messages", [])

            if not messages:
                print("No new messages.")
                return

            message = (
                service.users()
                .messages()
                .get(userId="me", id=messages[0]["id"])
                .execute()
            )
            return self.parse_email(message)

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")

    def run(self):
        return self.get_new_email()
