"""Program to Create, Update, Delete, List, and View contacts"""

import json
import mysql.connector
from starlette.routing import Route
from starlette.applications import Starlette
from starlette.responses import JSONResponse

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    auth_plugin="mysql_native_password",
    database="contactApp"
)
mycursor = mydb.cursor()


def list_all_contacts(request):
    """Function list all contacts."""

    contact_list = []

    #  Query to select all contacts.
    mycursor.execute("""SELECT JSON_OBJECT(
    "contactId",contact.contactId,"fname",fname,"lname",lname,"phone",(
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT("type",type,"value",number)
            ) from phoneNo where contact.contactId = phoneNo.contactId
    ),
    "email",(
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT("type",type,"value",email)
            ) from email where contact.contactId = email.contactId
        )
    ) as contacts 
    from contact 
    left join phoneNo on phoneNo.contactId = contact.contactId 
    left join email on email.contactId = contact.contactId 
    group by contact.contactId""")

    result = mycursor.fetchall()
    for i in result:
        contact_data = json.loads(i[0])
        contact_list.append(contact_data)

    return JSONResponse(contact_list)


async def create_contact(request):
    """Function to create a new contact."""
    try:
        data = await request.json()
    except json.decoder.JSONDecodeError:
        return JSONResponse({"status":"JSONDecodeError"}, status_code=400)

    try:
        fname = data["fname"]
        lname = data["lname"]
        phone = data["phone"]
        email = data["email"]
        mycursor.execute(f'INSERT INTO contact(fname, lname) '
        f'VALUES("{fname}", "{lname}")')

        mycursor.execute(f'SELECT max(contactId) from contact')
        contactId = mycursor.fetchall()[0][0]
        
        for number in phone:
            mycursor.execute(f'INSERT INTO phoneNo(contactId, type, number) '
            f'VALUES({contactId}, "{number["type"]}", "{number["value"]}")')
        
        for address in email:
            mycursor.execute(f'INSERT INTO email(contactId, type, email) '
            f'VALUES({contactId}, "{address["type"]}", "{address["value"]}")')

        mydb.commit()
    except:
        mydb.rollback()
        return JSONResponse({"status":"Contact create failed"})

    return JSONResponse({"status":"Contact created"})


#  CONTACT DETAILS.
async def contact_details(request):
    """Function to get contact details of a single person. 
    Recieve contactId from url.
    """

    contactId = request.path_params['contactId']

    #  Query to get all contact information using contactId.
    mycursor.execute(f"""SELECT JSON_OBJECT(
    "contactId",contact.contactId,"fname",fname,"lname",lname,"phone",(
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT("type",type,"value",number)
            ) from phoneNo where contact.contactId = phoneNo.contactId
    ),
    "email",(
        SELECT JSON_ARRAYAGG(
            JSON_OBJECT("type",type,"value",email)
            ) from email where contact.contactId = email.contactId
        )
    ) as contacts 
    from contact 
    left join phoneNo on phoneNo.contactId = contact.contactId 
    left join email on email.contactId = contact.contactId 
    where contact.contactId = {contactId}""")

    try:
        result = mycursor.fetchall()
        contact_details = json.loads(result[0][0])
        return JSONResponse(contact_details)
    except IndexError:
        return JSONResponse({"status": "error","message": "Invalid contactId"},status_code=400)
        
    
#  SEARCH CONTACT.
def search_contacts(request):
    """Function to search contacts using name."""

    result = []

    name = request.query_params['name']

    # Query to get all contacts list using name.
    mycursor.execute(f"""SELECT json_arrayagg(json_object(
    "fname",contact.fName,
    "lname",contact.lName,
    "contactId",contact.contactId,"email",
    (select json_arrayagg(json_object("type",type,"value",email)) 
    from email where email.contactId = contact.contactId),"phone",
    (select json_arrayagg(json_object("type",type,"value",number)) 
    from phoneNo where phoneNo.contactId = contact.contactId)))as contact
    from
    contact
    WHERE
    contact.fname = '{name}'
    or contact.lname = '{name}'""")

    try:
        name_result = json.loads(mycursor.fetchall()[0][0])
        result.extend(name_result)
    except TypeError:
        return JSONResponse([])
        
    return JSONResponse(result, status_code=200)


