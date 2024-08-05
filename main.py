from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
web = webdriver.Chrome(options=chrome_options)
web.get('https://report-100xdevs.vercel.app/')
import time

#random url generator (url_gen)

import random
import string

def generate_random_string(min_length=26, max_length=38):
  """Generates a random string of the specified length using letters and digits."""
  length = random.randint(min_length, max_length)
  print(length)
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  return ''.join(random.choice(characters) for _ in range(length)) 

def attach_random_characters(base_url, random_text_length=10):
  """Attaches a random string to the base URL and generates random text for the folder name."""
  random_string = generate_random_string()
  random_text = ''.join(random.choice(string.ascii_letters) for _ in range(random_text_length))
  gen_url = f"{base_url}/{random_text}{random_string}"
  return gen_url

base_url = "https://drive.google.com/drive/folders"

def generate_random_username(min_length=9, max_length=16):
  """Generates a random string of the specified length using letters and digits."""
  length = random.randint(min_length, max_length)
  print(length)
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  username = ''.join(random.choice(characters) for _ in range(length)) 
  return username

def generate_random_email(min_length=11, max_length=24):
    """Generates a random string of the specified length using letters and digits."""
    length = random.randint(min_length, max_length)
    print(length)
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    email = ''.join(random.choice(characters) for _ in range(length)) + '@gmail.com'
    return email

def generate_random_reason(min_length=30, max_length=50):
    """Generates a random string of the specified length using letters and digits."""
    length = random.randint(min_length, max_length)
    print(length)
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    reason = ''.join(random.choice(characters) for _ in range(length))
    return reason

def send_keys():
    # sending the url to the form
    url = web.find_element("xpath",'//*[@id="url"]')
    url.clear()
    url.send_keys(attach_random_characters(base_url))

    username = web.find_element("xpath",'//*[@id="reportedBy"]')
    username.clear()
    username.send_keys(generate_random_username())

    email = web.find_element("xpath",'//*[@id="email"]')
    email.clear()
    email.send_keys(generate_random_email())

    reason = web.find_element("xpath",'//*[@id="reason"]')
    reason.clear()
    reason.send_keys(generate_random_reason())

    submit = web.find_element("xpath",'/html/body/div/div[1]/div[1]/div[3]/button')
    submit.click()

while True:
    send_keys()
    time.sleep(2)
