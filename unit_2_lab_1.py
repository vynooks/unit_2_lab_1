'''
programmer: Allyson Licerio
date: January 30, 2026
program: Unit_2_lab_1.py
description: write a program that asks the user to enter an address and customer name as separate 
elements.
'''

#user inputs shipping address and customer name, etc.
civic_number=input("Enter Civic Number: ")
street_name=input("Enter Street Name: ")
city_name=input("Enter City Name: ")
province_code=input("Enter Province Code: ")
postal_code=input("Enter Postal Code: ")
customer_name=input("Enter Customer Name: ")

#output shipping address print
print('\nShip to: ')
print(customer_name)
print(civic_number,street_name)
print('{0}, {1} {2}'.format(city_name, province_code, postal_code))
