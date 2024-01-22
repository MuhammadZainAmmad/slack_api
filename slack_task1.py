import os
from slack_sdk import WebClient
from htmlslacker import HTMLSlacker
import html2text

slack_token = os.environ.get('slackAPIToken_task1')
channel_id = "C05E96Q6PFB"

client = WebClient(token=slack_token)


# Function to send a message to a channel
def send_message_to_channel(filePath):
    with open(filePath, 'r') as file:
        content = file.read()
        
    try:
        # 1) Sending the file as it is
        # response = client.files_upload_v2(channels=channel_id, file=filePath) 
        
        # 2.1) Sending the content of the file as message
        # response = client.chat_postMessage(channel=channel_id, text=content) 
        
        # 2.2) Same, sending the content of the file as message
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
        # response = client.chat_postMessage(channel=channel_id, text= 'html page', blocks=message['blocks'])
        
        # 3) Sending content with parsing 
        # message = HTMLSlacker(content).get_output()
        # response = client.chat_postMessage(channel=channel_id, text=message) 
        
        # 4) Sending the table content with a table like format 
        slackTable = html2text.html2text(content) # parse the html table 
        message = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"```{slackTable}```"
                        }
                    }
                ]
            } # for sending mesage in code block
        response = client.chat_postMessage(channel=channel_id, text= 'html page', blocks=message['blocks'])
        
        if response["ok"]:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    except Exception as e:
        print(f"Error: {str(e)}")
        
send_message_to_channel("./test.html")