import requests

api_key = 'goldapi-j37uxukjtotcud-io'
api_header = {"x-access-token": api_key}
price_api_url = 'https://www.goldapi.io/api/XAU/INR'
account_stat_api_url = 'https://www.goldapi.io/api/stat'

thingspeak_write_api_key = 'HSQ1I2JEHW9EHG4V'
thingspeak_insert_api_url = 'https://api.thingspeak.com/update'

def validate_api_response(api_response):
    if(api_response != None and api_response.status_code == 200):
        return True
    else:
        print('Invalid API response')

def add_record_to_backend(inr_price):
    endpoint = '{0}?api_key={1}&field1={2}'.format(thingspeak_insert_api_url,thingspeak_write_api_key,inr_price)
    response = requests.get(endpoint)
    if(validate_api_response(response)):
        print('Saved to backend')


def print_price(api_response):
    gold_price_results = api_response.json()
    if(gold_price_results != None and gold_price_results['price'] != None):
        usd_price = gold_price_results['price']
        inr_price = round(usd_price/28.5,2)
        print('Gold price: {0}'.format(inr_price))
        add_record_to_backend(inr_price)
    else:
        print('Invalid contents in response')

def get_current_gold_price(event,context):
    api_response = requests.get(price_api_url, headers = api_header)
    if(validate_api_response(api_response)):
        print_price(api_response)

def get_account_api_request_stats():
    api_response = requests.get(account_stat_api_url, headers = api_header)
    if(validate_api_response(api_response)):
        print(api_response.json())

get_account_api_request_stats()
#get_current_gold_price(None,None)



