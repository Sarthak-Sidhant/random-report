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
  length = random.randint(min_length, max_length)
  print(length)
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  return ''.join(random.choice(characters) for _ in range(length)) 

def attach_random_characters(base_url, random_text_length=10):
  random_string = generate_random_string()
  random_text = ''.join(random.choice(string.ascii_letters) for _ in range(random_text_length))
  gen_url = f"{base_url}/{random_text}{random_string}"
  return gen_url

base_url = "https://drive.google.com/drive/folders"
gen_url = attach_random_characters(base_url)

def generate_random_username(min_length=9, max_length=16):
  length = random.randint(min_length, max_length)
  print(length)
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  username = ''.join(random.choice(characters) for _ in range(length)) 
  return username

gen_username = generate_random_username()
print(gen_username)

def generate_random_email(min_length=11, max_length=24):
    length = random.randint(min_length, max_length)
    print(length)
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    email = ''.join(random.choice(characters) for _ in range(length)) + '@gmail.com'
    return email

gen_email = generate_random_email()
print(gen_email)

def generate_random_reason(min_length=30, max_length=50):
    length = random.randint(min_length, max_length)
    print(length)
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    reason = ''.join(random.choice(characters) for _ in range(length))
    return reason

gen_reason = generate_random_reason()
print(gen_reason)

print(gen_url)
print(gen_username)
print(gen_email)
print(gen_reason)


# sending the url to the form
url = web.find_element("xpath",'//*[@id="url"]')
url.send_keys(gen_url)

username = web.find_element("xpath",'//*[@id="reportedBy"]')
username.send_keys(gen_username)

email = web.find_element("xpath",'//*[@id="email"]')
email.send_keys(gen_email)

reason = web.find_element("xpath",'//*[@id="reason"]')
reason.send_keys(gen_reason)

submit = web.find_element("xpath",'/html/body/div/div[1]/div[1]/div[3]/button')
submit.click()
