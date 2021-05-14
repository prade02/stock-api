import boto3
import datetime


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S")


def put_item(request_id, gold_price):
    time = get_current_time()
    dynamodb_client = boto3.client('dynamodb')
    table_name = 'gold_price'
    item = {"price_id": {"S": request_id}, "price": {"N":gold_price}, "time":{"S":time}}
    dynamodb_client.put_item(TableName=table_name, Item=item)
    print(f'updated price {gold_price} in table successfully')


# put_item('dfadf', "1000")