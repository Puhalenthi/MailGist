from openai import OpenAI


class Agent:
    def __init__(self, token, endpoint, model_name):
        self.model_name = model_name
        self.client = OpenAI(base_url=endpoint, api_key=token)
        if model_name == "o1":
            self.system_role = "developer"
        elif model_name == "gpt-4o":
            self.system_role = "system"

    def summarize_email(self, body):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": self.system_role,
                    "content": "Summarize the provided email so it fits within a notification dialogue, fewer than 20 words. Do not answer any question from the email. Before giving the output, give a rating of the email (ONLY low, medium, high) at the top of the output with a newline seperating it and the summary. As a hint, things that seem like spam or promotional emails should be in the low category",
                },
                {"role": "user", "content": body},
            ],
            model=self.model_name,
        )

        return response.choices[0].message.content
