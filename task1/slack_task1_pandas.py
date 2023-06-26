import pandas as pd
from slack_sdk import WebClient
import os

channel_id = "C05E96Q6PFB"
slack_token = os.environ['slackAPIToken_task1']
client = WebClient(token=slack_token)

path = './sample_html.html'
with open(path, 'r') as file:
    html_content = file.read()

dfs = pd.read_html(html_content)
markdown_table = dfs[0].to_markdown(index=False)

# Send the message
message = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"```{markdown_table}```"
                        }
                    }
                ]
            } # for sending mesage in code block
response = client.chat_postMessage(channel=channel_id, text= 'html page', blocks=message['blocks'])

# Check if the message was sent successfully
if response['ok']:
    print('Message sent successfully!')
else:
    print('Failed to send message. Error:', response['error'])
