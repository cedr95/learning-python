import csv
import random
import time
import shutil
from datetime import date



def read_file(file='sales_data.csv'):
    empty_data =[]
    with open(file, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # If your CSV file has a header row, you can skip it.
        for row in csv_reader:
          empty_data.append(row)
    return empty_data


def write_data(data: list):
   with open('sales_data_2.csv', 'w', newline='') as file:
      csv_writer = csv.writer(file)
      for row in data:
         csv_writer.writerow(row)

def shuffle_data(data: list):
   shuffled = (random.shuffle(data))
   if shuffled != data:
      print("Data was successfully shuffled")
   else:
      print("Data was not shuffled")
   return data

def file_backup():
   shutil.copy("sales_data.csv", "sales_data_2.csv")
   today = date.today()
   date_format = today.strftime("%d %b %Y")
   print(f"Your file was backed up on {date_format}")


def everything():
   og_file = read_file()
   file_backup()
   shuffled_data = shuffle_data(og_file)
   write_data(shuffled_data)

everything()