import mysql.connector
import boto3
import json 

client = boto3.client('secretsmanager', region_name='us-east-1' )

response = client.get_secret_value(
    SecretId='stage/deloitte/mysql'
)

secretDict = json.loads(response['SecretString'])

#Create connection to mysql DB
mydb = mysql.connector.connect(
    host=secretDict['host'],
    user=secretDict['username'],
    passwd=secretDict['password'],
    database=secretDict['dbname']
)

mycursor = mydb.cursor()

sql = "INSERT INTO employees (id, name) VALUES (%s, %s)"
val = (2, "Cloud")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted...")



