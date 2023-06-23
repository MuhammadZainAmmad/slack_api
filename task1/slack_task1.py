from slack_sdk import WebClient

slack_token = "xoxb-5472584772914-5472503405811-lUCdSgPXDg0pZFf8OGY4eC0y"
channel_id = "C05E96Q6PFB"

# Slack API client initialization
client = WebClient(token=slack_token)

# Function to send a message to a channel
def send_message_to_channel(message):
    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        if response["ok"]:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Program that causes a divide by zero error
def testingFunc():
    try:
        numerator = 10
        denominator = 0
        result = numerator / denominator
        print(f"The result is: {result}")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        send_message_to_channel(error_message)

testingFunc()