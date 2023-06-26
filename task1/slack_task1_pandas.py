import pandas as pd
from slack_sdk import WebClient
import os

channel_id = "C05E96Q6PFB"
slack_token = os.environ['slackAPIToken_task1']
client = WebClient(token=slack_token)

path = './modified_sampleHTML.html'
with open(path, 'r') as file:
    html_content = file.read()

dfs = pd.read_html(html_content, header=None)
print(dfs[0])
markdown_table = dfs[0].to_markdown(index=False)

response = client.chat_postMessage(channel=channel_id, text= f"```{markdown_table}```")

if response['ok']:
    print('Message sent successfully!')
else:
    print('Failed to send message. Error:', response['error'])
