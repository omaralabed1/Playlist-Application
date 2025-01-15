'''
ABOUT: Main operations of the app will be conducted in this file. This is where
the main menu will be shown, the user will select different menu items and 
when the user selects a menu item we will be calling methods from the db_operations class 
for sql statements.
'''

from db_operations import db_operations

#global variable
db_ops = db_operations("playlist.db")

def startApp():
    print("Welcome to your playlist! ")

    # Create the songs table 
    #db_ops.create_new_table()

    # Ingest data from the songs.csv file
    #db_ops.ingest_songs('songs.csv')

def mainMenu():
    
    user_choice = input('''
    SELECT FROM THE FOLLOWING MENU:
    1. Find songs by artist
    2. Find songs by genre
    3. Show all songs
    4. Add new songs
    5. Delete a song
    6. Update song information
    7. Get playlist stats
    ''')
    
    if user_choice == '1':
        db_ops.find_songs_artist()
    elif user_choice == '2':
        db_ops.find_songs_genre()
    elif user_choice == '3':
        db_ops.show_songs()
    elif user_choice == '4':
        db_ops.add_new_songs('new_songs.csv')
    elif user_choice == '5':
        db_ops.delete_song()
    elif user_choice == '6':
        db_ops.update_song()
    elif user_choice == '7':
        db_ops.get_stats()
    else:
        print("Invalid choice, please select again.")

 

def main():
    startApp()
    mainMenu()
    
if __name__ == '__main__':
    main()
