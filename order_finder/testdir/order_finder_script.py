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
    'cookie': 'dwanonymous_c12a0e62e3aa4cd725053c1b8344dd31=bcLupheQx4NLzaNVq1he27YVgC; _gcl_au=1.1.442117799.1710472994; __attentive_id=08dc1800d74546a382c6d38e4b2a105b; _attn_=eyJ1Ijoie1wiY29cIjoxNzEwNDcyOTk0MjIzLFwidW9cIjoxNzEwNDcyOTk0MjIzLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjA4ZGMxODAwZDc0NTQ2YTM4MmM2ZDM4ZTRiMmExMDViXCJ9In0=; __attentive_cco=1710472994223; _gid=GA1.2.660629526.1710472994; __attentive_dv=1; iadvize-6361-vuid=%7B%22vuid%22%3A%229483cb9150ee4821bca7839da7af5135c24a222d9a294%22%2C%22deviceId%22%3A%225d22ee8b-6971-4621-8587-80b883ceeb01%22%7D; attntv_mstore_email=david@cosmeticworld.ca:0; dwcustomer_c12a0e62e3aa4cd725053c1b8344dd31=abgEpxSugqKciFaN4L97ndh87G; onCart=true; __netid="h6zwhr7qmxhepl0ldej3taed2l"; __netsp="true"; __cf_bm=f9QcX0Ebm0Ei.U2OQBRmJzmkykCtoSRo3SK4bFXEkN4-1710475044-1.0.1.1-b93fX_EhYrWwqzZqdYLlKZb1WtRZR4MTb5N9880acGPyQoXy7w_fS5Tio7JRZ1Hv3k9rSIW4xOsBoHtpDRGJ9Q; _aqv=true; cf_clearance=J.Rak3noVxAu825PaEBMd.1DIfb2ioth9zqLr47iTSU-1710475046-1.0.1.1-cR8tVbpFE6wecTImoqkgYfD_vwR9mcI2ljJIx6135lbR0GrbWqYiACOfL6PJwxxu6cp_3KA_KSK1Y3mjCciQvg; __attentive_ss_referrer=https://ca.lorealpartnershop.com/en/accountshow/; sid=IqbBePRlOWjlm7il00vOXxkiiZh97iWno0Q; _dc_gtm_UA-122307645-3=1; _dc_gtm_UA-74428248-1=1; announcement=notif-5b436f6c6c656374696f6e2069643d363436343236355d616e6e6f756e63656d656e742d706f70696e; _ga=GA1.2.1411889501.1710472994; __attentive_pv=12; __cq_dnt=1; dw_dnt=1; _ga_96H14XGK1M=GS1.1.1710475044.2.1.1710475474.37.0.0; _ga_50B660WM08=GS1.1.1710475044.2.1.1710475474.37.0.0; _gali=dwfrm_login; RT="r=https%3A%2F%2Fca.lorealpartnershop.com%2Fen%2Flogin%2F&ul=1710475474490"; dwsid=zD9EOrPsdA1Y233zy6--hfbMKiXG386xFS7ZU0UnWjX9NSbTr6120AkfJhXsA_gsJ1xnlQlySQNlFHsHkz_i9w==',
    'pragma': 'no-cache',
    'referer': 'https://ca.lorealpartnershop.com/en/login/',
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