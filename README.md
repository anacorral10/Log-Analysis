# Log Analysis Project - Udacity Full Stack Web Developer Nanodegree

## Overview 

For this project, my task was to create a reporting tool that prints out reports(in plain text) based on the data in the given database. This reporting tool is a Python program using the psycopg2 module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Set Up

1. To run the program, you'll need database software (provided by a Linux virtual machine) and the data to analyze. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser. You can download Vagrant and VirtualBox to install and manage your virtual machine. 

2. VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

3. Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com.](https://www.vagrantup.com/downloads.html) Install the version for your operating system.

4. From your terminal, inside the vagrant subdirectory, run the command ``vagrant up``. This will cause Vagrant to download the Linux operating system and install it. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run  and ``vagrant ssh`` to login.

5. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.

6. Load the database using ``psql -d news -f newsdata.sql``.

7. Connect to the database using ``psql -d news``.

8. Create the Views given below. Then exit ``psql``.

9. Now execute the Python file - ``python logs_analysis.py``. 

## IMPORTANT - Create the Following Views for Question 2 and Question 3

### Views for Question 2 

```SQL
CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```

```SQL
CREATE VIEW article_views AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
```
### Views for Question 3

```SQL
CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;
```

```SQL
CREATE VIEW errorlogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
```
