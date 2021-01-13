import requests

api_key = 'goldapi-j37uxukjtotcud-io'
api_header = {"x-access-token": api_key}
price_api_url = 'https://www.goldapi.io/api/XAU/INR'
account_stat_api_url = 'https://www.goldapi.io/api/stat'

def validate_api_response(api_response):
    if(api_response != None and api_response.status_code == 200):
        return True
    else:
        print('Invalid API response')

def print_price(api_response):
    gold_price_results = api_response.json()
    if(gold_price_results != None and gold_price_results['price'] != None):
        usd_price = gold_price_results['price']
        inr_price = round(usd_price/28.5,2)
        print('Gold price: {0}'.format(inr_price))
    else:
        print('nvalid contents in response')

def get_current_gold_price():
    api_response = requests.get(price_api_url, headers = api_header)
    if(validate_api_response(api_response)):
        print_price(api_response)

def get_account_api_request_stats():
    api_response = requests.get(account_stat_api_url, headers = api_header)
    if(validate_api_response(api_response)):
        print(api_response.json())

#get_account_api_request_stats()
get_current_gold_price()



