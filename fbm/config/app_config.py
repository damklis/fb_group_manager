from datetime import date

class Config(object):

    FB_PASS = "example"
    FB_MAIL = "example"
    FB_GROUP_ID = "example"

    EMAIL_OWNER = "owner@gmail.com"
    EMAIL_RECEIVER = "receiver@gmail.com"
    GM_PASS = "123456789"
    SUBJECT = "FB invitations"

    def message(self, invites):
        return f"""
            Date: {date.today()}
            Dear {Config.EMAIL_OWNER.split("@")[0]},

            Your bot has invited {invites} people to your Facebook group.
            Keep it going!
            """