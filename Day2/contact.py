"""Program to List, Create, Add, Edit, Delete contacts and save to a JSON file"""

import json


class CreateContact:
    """"""

    def __init__(self, fname, lname, phone): #constructor
        self.fname = fname
        self.lname = lname
        self.phone = phone
    
    def create_new_contact(self):
        contact_data = {}
        contact_data['fname'] = self.fname
        contact_data['lname'] = self.lname
        contact_data['phone'] = self.phone
        print("new contact added")
        print(contact_data)
        print(type(contact_data))
        return contact_data
        # print("Details:", self.fname, self.lname, self.phone)

def create_contact():
    """Function to create a new contact and add to contacts list."""

    new_contact_list = []
    phone_number_list = []

    print("Enter Details")
    fname = input("Enter first name:")
    lname = input("Enter last name:")
    choice = input("Add number?(Y/N):")

    while choice == 'y' or choice == 'Y':

        number_type = input("Enter type: ")
        number = input("Enter phone number: ")

        contact_dict = {}
        contact_dict['type'] = number_type
        contact_dict['value'] = number
        phone_number_list.append(contact_dict)
        print("Contact added")
        choice = input("Add number?(Y/N):")
    


    new_contact = CreateContact(fname, lname, phone_number_list)
    new_contact_data = new_contact.create_new_contact()

    try:
        contact_file_object = open("contact.json", "r")
        data_list = contact_file_object.read()
        data_list = json.loads(data_list)

        contact_file_object.close()
        print(data_list)
    except:
        print("no data")
        data_list = []

    data_list.append(new_contact_data)
    print(data_list)

    return data_list # New contact data.

