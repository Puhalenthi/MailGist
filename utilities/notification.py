import winotify


class Notification:
    def __init__(self, app_id, title, msg, email_urgency="medium"):
        self.app_id = app_id
        self.title = title
        self.msg = msg
        self.email_urgency = email_urgency

    def show(self):
        toast = winotify.Notification(
            app_id=self.app_id,
            title=self.title,
            msg=self.msg,
        )

        if self.email_urgency == "low":
            toast.set_audio(winotify.audio.Mail, loop=False)
        elif self.email_urgency == "medium":
            toast.set_audio(winotify.audio.Default, loop=False)
        elif self.email_urgency == "high":
            toast.set_audio(winotify.audio.LoopingAlarm, loop=False)

        toast.show()


if __name__ == "__main__":
    notif = Notification(
        app_id="MailGist",
        title="Hello, World!",
        msg="This is a notification from Python.",
        email_urgency="high",
    )
    notif.show()
