#! /usr/bin/env python

import psycopg2

# Connect to database
def connect(sql_request):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results

# Building Query 1 : The most popular three articles of	all	time:
query1 = """SELECT articles.title, COUNT(*) AS num
    FROM articles
    JOIN log
    ON log.path LIKE concat('/article/%', articles.slug)
    GROUP BY articles.title
    ORDER BY num DESC
    LIMIT 3;"""

# Building Query 2 : The most popular article authors of all time:
query2 = """SELECT authors.name, COUNT(*) AS num
    FROM authors
    JOIN articles
    ON authors.id = articles.author
    JOIN log
    ON log.path like concat('/article/%', articles.slug)
    GROUP BY authors.name
    ORDER BY num DESC"""

# Bilding Query 3 : Day	with more than 1% of requests lead to errors:
query3 = """SELECT total.day,
      ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
    FROM (
      SELECT date_trunc('day', time) "day", count(*) AS error_requests
      FROM log
      WHERE status LIKE '404%'
      GROUP BY day
    ) AS errors
    JOIN (
      SELECT date_trunc('day', time) "day", count(*) AS requests
      FROM log
      GROUP BY day
      ) AS total
    ON total.day = errors.day
    WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
    ORDER BY percent DESC;"""

# Run&Print Query 1 : The	most popular three articles	of	all	time:
def get_top_three_articles():
    results = connect(query1)
    # Print the title
    print('\n1. What are the most popular three articles of all time?')
    # Print the results
    count = 1
    for title, num in results:
        print( ' (' + str(count) + ')' + " \"{}\" - {} views".format(title, num))
        count += 1

# Run&Print Query 2 : The most popular article authors of all time:
def get_top_article_authors():
    results = connect(query2)
    # Print the title
    print('\n2. Who are the most popular article authors of all time?')
    # Print the results
    count = 1
    for name, num in results:
        print( ' (' + str(count) + ')' + " {} - {} views".format(name, num))
        count += 1

# Run&Print Query 3 : Day with more than 1% of requests lead to errors:
def get_days_with_errors():
    results = connect(query3)
    # Print the title
    print('\n3. On which days did more than 1% of requests lead to errors?')
    # Print the results
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(" *"+ date + " - " + errors)

print('Please wait to calculate the results...\n')
get_top_three_articles()
get_top_article_authors()
get_days_with_errors()
