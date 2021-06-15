import sqlite3
from sqlite3 import Error
import sql_queries as q


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("D:\\My Workplace\Code\Python\Education\SQL\sm_app.sqlite")


# execute_query(connection, q.create_users_table)
# execute_query(connection, q.create_posts_table)
# execute_query(connection, q.create_comments_table)
# execute_query(connection, q.create_likes_table)
# execute_query(connection, q.create_users)
# execute_query(connection, q.create_posts)
# execute_query(connection, q.create_comments)
# execute_query(connection, q.create_likes)

# users = execute_read_query(connection, q.select_users)
# print(*users, sep='\n')

# posts = execute_read_query(connection, q.select_posts)
# print(*posts, sep='\n')

# users_posts = execute_read_query(connection, q.select_users_posts)
# print(*users_posts, sep='\n')

# posts_comments_users = execute_read_query(connection, q.select_posts_comments_users)
# print(*posts_comments_users, sep='\n')

# cursor = connection.cursor()
# cursor.execute(q.select_posts_comments_users)
# cursor.fetchall()
#
# column_names = [description[0] for description in cursor.description]
# print(column_names)

# post_likes = execute_read_query(connection, q.select_post_likes)
# print(*post_likes, sep='\n')

post_description = execute_read_query(connection, q.select_post_description)
print(*post_description, sep='\n')

execute_query(connection, q.update_post_description)

post_description = execute_read_query(connection, q.select_post_description)
print(*post_description, sep='\n')
