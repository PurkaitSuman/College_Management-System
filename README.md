# College_Management-System
College_Management System using tkinter

A Project Report

in partial fulfillment for the award of the degree of 

B.Tech


under

Engineers Study Centre


 
Submitted by

Suman Purkait

Netaji Subhash Engineering College

Acknowledgement


I take this opportunity to express my deep gratitude and sincerest thank to my project mentor, Prity Dwivedi madam for giving most valuable suggestion, helpful guidance and encouragement in the execution of this project work.

I will like to give a special mention to my group members- Suprotim Datta, Subhashis Dutta and Sudhyabrata Guha. Last but not the least I am grateful to all the faculty members of Engineers Study Centre for their support.


College Management System –An overview
The task is to create a Database-driven College Management System in Python that will store the information in the MySQL Database.
For creating the College Management System in Python that uses MySQL database, we need to connect Python with MySQL.
For making a connection we need to install mysqlconnector which can be done by writing the following command in the command prompt on Windows.
pip install mysqlconnector
Now after successful installation of mysqlconnector we can connect MySQL with Python which can be done by writing the following code :-

import mysql.connector
 
 
con = mysql.connector.connect(
    host="localhost", user="root", password="password", database="sd"


Python offers multiple options for developing GUI (Graphical User Interface). 
We have used tkinter in our project. Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
To create a tkinter app:
1.	Importing the module – tkinter
2.	Create the main window (container)
3.	Add any number of widgets to the main window
4.	Apply the event Trigger on the widge.
Importing tkinter is same as importing any other module in the Python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.
import tkinter

 project mainly focuses on building a simple database driven management system with the primary aim of opening the home page – consisting of buttons connecting to environments created to perform specific tasks.		

Now before we dive straight into our project – a brief introduction of   my group members-

 

                       


The database is created with the help of XAMPP Control Panel by activating APACHE & MYSQL ports. Tables are created in the phpMyAdmin portal according to our requirement.

 

The code is implemented in Python and run in a suitable Integrated Development Environment (IDE)- Visual Studio or Sublime Text.

 

 The remaining details are mentioned later.

Scope of the Project- College Management System using Python

•	Install mysql using ‘pip’ command through the Command Prompt and import it through a code .
•	Install tkinter – the most commonly used method for developing the GUI(Graphical User Interface)
•	Using concepts of database management system with the help of SQL in our code for proper connectivity of each and every page of our project.
•	Using the programming language of Python to develop, design & implement the different features in our database driven – College Management System.







Now we will describe briefly the various features in our Project through the help of attached screenshots.


 


FIGURE-THE HOME PAGE

Description:-  The Home page consists of 4 buttons –
1.	Student Login 
2.	Administrator Login
3.	Professor Login
4.	Register

The heading consists of   the   message
 – “Welcome to NSEC College”.
1.STUDENT LOGIN

 

FIGURE – STUDENT LOGIN

Description:- Here, the students can login themselves after registering themselves with a specific mail id and password (from the  registered database).
 
FIGURE- REGISTRATION DATABASE


Register New Account-   takes us to the registration portal, where a student registers himself/herself by filling the details.

 


FIGURE-REGISTRATION PAGE
After a student logins himself/herself it takes him/her to this page below-

 

FIGURE-STUDENT DETAILS

The buttons created takes the student to view the personal details & academic   details -   CA marks, Lab Marks, Fees details, Library & attendance details and Placement details.

 

FIGURE-VIEW STUDENT DETAILS


 


FIGURE- VIEW CA MARKS 
 

FIGURE-VIEW LAB MARKS

 

FIGURE-VIEW FEES DETAILS


 
FIGURE-VIEW ATTENDANCE

 

FIGURE-VIEW PLACEMENT DETAILS
 

FIGURE-VIEW LIBRARY DETAILS


2.ADMINSTRATOR LOGIN

 

FIGURE-ADMINISTRATOR LOGIN

Apart from creating a student’s login portal we have also added the administrator login portal- that lets the college admin manage things in a suitable manner. We have kept a unique Email ID –nsec@ac.in.








After the admin logs in himself/  herself , it takes him to the main page-

 

FIGURE-ADMIN MAIN PAGE

The buttons provided takes the admin to the individual profiles or the system and lets the admin to do required changes.


 

 
 
FIGURE- EDIT STUDENT DETAILS

The admin can edit the STUDENT DETAILS with the help of the 4 buttons- ADD, UPDATE, DELETE & CLEAR each of them having the function to perform it’s specific task of adding, updating ,deleting or clearing data related with the student’s details.
The Search button allows us to search details in the database.
The Search By option allows us to search through the database by the specific details.
The Show All button shows each and every detail in the database

The admin also have access to edit and view the professor’s details- only the name in the system. However, he will not have access to edit the CA Marks, Lab Marks and Attendance details which the professor will have.
 
FIGURE-EDIT PROFESSOR’S DETAILS

The admin can also edit the Fees, Placement & Library details.
 

	FIGURE-EDIT FEES DETAILS

  

	FIGURE-EDIT LIBRARY & PLACEMENT DETAILS


3.PROFESSOR’S LOGIN

The professor’s login system allows the professor to login using details from the registration database.
 

FIGURE-PROFESSOR’S LOGIN

After logging in, it takes the professor straight to the main page where the buttons provided takes him to the desired page, where he can view/edit details.

 
FIGURE-PROFESSOR’S MAIN PAGE
The main page lets the professor to edit the continuous assessment (CA) marks, the laboratory marks and allows him to record attendance.
 

FIGURE-ADD CA MARKS
 

FIGURE-ADD LAB MARKS
 

FIGURE-TAKE ATTENDANCE


CONCLUSION
Hereby, I conclude my project- “COLLEGE MANAGEMENT SYSTEM WITH PYTHON & MYSQL”.





 

