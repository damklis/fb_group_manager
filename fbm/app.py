from fbm.manager.fb_group_manager import FbGroupContentManager
import os
from datetime import date
from fbm.common.email_sender import GmailEmailSender
from selenium.common.exceptions import StaleElementReferenceException

def run_app(headless_option: bool=False):
    '''
    The full process of the managing group page.
    Additionally, you will receive information trough email with a number of invitations sent.
    '''

    fb_pass = os.environ.get('FB_PASS')
    fb_mail = os.environ.get('FB_@')

    fb_group_manager = FbGroupContentManager(
        email=fb_pass, 
        password=fb_mail, 
        fb_group_id="298296040793329", 
        headless=headless_option
    )
    fb_group_manager.sign_in()
    print("Signed in.")

    fb_group_manager.redirect_to_group()
    print(f"Redirected to group with id: {fb_group_manager.fb_group_id}")

    try:
        fb_group_manager.invite_people_to_group()
    except StaleElementReferenceException as e:
        print('This person is already your group member.')
    finally:
        fb_group_manager.redirect_to_group()
    
    fb_group_manager.write_post()
    
    fb_group_manager.approve_new_users()

    email_owner = "owner@gmail.com"
    email_receiver = "receiver@gmail.com"
    gm_pass = "123456789"

    message = f"""
    Date: {date.today()}
    Dear {email_owner.split("@")[0]},

    Your bot has invited {fb_group_manager.invites} people to your Facebook group.
    Keep it going!
    """

    gmail_app = GmailEmailSender(email_owner, gm_pass, "FB invitations")

    gmail_app.send_information(email_receiver, message)

    fb_group_manager.close_browser_connection()
