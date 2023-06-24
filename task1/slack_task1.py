from slack_sdk import WebClient
from htmlslacker import HTMLSlacker

slack_token = "xoxb-5472584772914-5472503405811-TyETVNdKI0LyOb4W3rL9vj5h"
channel_id = "C05E96Q6PFB"

# Slack API client initialization
client = WebClient(token=slack_token)


# Function to send a message to a channel
def send_message_to_channel(filePath):
    with open (filePath, 'r') as file:
        content = file.read()
    try:
        # response = client.files_upload_v2(channels=channel_id, file=filePath) # Sending the file as it is
        # response = client.chat_postMessage(channel=channel_id, text=content) # Sending the content of the file as message
        
        # message = {
        #             'blocks': [
        #                 {
        #                     'type': 'section',
        #                     'text': {
        #                         'type': 'mrkdwn',
        #                         'text': content
        #                     }
        #                 }
        #             ]
        #         }
        # response = client.chat_postMessage(channel=channel_id, text= 'html page', blocks=message['blocks']) # Same, sending the content of the file as message
        
        message = HTMLSlacker(content).get_output()
        response = client.chat_postMessage(channel=channel_id, text=message)
        
        if response["ok"]:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    except Exception as e:
        print(f"Error: {str(e)}")
        
send_message_to_channel("./test.html")

# Program that causes a divide by zero error
# def testingFunc():
#     try:
#         numerator = 10
#         denominator = 0
#         result = numerator / denominator
#         print(f"The result is: {result}")
#     except Exception as e:
#         error_message = f"An error occurred: {str(e)}"
#         send_message_to_channel(error_message)

# testingFunc()