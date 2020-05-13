import csv
import os.path
from os import path
import mongo_api

def insert_msg(email, flight, msg):
    print("Checking if 'messages.csv' exists...")
    if path.exists('csv\\messages.csv'):
        print("Opening 'messages.csv'...")
        csv_file = open('csv\\messages.csv', 'a', newline = '')
    else:
        print("File does not exist...\nCreating 'messages.csv'...")
        print("Opening 'messages.csv'...")
        csv_file = open('csv\\messages.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([email, flight, msg])
    csv_file.close()