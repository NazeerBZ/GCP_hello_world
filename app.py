import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./keyfile.json"

from google.cloud import vision
client = vision.ImageAnnotatorClient()
import io

file_name = 'larry.jpg'
with io.open(file_name,'rb') as image_file:
    content = image_file.read()
    response = client.annotate_image({
            'image': {
                    'content': content 
                    },
            })
    
print(response)
dataLen = len(response)