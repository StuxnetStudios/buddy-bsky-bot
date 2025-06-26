# buddy.py
# bsky bot starter kit
#
# Stuxnet Studios 2025
# Copyleft

from atproto import Client
from dotenv import load_dotenv
import os

# This is how we hide our keys and secrets
# Create a .env file in the same directory with the following content:
# BSKY_HANDLE=your_handle
# BSKY_APP_PASSWORD=your_app_password
# No quotes

load_dotenv()  # Load environment variables from .env file

HANDLE = os.environ.get('BSKY_HANDLE')
APP_PASSWORD = os.environ.get('BSKY_APP_PASSWORD')
# NOT the account password, but the app password generated from the account settings
# You can generate an app password at https://bsky.app/settings/app-passwords

if not HANDLE or not APP_PASSWORD:
    raise RuntimeError("Please set BSKY_HANDLE and BSKY_APP_PASSWORD in your .env file.")

client = None

def connect_bsky():
    global client
    if client is None:
        try:
            client = Client()
            client.login(HANDLE, APP_PASSWORD)
            print("Successfully logged in to Bluesky!")
        except Exception as e:
            print(f"Login failed: {e}")
            client = None
            raise
    return client

def start_bot():
    """
    Main entry point for the bot. Posts a hello message and fetches notifications.
    """
    notifications = fetch_notifications()
    parse_notifications(notifications)

def fetch_notifications():
    """
    Fetch notifications from Bluesky and return the list.
    """
    try:
        client = connect_bsky()
        # Use the correct method for fetching notifications
        response = client.app.bsky.notification.list_notifications()
        return response.notifications
    except Exception as e:
        print(f"Failed to fetch notifications: {e}")
        return []

def parse_notifications(notifications):
    """
    Process and handle the list of notifications.
    """
    if notifications:
        print(f"Fetched {len(notifications)} notifications.")
        for notification in notifications:
            # Check if the notification is a mention
            if notification.reason == 'mention':
                author = notification.author.handle
                
                # Check if the author is a follower
                try:
                    viewer_info = getattr(notification.author, 'viewer', None)
                    if viewer_info:
                        # Check for followed_by (with underscore) which contains the follow URI
                        followed_by = getattr(viewer_info, 'followed_by', None)
                        is_follower = followed_by is not None and followed_by != False
                    else:
                        is_follower = False
                except Exception as e:
                    print(f"Error checking follower status: {e}")
                    is_follower = False
                
                print(f"Mention from @{author}, is_follower: {is_follower}")
                
                # Only reply to followers
                if is_follower:
                    reply_text = "I only interact with my followers."
                    try:
                        # Create proper reply structure
                        reply_ref = {
                            "root": {
                                "uri": notification.uri,
                                "cid": notification.cid
                            },
                            "parent": {
                                "uri": notification.uri,
                                "cid": notification.cid
                            }
                        }
                        post_message(reply_text, reply_to=reply_ref)
                    except Exception as e:
                        print(f"Failed to reply: {e}")
                else:
                    print(f"Not replying to @{author} (not a follower).")
    else:
        print("No notifications found.")

def post_message(message="Hello World!", reply_to=None):
    try:
        client = connect_bsky()
        if reply_to:
            # Create a reply post
            client.send_post(text=message, reply_to=reply_to)
        else:
            # Create a regular post
            client.send_post(text=message)
        print(f"Posted '{message}' to bsky.")
    except Exception as e:
        print(f"Failed to post message: {e}")

# To start the bot, call:
start_bot()
