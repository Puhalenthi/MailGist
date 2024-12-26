from abc import ABC, abstractmethod
import asyncio

from clients import gmail, outlook
from utilities import agent, notification


class MailGist(ABC):
    def __init__(self, token, endpoint, model_name, credential, client_secret=None):
        self.credential = credential
        self.client_secret = client_secret

        self.agent = agent.Agent(token, endpoint, model_name)

    def summarize_email(self, body):
        return self.agent.summarize_email(body)

    def process_summary(self, summary):
        summaryArr = summary.split("\n")
        print(summaryArr)

        if "low" in summaryArr[0].lower():
            urgency = "low"
        elif "medium" in summaryArr[0].lower():
            urgency = "medium"
        elif "high" in summaryArr[0].lower():
            urgency = "high"
        else:
            urgency = "medium"

        return [urgency, summaryArr[2]]

    @abstractmethod
    def start(self):
        pass


class GmailMailGist(MailGist):
    async def start(self):
        gmailClient = gmail.Gmail(self.client_secret)
        prevBody = None
        while True:
            body = gmailClient.run()
            if body != prevBody:
                summary = self.process_summary(self.summarize_email(body))
                print(summary)

                toast = notification.Notification(
                    app_id="MailGist",
                    title="TEMP",
                    msg=summary[1],
                    email_urgency=summary[0],
                )
                toast.show()
                prevBody = body
            await asyncio.sleep(5)


class OutlookMailGist(MailGist):
    def start(self):
        # TODO: Perform outlook methods
        pass
