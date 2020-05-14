"""
# For a Boto3 client.
AA
"""
import boto3
from boto3.dynamodb.conditions import Key, Attr
from sys import exit


def create_table(ddb):
    table = ddb.create_table(
        TableName='Test_Table',

        KeySchema=[
            {
                'AttributeName': 'user_name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'user_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            }
        ],

        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='Test_Table')
    # print(table.item_count)


ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
ddbC = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

table_name = 'Test_Table'

existing_tables = ddbC.list_tables()['TableNames']
if table_name not in existing_tables:
    create_table(ddb)

table = ddb.Table(table_name)

print(table)

# Print all Items in Table


table.put_item(
    TableName=table_name,
    Item={
        'user_name': 'Larry',
        'last_name': 'Berlton',
        'age': 26
    }
)

table.put_item(
    TableName=table_name,
    Item={
        'user_name': 'Amber',
        'last_name': 'Corn',
        'age': 25
    }
)

print(table.scan()['Items'])
