from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup
from .login import get_session_id
router = APIRouter()


def get_order_list(headers):
    print(headers)
    url = "https://ca.lorealpartnershop.com/en/orders/"
    response = requests.request("GET", url, headers=headers, data={})
    soup = BeautifulSoup(response.text, "html.parser")
    order_list = []
    for a in soup.find_all('a', href=True):
        if "orderdetail" in a['href']:
            order_list.append(a['href'])

    return order_list
@router.get("/search_product/")
def search_product(product_name: str):
    print(f"Searching product {product_name}")
    item_name = product_name;
    session_id = get_session_id()
    headers = {
        'authority': 'ca.lorealpartnershop.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': '',
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

    new_cookie_value = 'dwsid='+session_id
    headers['cookie'] = new_cookie_value

    print("old_session_id="+session_id)
    order_list = get_order_list(headers)

    if len(order_list) == 0:
        get_session_id.cache_clear()
        session_id = get_session_id()
        new_cookie_value = 'dwsid=' + session_id
        print("new_cookie_value="+new_cookie_value)
        headers['cookie'] = new_cookie_value
        order_list = get_order_list(headers)

    count = 0

    orders = {}

    print(order_list)
    for order in order_list:
        response_order_detail = requests.request("GET", order, headers=headers, data={})

        soup = BeautifulSoup(response_order_detail.text, "html.parser")

        expected_shipping_date = soup.find("div", {"class": "c-lpsordersdetails__orderShipmentFeatures"})
        expected_shipping_date = expected_shipping_date.text.split("\n")[17] if expected_shipping_date is not None else ""

        order_creation_date = soup.find_all("span", {"class": "c-lpsordersdetails__orderInfo"})[1]

        order_creation_date = order_creation_date.nextSibling.nextSibling.text.replace("\n", "")

        for div in soup.find_all("div", {"class": "c-singleorderdetail__product-line"}):
            prod_name = div.text.split("\n")[2]

            if item_name.lower() in prod_name.lower():
                order_value = {"prod_name": prod_name,
                               "order_no":order.split("/")[-1].split("=")[-1],
                               "created_date":order_creation_date,
                               "exp_shipping_date":expected_shipping_date}

                orders.append(order_value)
                count += 1

        if count > 3:
            break
    return orders