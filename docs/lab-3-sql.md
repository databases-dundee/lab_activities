# Lab 2 - SQL Practice

This lab aims to give you practice in connecting to a simple SQL database and running some simple SQL queries upon it


## What you need to do

This practical work requires you to use MySQL Workbench to access your own MySQL database
(which is hosted by AWS). You can access MySQL Workbench as follows:
- Through the Windows desktop on a QMB Lab PC (type “SQL” into the search bar)
- Through the Windows desktop on a University PC via AppsAnywhere
- By downloading and installing it on your own PC from [this link](dev.mysql.com/downloads/workbench).

Before we start using the database, we need to perform three steps:
1. Initialise your AWS account - you should have recently received an e-mail from AWS asking
you to set up an account - follow the instructions in this e-mail. If you don’t have an e-mail,
check your spam folder, and if it's not in there either, please let us know!
2. Set up a relational database server (RDS) on your AWS account by following the AWS
Learner Lab Database Setup Instructions document on MyDundee. Make a note of the
database host name and your password (you'll need these in the next step). Note that
not all screens will look *exactly* the same as the examples in this document, but the
functional parts are the same.
3. Set up the database on your RDS using MySQL WorkBench - by the end of Part 2 above, you
should have connected successfully to the database server. Now download the file
SQLTutorialCreateTables.SQL from MyDundee. Click File \ Open SQL Script and select the
SQLTutorialCreateTables.SQL that you downloaded. Within the script text, on lines 10, 12
and 14, replace the word YOUR-DATABASE-NAME-HERE with your actual database name.
4. Now run the script by clicking the lightning flash icon on the toolbar to populate your
database (it'll take a bit of time - there are a lot of cities in the world!)

## Let's look at the SQL!
There are a few features to note:
- The SQL is a simple (but quite big) text file
- An SQL database can be backed up to an SQL text file if required (it is recommended that
you do this at the end of each session); running the SQL file then recreates the database
- The attributes in the `CREATE TABLE` statements have appropriate data types, and note the additional
integrity features that can be added e.g. `NOT NULL`, `PRIMARY KEY` and `FOREIGN KEY` declarations
- The `set autocommit = 0` and `COMMIT` that sandwich the `INSERT` statements mean that either **all** 
these statements are executed, or **none** of them are - this is the concept of transactions that we'll
cover in Week 4!

## Anything else?
