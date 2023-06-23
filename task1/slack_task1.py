import os
from slack_sdk import WebClient

# Set your Slack API token and channel ID
slack_token = "xoxb-5472584772914-5472503405811-9CC151JEOurx0t6o0FHmPMiQ"
channel_id = "C05E96Q6PFB"

# Initialize the Slack API client
client = WebClient(token=slack_token)

# Function to send a message to a channel
def send_message_to_channel(message):
    try:
        # Send the message to the specified channel
        response = client.chat_postMessage(channel=channel_id, text=message)
        if response["ok"]:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Prompt the user for a message
message = input("Enter the message to send: ")

# Send the message to the channel
send_message_to_channel(message)
