import requests
import random
import time
from PIL import Image
from io import BytesIO

#########################################

showimage = "true"
infloop = "true"
loopinterval = 3

while infloop == "true":
  response = requests.get("https://api.github.com/repos/pythonindenthater4444/lehmanapi/contents")
  if response.status_code == 200:
    data = response.json()
    random_image_url = random.choice([i["download_url"] for i in data])
    print(str(random_image_url))
    if showimage == "true":
      reponse2 = requests.get(random_image_url)
      if reponse2.status_code == 200:
        img = Image.open(BytesIO(reponse2.content))
        img.show()
      else:
        print("Error")
    else:
      print("Error")
  else:
    print("Error")
  time.sleep(loopinterval)
