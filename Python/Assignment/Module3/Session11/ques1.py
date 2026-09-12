import pymysql

try:
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="1Whysoserious?",
        port=3306
    )
    print("Connection successful")
except Exception as e:
    print("Connection failed:", e)
finally:
    if 'connection' in locals() and connection.open:
        connection.close()