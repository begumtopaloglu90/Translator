import requests, uuid, json
import csv
# Add your key and endpoint
key = "b3037f6ee59f4f29b0fd80b3fe6213aa"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "westus2"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['es', 'tr', 'de', 'fr', 'pt', 'ru', 'it', 'ar', 'az', 'da', 'el']
}
headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

file_path = input("Enter your text: ")

with open (file_path,'r') as file :
    text_to_translate = file.read()

# You can pass more than one object in body.
body = [{
    'text': text_to_translate
}]
request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

# billgates.csv
newFile = file_path.split('.')[0] + '.csv'
file = open(newFile, 'w', encoding='utf-8', newline='')

csv_writer = csv.writer(file)
csv_writer.writerow(['en', text_to_translate, len(text_to_translate)])

print(response)

for translation in response[0]['translations']:
    csv_writer.writerow([translation['to'], translation['text'], len(translation['text'])])
    



