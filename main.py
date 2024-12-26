from MailGist import GmailMailGist
import os
import asyncio


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"
credential = None
client_secret = "clients\\credentials\\gmail\\personal.json"

personal = GmailMailGist(token, endpoint, model_name, credential, client_secret)
asyncio.run(personal.start())
