import os
import boto3
import requests
from dotenv import load_dotenv
from datetime import date
load_dotenv()


# goals_df = list(filter(lambda t: 'G' in t.columns, tables))[0]
# assists_df = list(filter(lambda t: 'A' in t.columns, tables))[0]
# goals_buffer = goals_df.to_csv(index=False).encode()
# assists_buffer = assists_df.to_csv(index=False).encode()
# client = boto3.client(
#     's3', 
#     endpoint_url=os.getenv('ENDPOINT_URL'),
#     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
#     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
# )
# client.put_object(
#     Bucket=os.getenv('BUCKET_NAME'), 
#     Key=f'premier_league/player/top_scorers_{date.today()}.csv',
#     Body=goals_buffer
# )
# client.put_object(
#     Bucket=os.getenv('BUCKET_NAME'), 
#     Key=f'premier_league/player/top_assisters_{date.today()}.csv', 
#     Body=assists_buffer
# )
