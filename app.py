import os
import boto3
import requests
import json
from dotenv import load_dotenv
from datetime import date
load_dotenv()

url = 'https://api-football-v1.p.rapidapi.com/v3/standings'
querystring = {'season':'2022','league':'39'}
headers = {
	'X-RapidAPI-Key': os.getenv('RAPID_API_KEY'),
	'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
}
response = requests.request('GET', url, headers=headers, params=querystring)
data = response.json()
json_string_from_data = json.dumps(data)
client = boto3.client(
    's3', 
    endpoint_url=os.getenv('ENDPOINT_URL'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
client.put_object(
    Bucket=os.getenv('BUCKET_NAME'), 
    Key=f'premier_league/standings/{date.today()}.json',
    Body=json_string_from_data
)
client.put_object(
    Bucket=os.getenv('BUCKET_NAME'), 
    Key=f'premier_league/standings/latest.json',
    Body=json_string_from_data
)
