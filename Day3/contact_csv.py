"""Program to take name, phone numbers, emails from a csv file and validate 
and format contact details. Validate and correct phone numbers and emails
and save it to a new csv file.
"""

import re
from csv import reader


def validate_email(email):
    """Function to validate email address."""

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return email
    else:
        return "Invalid Email"


def validate_phone(phone_number):
    """Function to validate phone number and reformat if needed."""

    regex = r"^[+][1][(](\d{3})[)][ ](\d{3})[-](\d{4})$"
    if re.fullmatch(regex, phone_number):
        return phone_number
    else:
        new_number = ""

        for char in phone_number:
            if char.isdigit():
                new_number += char

        if len(new_number) < 10:
            return "Invalid number"
        
        #  To reformat number when there are only 10 digits.
        elif len(new_number) == 10:
            new_number = (f'+1({new_number[:3]}) '
            f'{new_number[3:6]}-{new_number[6:]}'
            )

        #  To reformat number when there are 11 digits and the first digit is 1.
        elif len(new_number) == 11:
            if new_number[0] == "1":
                new_number = (f'+1({new_number[1:4]}) '
                                f'{new_number[4:7]}-{new_number[7:]}')
                return new_number
            else:
                return "Invalid number"

        return new_number


def validate_data(row):
    """Function to validate data row by row."""

    new_row = []

    first_name = row[0]
    last_name = row[1]

    phone_1 = row[2]
    new_phone_1 = validate_phone(phone_1)
    phone_2 = row[3]
    new_phone_2 = validate_phone(phone_2)

    email_1 = row[4]
    new_email_1 = validate_email(email_1)
    email_2 = row[5]
    new_email_2 = validate_email(email_2)
    
    new_row.extend([first_name, last_name, phone_1, phone_2, email_1, email_2, 
        new_phone_1, new_phone_2, new_email_1, new_email_2])
    return new_row
    

#  To write headers in new file.
with open('new_contacts.csv', 'w') as write_object:
    write_object.write(f'First name,Last name,'
    f'Phone 1,Phone 2,Email 1,Email 2,'
    f'Phone 1 Validated,Phone 2 validated,'
    f'Email 1 validated,Email 2 validated')

        
#  To read from 'contacts.csv' file line by line.
with open('contacts.csv', 'r') as read_obj:

    csv_reader = reader(read_obj)
    index = 1
    for row in csv_reader:
        if index > 1:
            new_row = validate_data(row)
            print(index," ",new_row)
            data = ','.join(new_row)
            with open('new_contacts.csv', 'a') as write_object:
                write_object.write("\n"+data)
        index += 1
