import pymongo
from bson import ObjectId

connection = ''
database = ''
QR_Gen_Accounts = ''
QR_Read_Accounts = ''
Flights = ''
Luggage = ''
Complaint = ''

def get_obj_id(id):
    return ObjectId(id)

def main():
    global connection
    global database
    global QR_Gen_Accounts
    global QR_Read_Accounts
    global Flights
    global Luggage
    global Complaint

    connection = pymongo.MongoClient(host = 'localhost', port = 27017)
    database = connection['DBMS_Project']
    QR_Read_Accounts = database['QR_Read_Accounts']
    QR_Gen_Accounts = database['QR_Gen_Accounts']
    Flights = database['Flights']
    Luggage = database['Luggage']
    Complaint = database['Complaint']
