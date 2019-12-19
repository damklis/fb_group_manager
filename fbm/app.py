from fbm.manager.fb_group_manager import FbGroupContentManager
import os
from datetime import date
from fbm.common.email_sender import GmailEmailSender
from selenium.common.exceptions import StaleElementReferenceException
from config.app_config import Config as config


def run_app(headless_option: bool=False):
    '''
    The full process of the managing group page.
    Additionally, you will receive information trough email with a number of invitations sent.
    '''
    fb_group_manager = FbGroupContentManager(
        email=config.FB_MAIL, 
        password=config.FB_PASS, 
        fb_group_id=config.FB_GROUP_ID, 
        headless=headless_option
    )

    fb_group_manager.sign_in()
    print("Signed in.")

    fb_group_manager.redirect_to_group()
    print(f"Redirected to group with id: {fb_group_manager.fb_group_id}")

    try:
        fb_group_manager.invite_people_to_group()
    except StaleElementReferenceException as e:
        print(f"This person is already your group member. More: {e}")
    finally:
        fb_group_manager.redirect_to_group()
    
    fb_group_manager.write_post()
    
    fb_group_manager.approve_new_users()

    gmail_app = GmailEmailSender(
        config.EMAIL_OWNER,
        config.GM_PASS,
        config.SUBJECT
    )

    gmail_app.send_information(
        config.EMAIL_RECEIVER,
        config.message(fb_group_manager.invites)
    )

    fb_group_manager.close_browser_connection()
