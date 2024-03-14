import requests

url = "https://ca.lorealpartnershop.com/en/loginform/"

payload = 'dwfrm_login_username_d0qdlkozxlbp=david%40cosmeticworld.ca&dwfrm_login_password_d0maagvxplmz=Loreal123!&dwfrm_login_rememberme=true&dwfrm_login_login=SIGN%20IN'
headers = {
  'authority': 'ca.lorealpartnershop.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': """""",
  'origin': 'https://ca.lorealpartnershop.com',
  'referer': 'https://ca.lorealpartnershop.com/en/login/',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
}




response = requests.request("POST", url, headers=headers, data=payload)

print(response.headers['Set-Cookie'].split(";")[0].split("=")[1])