def delete_contact(request):
    """Function to delete a contact."""

    contactId = request.path_params['contactId']

    mycursor.execute(f"SELECT * FROM contact WHERE contactId = '{contactId}'")
    result = mycursor.fetchall()
    if result == []:
        return JSONResponse({"status": "Invalid contactId"},status_code=400)

    mycursor.execute(f"DELETE FROM contact WHERE contactId = '{contactId}'")
    mydb.commit()
    return JSONResponse({"status": "Contact Deleted"})


async def update_contact(request):
    """Function to update contact details in database. phoneId and emailId 
    are passed in json string inside phone and email to update phone number 
    and emails. phone and email data without ids are inserted to the table 
    as new number and new email
    """

    contactId = int(request.path_params['contactId'])

    data = await request.json()
    fname = data["fname"]
    lname = data["lname"]
  
    mycursor.execute(f"UPDATE contact SET fname = '{fname}', "
                        f"lname = '{lname}' WHERE contactId = '{contactId}'")

    #  To update, delete, and add phone numbers.
    table_phoneid_list = []
    mycursor.execute(f"SELECT phoneId from phoneNo where contactId = "
    f"'{contactId}'")
    result = mycursor.fetchall()
    if result == []:
        mydb.rollback()
        return JSONResponse({"Staus": "Invalid contactId"}, status_code=400)
    
    for i in result:
        table_phoneid_list.append(i[0])    

    phone = data["phone"]

    phoneId_list = []
    phone_list = []

    for item in phone:

        #  To update existing phoneno.
        if "phoneId" in item:
            phone_list.append(item)
            phoneId_list.append(int(item["phoneId"]))
            mycursor.execute(f'UPDATE phoneNo SET type = "{item["type"]}"'
            f', number = "{item["value"]}"'
            f'where phoneId = "{item["phoneId"]}"')

        #  To add new phonno.
        else:
            mycursor.execute(f'INSERT INTO phoneNo(contactId, type, number) '
            f'VALUES({contactId}, "{item["type"]}", "{item["value"]}")')
    
    #  To delete phoneno.
    index = 0
    for item in table_phoneid_list:
        if item not in phoneId_list:
            mycursor.execute(f"delete from phoneNo where phoneId = {item}")
            index += 1


    #  To update, delete, and add email addresses.
    table_emailId_list = []
    mycursor.execute(f"SELECT emailId from email where contactId = "
    f"'{contactId}'")
    result = mycursor.fetchall()
    for i in result:
        table_emailId_list.append(i[0])
    
    email = data["email"]

    emailId_list = []
    email_list = []

    for item in email:

        #  To update existing email.
        if "emailId" in item:
            email_list.append(item)
            emailId_list.append(int(item["emailId"]))
            mycursor.execute(f'UPDATE email SET type = "{item["type"]}"'
            f', email = "{item["value"]}" '
            f'where emailId = "{item["emailId"]}"')

        #  Add new email.
        else:
            mycursor.execute(f'INSERT INTO email(contactId, type, email) '
            f'VALUES({contactId}, "{item["type"]}", "{item["value"]}")')
    
    #  To delete email.
    index = 0
    for item in table_emailId_list:
        if item not in emailId_list:
            mycursor.execute(f"delete from email where emailId = {item}")
            index += 1

    mydb.commit()

    return JSONResponse({"status": "Contact edited"})


routes = [
    Route("/contacts", endpoint=list_all_contacts, methods=["GET"]),
    Route("/contact", endpoint=create_contact, methods=["POST"]),
    Route("/contacts/{contactId:int}", endpoint=contact_details, methods=["GET"]),
    Route("/contacts/search/", endpoint=search_contacts, methods=["GET"]),
    Route("/contacts/{contactId:int}", endpoint=delete_contact, methods=["DELETE"]),
    Route("/contacts/{contactId:int}", endpoint=update_contact, methods=["PUT"])
]

app = Starlette(
    routes=routes
)
