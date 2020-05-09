import csv
import os.path
from os import path

def insert_msg(email, flight, msg):
    print("Checking if 'messages.csv' exists...")
    if path.exists('helpdesk\\messages.csv'):
        print("Opening 'messages.csv'...")
        csv_file = open('helpdesk\\messages.csv', 'a', newline = '')
    else:
        print("File does not exist...\nCreating 'messages.csv'...")
        print("Opening 'messages.csv'...")
        csv_file = open('helpdesk\\messages.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([email, flight, msg])
    csv_file.close()