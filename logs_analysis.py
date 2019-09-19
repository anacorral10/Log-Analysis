#!/usr/bin/env python
# Logs Analysis Project

# Import postgreSQL library
import psycopg2

DBNAME = "news"

query1 = """SELECT *
            FROM article_views
            LIMIT 3;"""

query2 = """SELECT name, sum(article_views.views) AS views
            FROM article_authors, article_views
            WHERE article_authors.title = article_views.title
            GROUP BY name
            ORDER BY views desc;"""

query3 = """SELECT errorlogs.date, round(100.0*errorcount/logcount,2)
            as percent
            FROM logs, errorlogs
            WHERE logs.date = errorlogs.date
            AND errorcount > logcount/100;"""


def connect(query):
    # Connection to database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Execute an SQL statement on the database
    c.execute(query)
    # Fetch all the results from the current statement.
    results = c.fetchall()
    # Closes the connection
    db.close()
    return results

# Create Views for Question 2 and Question 3 as instructed on the README file.

# Question 1. What are the most popular three articles of all time?


def top_three_articles(query):
    results = connect(query)
    print('\n Displaying the most popular articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

# Question 2. Who are the most popular article authors of all time?


def top_authors(query):
    results = connect(query)
    print('\n Displaying the most popular article authors of all \
    time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

# Question 3. On which days did more than 1% of requests lead to errors?


def error_days(query):
    results = connect(query)
    print('\n Displaying the days when more than 1% of requests \
    lead to errors:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")

# Question 1. What are the most popular three articles of all time?
    # r1 = connect(query1)
    # print('Results from Query 1:')
    # print(r1)
# Question 2. Who are the most popular article authors of all time?
    # r2 = connect(query2)
    # print('Results from Query 2:')
    # print(r2)
# Question 3. On which days did more than 1% of requests lead to errors?
    # r3 = connect(query3)
    # print('Results from Query 3:')
    # print(r3)


# prints results when python executed in terminal
if __name__ == '__main__':
    top_three_articles(query1)
    top_authors(query2)
    error_days(query3)
