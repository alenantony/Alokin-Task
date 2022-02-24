CREATE DATABASE if not exists oldDatabase
    DEFAULT CHARACTER SET = 'utf8mb4';
CREATE TABLE if not exists oldDatabase.userDetails(
    userId INT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT
);
CREATE TABLE if not exists newDatabase.userInformation(
    userId INT PRIMARY KEY,
    fName TEXT,
    lName TEXT
);
INSERT INTO oldDatabase.userDetails (userId, firstName, lastName)
    VALUES(1, "Alen", "Antony");
INSERT INTO oldDatabase.userDetails (userId, firstName, lastName)
    VALUES(2, "Sachin", "Tendulkar");
INSERT INTO oldDatabase.userDetails (userId, firstName, lastName)
    VALUES(3, "Virat", "Kohli");
INSERT INTO oldDatabase.userDetails (userId, firstName, lastName)
    VALUES(4, "Brian", "Lara");
INSERT INTO oldDatabase.userDetails (userId, firstName, lastName)
    VALUES(5, "Jacques", "Kallis");
CREATE TABLE if not exists oldDatabase.userInformation(  
    userId int NOT NULL PRIMARY KEY COMMENT 'Primary Key',
    fName TEXT,
    lName TEXT
);
INSERT INTO oldDatabase.userInformation(userId, fName, lName)
    SELECT userId, firstName, lastName FROM oldDatabase.userDetails;
INSERT INTO newDatabase.userInformation(userId, fName, lName)
    SELECT userId, firstName, lastName FROM oldDatabase.userDetails;
CREATE TABLE if not exists oldDatabase.userAge(
    userId int NOT NULL PRIMARY KEY,
    userAge INT,
    FOREIGN KEY (userId) REFERENCES oldDatabase.userDetails(userId)
);
CREATE TABLE if not exists oldDatabase.allUserDetails(
    userId int NOT NULL PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    userAge TEXT,
    FOREIGN KEY (userId) REFERENCES oldDatabase.userDetails(userId)
);
CREATE TABLE if not exists oldDatabase.newTable(
    userId int NOT NULL PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    userAge TEXT,
    username TEXT,
    FOREIGN KEY (userId) REFERENCES oldDatabase.userDetails(userId)
);
INSERT INTO oldDatabase.userAge(userId, userAge)
    VALUES(1, 10);
INSERT INTO oldDatabase.userAge(userId, userAge)
    VALUES(2, 20);
INSERT INTO oldDatabase.userAge(userId, userAge)
    VALUES(3, 30);
INSERT INTO oldDatabase.userAge(userId, userAge)
    VALUES(4, 40);
INSERT INTO oldDatabase.userAge(userId, userAge)
    VALUES(5, 50);
INSERT INTO oldDatabase.allUserDetails (userId, firstName, lastName, userAge)
    SELECT oldDatabase.userDetails.userId, oldDatabase.userDetails.firstName, oldDatabase.userDetails.lastName, oldDatabase.userAge.userAge 
    FROM oldDatabase.userDetails 
    INNER JOIN oldDatabase.userAge 
    where oldDatabase.userDetails.userId = oldDatabase.userAge.userId;
INSERT INTO oldDatabase.newTable(userId, firstName, lastName, userAge)
    SELECT oldDatabase.userDetails.userId, oldDatabase.userDetails.firstName, oldDatabase.userDetails.lastName, oldDatabase.userAge.userAge 
    FROM oldDatabase.userDetails 
    INNER JOIN oldDatabase.userAge 
    where oldDatabase.userDetails.userId = oldDatabase.userAge.userId;
create table if not exists newDatabase.newTable as SELECT oldDatabase.userDetails.userId, oldDatabase.userDetails.firstName, oldDatabase.userDetails.lastName, oldDatabase.userAge.userAge 
    FROM oldDatabase.userDetails 
    INNER JOIN oldDatabase.userAge 
    where oldDatabase.userDetails.userId = oldDatabase.userAge.userId;



-- DROP TABLES
DROP TABLE newDatabase.newTable;
DROP TABLE oldDatabase.newTable;
DROP TABLE oldDatabase.allUserDetails;
DROP TABLE oldDatabase.userAge;
DROP TABLE oldDatabase.userDetails;
DROP TABLE oldDatabase.userInformation;
DROP TABLE newDatabase.userInformation;
-- DROP TABLES END