"""Program to List, Create, Add, Edit, Delete contacts and save to a JSON file"""

import json


def get_data():
    """Takes data from json file and saves into a variable."""

    file_object = open('contact.json', 'r')
    data_list = file_object.read()
    file_object.close()

    return data_list


def list_contacts():
    """Function to list all contacts."""

    data_list = get_data()
    if data_list == "":
        print("No contacts to display\n")
    else:
        data_list = json.loads(data_list)
        data_list = sorted(data_list, key=lambda item: item['fname'])
        for item in data_list:
            print("--------------------------------------------------------")
            print(f'{item["fname"]} {item["lname"]}')
            for phone in item['phone']:
                print(f'phone: {phone["type"]}\tnumber: {phone["value"]}')
            index = 1
            for email in item['email']:
                if(index >= 2):
                    print("",end=" ")
                print(f'email: {email["type"]}\temail: {email["value"]}')
        print("--------------------------------------------------------")


def create_contact():
    """Function to create a new contact."""

    data_list = get_data()  # To fetch data from file.
    if data_list == "":
        data_list = []
    else:
        data_list = json.loads(data_list)
    
    contact_dict = {}
    contact_dict['fname'] = input("Enter first name: ")
    contact_dict['lname'] = input("Enter last name: ")

    #  To add phone number.
    choice = input("Add number?(Y/N): ")
    phone_number_list = []

    while choice != "n" and choice != "N":
        phone_dict = {}
        phone_dict['type'] = input("Enter type: ")
        phone_dict['value'] = input("Enter number: ")
        phone_number_list.append(phone_dict)
        choice = input("Add another number?(Y/N): ")
    contact_dict['phone'] = phone_number_list

    #  To add email address.
    choice = input("Add email?(Y/N): ")
    email_list = []

    while choice != 'n' and choice != 'N':
        email_dict = {}
        email_dict['type'] = input("Enter type: ")
        email_dict['value'] = input("Enter email: ")
        email_list.append(email_dict)
        choice = input("Add another email?(Y/N): ")
    contact_dict['email'] = email_list

    data_list.append(contact_dict)
    json_object = json.dumps(data_list, indent = 4)

    with open("contact.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()


def search_contact():
    """Function to search for a contact."""

    data_list = get_data()
    print()

    if data_list == "":
        print("No contacts")
        return 0

    data_list = json.loads(data_list)
    name = input("Enter first name to search: ")
    
    data_fname = [item for item in data_list if item["fname"] == f'{name}']

    if data_fname == []:
        print(f'contact "{name}" doesnt exist.')
    else:
        for data in data_fname:
            print("--------------------------------------------------------")
            print(f'{data["fname"]} {data["lname"]}')
            for item in data['phone']:
                print(f'phone: {item["type"]}\tnumber: {item["value"]}')
            for item in data['email']:
                print(f'email: {item["type"]}\taddress: {item["value"]}')
        print("--------------------------------------------------------")


def edit_contact():
    """Function to edit contacts."""

    data_list = get_data()
    if data_list == "":
        print("No contacts to edit.")
        return
    
    data_list = json.loads(data_list)

    name = input("Enter the contact name to edit: ") 
    try:
        data = [item for item in data_list if item["fname"] == f"{name}"]
        temp_data = data

        data = data[0]
        print(data['fname']," ",data['lname'])
        print(f'''phone: {data['phone']}\nemail: {data['email']}''')
        choice = input("Edit data?(Y/N):")
        while choice == 'y' or choice == 'Y':
            try:
                sub_choice = int(input(
                    f'Choose from 1.fname, 2.lname, 3.phone, '
                    f'4.email, 0.exit to edit\n'
                    f'(choose: 1/2/3/4/0):'
                ))

                if sub_choice == 1:
                    data['fname'] = input("Enter first name")
                    choice = 'y'
                
                elif sub_choice == 2:
                    data['lname'] = input("Enter last name")
                    choice ='y'
                
                # To edit phone number.
                elif sub_choice == 3:
                    phone_list = data['phone']

                    index = 1
                    try:
                        for item in phone_list:
                            print(f'{index}.{item}')
                            index += 1

                        phone_index = int(input("Choose number by index"))
                        phone_index -= 1

                        if phone_index >= 0:
                            print(phone_list[phone_index])
                            user_option = int(input("1.Edit/2.Delete"))

                    
                            if user_option == 1:
                                number_details = phone_list[phone_index]
                                number_details['type'] = input("Enter type: ")
                                number_details['value'] = input("Enter number: ")
                                phone_list[phone_index] = number_details
                            if user_option == 2:
                                phone_list.pop(phone_index)
                                data['phone'] = phone_list
                        

                    except:
                        print("No number to edit")
                    
                    choice = 'y'   

                elif sub_choice == 4:
                    email_list =  data['email']

                    index = 1
                    try:
                        for item in email_list:
                            print(f'{index}.{item}')
                            index += 1

                        email_index = int(input("Choose number by index"))
                        email_index -= 1

                        if email_index >= 0:
                            print(email_list[email_index])
                            user_option = int(input("1.Edit/2.Delete"))

                            if user_option == 1:
                                number_details = email_list[email_index]
                                number_details['type'] = input("Enter type: ")
                                number_details['value'] = input("Enter email: ")
                                phone_list[email_index] = number_details
                            elif user_option == 2:
                                email_list.pop(email_index)
                                data['phone'] = email_list

                    except:
                        print("No email to edit")

                    choice = 'y' 


                elif sub_choice == 0:
                    data_list.remove(temp_data[0])
                    data_list.append(data)
                    print("-----------")
                    print("Edit saved")
                    print("-----------")

                    json_object = json.dumps(data_list, indent = 4)
                    with open("contact.json", "w") as outfile:
                        outfile.write(json_object)
                    outfile.close()

                    choice = 'n'
            except:
                print("Wrong option")
    except:
        print(f'No contact named {name}')
        print("---------------------------------------------------------\n")
        return
    


def delete_contact():
    """Function to delete a contact."""

    data_list = get_data()
    if data_list == "":
        print("No contacts to delete")
        return

    data_list = json.loads(data_list)

    try:
        name = input("Enter the contact name to delete: ")
        data = [item for item in data_list if item["fname"] == f"{name}"]
    except:
        print(f'No contact named {name}\n')
        return

    print(data[0])
    data_list.remove(data[0])

    json_object = json.dumps(data_list, indent = 4)
    with open("contact.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()


def contacts_application():
    """Main function that displays main menu."""

    choice_list = [0, 1, 2, 3, 4, 5]
    choice = 100

    while choice not in choice_list:

        print("Contacts App\n")
        
        print("Choose",
            f'\n\t1. List contacts'
            f'\n\t2. Create new contact'
            f'\n\t3. Search a contact'
            f'\n\t4. Edit a contact'
            f'\n\t5. Delete a contact'
            f'\n\t0. Exit'
        )
        
        try:
            choice = int(input("Enter a choice : "))
        except:
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
