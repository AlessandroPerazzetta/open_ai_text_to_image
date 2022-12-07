import os, errno
import openai
import urllib.request
from datetime import datetime

from pprint import pprint

# Load your API key from an environment variable or secret management service
openai.api_key = "INSERT-OPENAI-API-KEY-HERE"

out_dir = 'out'

# input_str = "a set of detailed futuristic digitalart of cities in Hans Ruedi Giger style"

input_str = ''

# Start a loop that will run until the user give input
while True:
    input_str = input("Enter your request: ")

    if input_str:
      print(input_str)
      # response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
      
      # prompt="a white siamese cat",

      response = openai.Image.create(
        prompt=input_str,
        n=1,
        size="1024x1024"
      )
      
      image_url = response['data'][0]['url']

      pprint(image_url)

      try:
          os.makedirs(out_dir)
      except OSError as e:
          if e.errno != errno.EEXIST:
              raise

      # current date and time
      now = datetime.now()

      output_str = "out/{}_{}.png".format(input_str.replace(' ', '_'), now.strftime("%Y%m%d%H%M%S"))

      urllib.request.urlretrieve(image_url, output_str)
      
      break
