import requests
from api_key import API_KEY # importing API token

# uploading file 
upload_endpoint = 'https://api.assemblyai.com/v2/upload'

filename = "C:/Users/JORN/speech-recognition/Speech_Recognition/Audio_processing/audio_file.wav"

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': API_KEY}
response = requests.post(upload_endpoint,
                        headers=headers,
                        data=read_file(filename))

print(response.json())
audio_url = response.json()['upload_url']# response from uploading audio

# submitting upload for transcription
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

json = { "audio_url": audio_url}

response = requests.post(transcript_endpoint, json=json, headers=headers)

print(response.json())

job_id = response.json()['id']

# polling AssemblyAI to get if the transcription is ready or not
polling_endpoint = transcript_endpoint + '/' + job_id # creating a polling endpoint
polling_response = requests.get(polling_endpoint, headers=headers) # get request

print(polling_response.json())

# while loop for polling AssemblyAI
while True:
    polling_response = requests.get(polling_endpoint, headers=headers)
    if polling_response.json()['status'] == 'completed':
        print(polling_response.json())
    elif polling_response.json()['status'] == 'error':
        print('error')

