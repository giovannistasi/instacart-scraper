import requests
from bs4 import BeautifulSoup

loginUrl = 'https://www.instacart.com/v3/dynamic_data/authenticate/login'
email = "bilbjdfgb@gmail.com"
password = "bilbjdfgb"

session = requests.Session()

payload = {
    "email": email,
    "password": password,
}

result = session.post(
	loginUrl,
	data = payload,
	headers = { "user-agent": "I'm a user" },
)

s = session.get('https://www.instacart.com', headers= {
    "user-agent": "I'm a user",
    "cookie": '_instacart_session=' + session.cookies.get_dict()['_instacart_session']
})

soup = BeautifulSoup(s.text, 'html.parser')

print (soup.find('h1').text)
print (soup.find('img')['src'])