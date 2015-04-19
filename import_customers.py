import csv
from juiceprogram.models import Customer, new_customer


def import_customers():
    i = 0
    with open('jp.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row
            if i>0:
                save_customer(row)
            i+=1


def save_customer(customer):
    fname = customer[0]
    lname = customer[1]
    notes = customer[4]

    if customer[3] == '':
        juices = 0
    else:
        juices = int(customer[3])

    new_customer(fname, lname, juices, 0, notes) 

import_customers()