def main_contact_function():
    """Main function to display actions to be performed on contacts list.
    """
    try:
        contact_file_object = open("contact.json", "r")
        data_list = contact_file_object.read()
        data_list = json.loads(data_list)

        contact_file_object.close()
    except:
        print("no data")
        data_list = []

    print("Contacts App\n")

    choice = 0
    choice_list = [1, 2, 3, 4]
    new_contact_list = []

    while choice not in choice_list:
        print("Choose Action\n\t1.Create new contact\n\t2.List Contacts\n\t3.Edit a contact\n\t4.Delete Contact\n\t5.Search a contact\n\t6.Exit")
        choice = int(input("Enter option: "))
        print(f"Choice : {choice}")

        if choice == 1:
            print("1.Create Contact")
            new_contact_details = create_contact()
            print(new_contact_details)
            new_contact_list.append(new_contact_details)

            json_object = json.dumps(new_contact_list, indent = 4)
            print(json_object)
  
            # Writing to sample.json
            with open("contact.json", "w") as outfile:
                outfile.write(json_object)
            outfile.close()
            choice = 0

        elif choice == 2:
            contact_file_object = open("contact.json","r")
            data_list = contact_file_object.read()
            data_list = json.loads(data_list)
            contact_file_object.close()
            print("2.List Contacts")
            new_list = sorted(data_list, key=lambda item: item['fname'])
            print("data:")
            for i in new_list:
                print(f"\n{i['fname']} {i['lname']}\t", end="")
                for multiple_number in i['phone']:
                    print(f"{multiple_number['type']}-{multiple_number['value']}\t", end="\t")
            print()
            choice = 0

        elif choice == 3:
            print("3.Edit a contact")
            contact_file_object = open("contact.json","r")
            data_list = contact_file_object.read()
            data_list = json.loads(data_list)
            contact_file_object.close()
            user_input_fname = input("Enter the name of the contact you wish to edit: ")
            data = [item for item in data_list if item["fname"] == f"{user_input_fname}"][0]
            print(data)
            choice = input("Edit data?(Y\\N):")
            if choice == 'y' or choice == 'y':
                # data_list.remove(data)
                # if choice == 'y' or choice == 'y':
                    sub_choice_list = [1, 2, 3]
                    sub_choice = 0
                    sub_choice = int(input("Choose from 1.fname, 2.lname, 3.phone, 4.exit number to edit\n \
                    (choose: 1/2/3/4):"))
                    while sub_choice in sub_choice_list[:3]:
                        if sub_choice == 1:
                            data["fname"] = input("Enter first name")
                            temp_data = data
                            data_list.remove(temp_data)
                            data_list.append(data)
                            json_object = json.dumps(data_list, indent = 4)
                            with open("contact.json", "w") as outfile:
                                outfile.write(json_object)
                            outfile.close()

                        elif sub_choice == 2:
                            data["lname"] = input("Enter last name")
                            temp_data = data
                            data_list.remove(temp_data)
                            data_list.append(data)
                            json_object = json.dumps(data_list, indent = 4)
                            with open("contact.json", "w") as outfile:
                                outfile.write(json_object)
                            outfile.close()
                        
                        elif sub_choice == 3:
                            temp_data = data
                            index = 1
                            print("type:")
                            for items in data:
                                number_type = [number_type for number_type in data['phone']]
                            for i in number_type:
                                print(index, ".", i)
                                index += 1
                            phone_type_choice = int(input("Choose number(by index):"))
                            print("index = ", phone_type_choice)
                            phone_type_choice -= 1
                            
                            print("Edit or Delete")

                            try:
                                while phone_type_choice >= 0 and phone_type_choice < index:
                                    print("hello")
                                    phone_data = number_type[phone_type_choice]
                                    print("hello")
                                    print(phone_data)
                                    type_or_value = int(input("change 1.Type, 2.Number"))
                                    if type_or_value == 1:
                                        temp_phone_data = phone_data
                                        phone_data['type'] = input("Enter new type")
                                        number_type.remove(temp_phone_data)
                                        number_type.append(phone_data)
                                        print(data)
                                        data_list.remove(temp_data)
                                        data_list.append(data)
                                        json_object = json.dumps(data_list, indent = 4)
                                        with open("contact.json", "w") as outfile:
                                            outfile.write(json_object)
                                        outfile.close()
                                        break
                                    elif type_or_value == 2:
                                        temp_phone_data = phone_data
                                        phone_data['value'] = input("Enter new number")
                                        number_type.remove(temp_phone_data)
                                        number_type.append(phone_data)
                                        print(data)
                                        data_list.remove(temp_data)
                                        data_list.append(data)
                                        json_object = json.dumps(data_list, indent = 4)
                                        with open("contact.json", "w") as outfile:
                                            outfile.write(json_object)
                                        outfile.close()
                                        break
                            except IndexError:
                                print("No phone number found")        
                        
                        elif sub_choice not in sub_choice_list:
                            break
                        sub_choice = int(input("Choose from 1.fname, 2.lname, 3.phone,\
                             4.exit number to edit\n\
                    (choose: 1/2/3/4):"))

                    print("yes1")    
            choice = 0



        elif choice == 4:
            print("DELETE")
            contact_file_object = open("contact.json","r")
            data_list = contact_file_object.read()
            data_list = json.loads(data_list)
            contact_file_object.close()
            print("Delete data by name:")
            user_input_fname = input()
            data = [item for item in data_list if item["fname"] == f"{user_input_fname}"][0]
            print(data)
            data_list.remove(data)
            print(data_list)
            json_object = json.dumps(data_list, indent = 4)
            print(json_object)
  
            # Writing to sample.json
            with open("contact.json", "w") as outfile:
                outfile.write(json_object)
            outfile.close()
            choice = 0

        # Contact Search.
        elif choice == 5:
            contact_file_object = open("contact.json","r")
            data_list = contact_file_object.read()
            data_list = json.loads(data_list)
            contact_file_object.close()
            print("Search data by name:")
            user_input_fname = input()
            data = [item for item in data_list if item["fname"] == f"{user_input_fname}"]
            print(data)
            choice = 0
        
        elif choice == 6:
            break


main_contact_function()
