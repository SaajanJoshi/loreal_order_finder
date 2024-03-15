import requests

url = "https://ca.lorealpartnershop.com/en/home/?alert=&validateform=success"

payload = {}
headers = {
  'authority': 'ca.lorealpartnershop.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': 'dwsid=UyXbcBQ02kMMefHsKSoEbGihk5Cdv8aMSqZ_3STFuXdeEJ4kMcDAirgxJxkKDLpeOjFgQQ4fXM5jIRJbDVJUrQ==; __cf_bm=hNbt7WLwaWXlTKrjPS8KbXBoqfZS6VeEJZ4PCtzB9BI-1710475910-1.0.1.1-Giqzdkjfzcmp3lI5YfvLWGuc6LB6ddAAxs12_CQysY4kpRHCGrgGBQWo.F824QoiM7ehfS5CvQcn8rwgPmCf5g; __cq_dnt=1; dw_dnt=1; dwanonymous_c12a0e62e3aa4cd725053c1b8344dd31=91462792a19e1a3855f3f82b43; sid=IqbBePRlOWjlm7il00vOXxkiiZh97iWno0Q',
  'referer': 'https://ca.lorealpartnershop.com/en/login/',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)