import sqlite3

cnn = sqlite3.connect('youtube_manager.db')
cursor = cnn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_vedios():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_vedios(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    cnn.commit()

def update_vedios(video_id,name,time):
    cursor.execute(
    "UPDATE videos SET name = ?, time = ? WHERE id = ?",
    (name, time, video_id)
    )
    cnn.commit()

def delete_vedios(video_id):
    cursor.execute(
    "DELETE FROM videos WHERE id = ?",
    (video_id,)
)

def main():
    while True:
        print("\n YOUTUBE_MANAGER app with db")
        print("1. LIST Videos")
        print("2. ADD videos")
        print("3. UPDATE videos")
        print("4. DELETE videos")
        print("5. EXIT app")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_vedios()
            case '2':
                name =  input("Enter thr video name: ")
                time =  input("Enter thr video time: ")
                add_vedios(name,time)
            case '3':
                video_id= input("Enter video Id to be updated: ")
                name =  input("Enter thr video name: ")
                time =  input("Enter thr video time: ")
                update_vedios(video_id,name,time)
            case '4':
                video_id= input("Enter video Id to be deleted: ")
                delete_vedios(video_id)
            case '5':
                break
            case _:
                print("invalid choice...🦩")
    cnn.close()

if __name__ == "__main__":
    main()