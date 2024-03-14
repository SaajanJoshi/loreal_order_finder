import requests
from bs4 import BeautifulSoup

url = "https://ca.lorealpartnershop.com/en/orders/"
item_name = input("Enter the name of item: ");
print("Searching.......\n")
payload = {}
headers = {
    'authority': 'ca.lorealpartnershop.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'dwsid=oWgp5kKp5Gk4fVkcX5z_P6ConNXZLsurN8Qz0o3i4nGtMDaN50lPEIocPGKWRrZFjAc_OGjtzQ4oUqX9xVuj7w==;',
    'pragma': 'no-cache',
    'referer': 'https://ca.lorealpartnershop.com/en/accountshow/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
soup = BeautifulSoup(response.text, "html.parser")
order_list = []
for a in soup.find_all('a', href=True):
    if "orderdetail" in a['href']:
        order_list.append(a['href'])

if len(order_list) == 0:
    raise Exception("Renew the cookie")

count = 0
for order in order_list:
    response_order_detail = requests.request("GET", order, headers=headers, data=payload)

    soup = BeautifulSoup(response_order_detail.text, "html.parser")

    expected_shipping_date = soup.find("div", {"class": "c-lpsordersdetails__orderShipmentFeatures"})
    expected_shipping_date = expected_shipping_date.text.split("\n")[17] if expected_shipping_date is not None else ""

    order_creation_date = soup.find_all("span", {"class": "c-lpsordersdetails__orderInfo"})[1]

    order_creation_date = order_creation_date.nextSibling.nextSibling.text.replace("\n", "")

    items = []
    for div in soup.find_all("div", {"class": "c-singleorderdetail__product-line"}):
        prod_name = div.text.split("\n")[2]

        if item_name.lower() in prod_name.lower():
            print("Item name: " + prod_name + "\n" +
                  "Order Number : " + order.split("/")[-1].split("=")[-1] + "\n" +
                  "Order Created Date : " + order_creation_date + "\n"
                  "Expected Shipping Date : " + expected_shipping_date + "\n\n")
            count += 1

    if count > 3:
        break

