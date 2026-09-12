import pymysql
connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="1Whysoserious?",
        port=3306
    )
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS music_stream")
cursor.execute("USE music_stream")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            song_count INT
        )
    """)

data = [
        ("Chill Vibes", 15),
        ("Workout Mix", 20),
        ("Road Trip", 25)
    ]

cursor.executemany(
        "INSERT INTO playlists (name, song_count) VALUES (%s, %s)",
        data
    )

connection.commit()
print("Playlists inserted successfully")