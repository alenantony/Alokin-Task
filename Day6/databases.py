"""Program to List, Create, Add, Edit, Delete contacts and save data in MySQL database"""

import json
import mysql.connector

# To connect to contacts database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    auth_plugin="mysql_native_password",
    database="contacts"
)

mycursor = mydb.cursor()


def list_contacts():
    """To list all contacts in s=ascending order."""

    mycursor.execute("SELECT * FROM contacts")
    result = mycursor.fetchall()
    print(result.sort(key=lambda x:x[1]))
    for contact in result:
        print("-------------------------------")
        print(f'{contact[1]} {contact[2]}\nphone:')
        phone = eval(contact[3])
        index = 1
        for number in phone:
            print(index, number)
            index += 1
        print("email:")
        index = 1
        email = eval(contact[4])
        for email in email:
            print(index, email)
            index += 1
    print("-------------------------------")


def create_contact():
    """Function to enter details for a new contact and to save it to the database."""

    choice = 'y'

    while choice == 'y' or choice == 'Y':
        fname = input("Enter first name")
        lname = input("Enter last name")
        
        phone_choice = 'y'
        phone_number_list = []

        while phone_choice == 'y' or phone_choice == 'Y':
            phone_dict = {}
            phone_dict["type"] = input("Enter phone type: ")
            phone_dict["value"] = input("Enter number: ")
            phone_number_list.append(phone_dict)
            phone_choice = input("Add another number?(Y/N): ")
        
        phone_string = str(json.dumps(phone_number_list))
        
        email_choice = 'y'
        email_list = []

        while email_choice == 'y' or email_choice == 'Y':
            email_dict = {}
            email_dict["type"] = input("Enter email type: ")
            email_dict["value"] = input("Enter email: ")
            email_list.append(email_dict)
            email_choice = input("Add another email?(Y/N): ")

        email_string = str(json.dumps(email_list))

        query = """SELECT MAX(slno) FROM contacts"""
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result[0][0] == None:
            result = 1
        else:
            result = result[0][0] + 1

        query = """INSERT INTO contacts(slno, fname, lname, phone, email) VALUES(%s, %s, %s, %s, %s)"""
        values = (result, fname, lname, phone_string, email_string)

        mycursor.execute(query, values)
        mydb.commit()

        print("Contact Added")

        choice = 'n'


def search_contact():
    """Function to search for a contact using name"""
    try:
        name = input("Enter a name to search")
        mycursor.execute(f'SELECT fname, lname, phone, email from contacts where fname = "{name}"')
        result = mycursor.fetchall()[0]
    except:
        print("invalid contact")
        return
    
    fname = result[0]
    first_name = result[0]
    last_name = result[1]
    phone = eval(result[2])
    email = eval(result[3])
    print(f'----------------------------------')
    print(f'{first_name} {last_name}')
    print(f'\nphone :')
    index = 1
    for item in phone:
        print(f'{index} {item["type"]} {item["value"]}')
        index += 1
    print(f'\nemail :')
    index = 1
    for item in email:
        print(f'{index} {item["type"]} {item["value"]}')
        index += 1
    print(f'----------------------------------\n')


def edit_contact():
    """Function to edit contact - 1.Search contact by name 2.Edit"""

    name = input("Enter a name to edit")
    mycursor. execute(f'SELECT fname, lname, phone, email FROM contacts where fname = "{name}"')
    result = mycursor.fetchall()[0]
    fname = result[0]
    first_name = result[0]
    last_name = result[1]
    phone = eval(result[2])
    email = eval(result[3])
    
    print(f'----------------------------------')
    print(f'{first_name} {last_name}')
    print(f'\nphone :')
    index = 1
    for item in phone:
        print(f'{index} {item["type"]} {item["value"]}')
        index += 1
    print(f'\nemail :')
    index = 1
    for item in email:
        print(f'{index} {item["type"]} {item["value"]}')
        index += 1
    print(f'----------------------------------\n')

    edit = 'y'
    while edit == 'y':
        print(f'Choose 1.First Name, 2.Last Name,' 
                f'3.Phone, 4.Email to edit or 0.Exit')
        try:    
            choice = int(input("choose(1/2/3/4/0): "))
            print(choice)
        except:
            print("Invalid choice")

        if choice == 1:
            first_name = input("Enter first name")
            edit = 'y'

        elif choice == 2:
            last_name = input("Enter last name")
            edit = 'y'

        elif choice == 3:
            print(f'\nphone :')
            index = 1
            for item in phone:
                print(f'{index} {item["type"]} {item["value"]}')
                index += 1
            try:
                index = int(input("Choose number by index:"))
                index -= 1
                new_item = {}
                new_item["type"] = input("Enter type: ")
                new_item["value"] = input("Enter number: ")
                phone[index] = new_item
                print(phone)
            except ValueError:
                print("invalid choice")
                edit = 'y'
        
        elif choice == 4:
            print(f'\nemail :')
            index = 1
            for item in email:
                print(f'{index} {item["type"]} {item["value"]}')
                index += 1
            try:
                index = int(input("Choose email by index:"))
                index -= 1
                new_item = {}
                new_item["type"] = input("Enter type: ")
                new_item["value"] = input("Enter number: ")
                email[index] = new_item
                print(phone)
                edit = 'y'
            except ValueError:
                print("invalid choice")
                edit = 'y'
            
        elif choice == 0:
            phone = str(json.dumps(phone))
            email = str(json.dumps(email))
            query = (f'UPDATE contacts '
                    f'SET fname = "{first_name}", lname = "{last_name}", '
                    f"phone = '{phone}', email = '{email}' "
                    f'WHERE fname = "{fname}";')
            mycursor.execute(query)
            mydb.commit()
            break

        else:
            print("invalid choice")


def delete_contact():
    """Function to delete a contact. - 1.search contact by name 2.delete"""

    name = input("Enter contact name to delete")
    mycursor.execute(f'SELECT * FROM contacts WHERE fname = "{name}"')
    result = mycursor.fetchall()
    if result == []:
        print("no contact to delete")
    else:
        mycursor.execute(f'DELETE FROM contacts WHERE fname = "{name}"')

            
    mydb.commit()
    print()


def contacts_application():
    """Main function that displays the main menu"""

    choice_list = [0,1,2,3,4,5]
    choice = 100

    while choice not in choice_list:

        print("Choose:",
            f'\n\t1. List contacts'
            f'\n\t2. Create new contact'
            f'\n\t3. Search a contact'
            f'\n\t4. Edit a contact'
            f'\n\t5. Delete a contact'
            f'\n\t0. Exit'
        )
    
        try:
            choice = int(input("Enter a choice : "))
        except ValueError:
            print("Invalid choice")
        
        if choice == 1:
            list_contacts()
            choice = 100

        elif choice == 2:
            create_contact()
            choice = 100
        
        elif choice == 3:
            search_contact()
            choice = 100
        
        elif choice == 4:
            edit_contact()
            choice = 100

        elif choice == 5:
            delete_contact()
            choice = 100


contacts_application()