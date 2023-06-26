import webbrowser
import pyautogui
import time
import urllib.parse

def send_messages_from_file(file_path):
    # Read the message bodies from the file
    with open(file_path, 'r') as file:
        message_bodies = file.readlines()

    # Iterate over each message body and send the message
    for message_body in message_bodies:
        # Strip leading/trailing whitespaces from the message body
        message_body = message_body.strip()

        # Encode the message body for the URL
        encoded_message_body = urllib.parse.quote(message_body)

        # Construct the message link with the updated body
        message_link = f'sms://open?addresses=888222&body={encoded_message_body}'
        webbrowser.open(message_link)

        time.sleep(1)  # Delay to give you time to focus on the desired input field
        pyautogui.press('enter')
        time.sleep(1)  # Delay between sending messages
        print('Message Actually Sent')
