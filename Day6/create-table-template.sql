CREATE DATABASE contactApp
    DEFAULT CHARACTER SET = 'utf8mb4';
CREATE TABLE contact (
    contactId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fName VARCHAR(20),
    lName VARCHAR(20)
);
CREATE TABLE phoneNo (
    phoneId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    contactId INT NOT NULL,
    type VARCHAR(10),
    number VARCHAR(20),
    FOREIGN KEY (contactId) REFERENCES contact(contactId) ON DELETE CASCADE
);
CREATE TABLE email (
    emailId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    contactId INT NOT NULL,
    type VARCHAR(10),
    email VARCHAR(20),
    FOREIGN KEY (contactId) REFERENCES contact(contactId) ON DELETE CASCADE
);
SELECT JSON_OBJECT(
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
    group by contact.contactId;

SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
            "phoneId", phoneId,
            "type",type,
            "value", number
        )
    ) FROM phoneNo where contactId = 19;

delete from phoneNo where phoneId = 22;
rollback;



SELECT JSON_ARRAYAGG(JSON_OBJECT(
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
    )) as contacts 
    from contact 
    left join phoneNo on phoneNo.contactId = contact.contactId 
    left join email on email.contactId = contact.contactId
    where contact.fname = 'Alen'
    group by contact.contactId;

SELECT json_arrayagg(json_object(
    "fname",contact.fName,
    "lname",contact.lName,
    "contactId",contact.contactId,"email",
    (select json_arrayagg(json_object("type",type,"value",email)) from email where email.contactId = contact.contactId),"phone",
    (select json_arrayagg(json_object("type",type,"value",number)) from phoneNo where phoneNo.contactId = contact.contactId)))as contact
from
    contact
WHERE
    contact.fname = 'Alen'
    or contact.lname = 'Alen';

select json_arrayagg(email) from email;
SELECT EXISTS(SELECT * from contact WHERE fname='Alen');
