import re
import sqlite3
import csv

class db_operations():

    # create the connectionn & cursor object
    def __init__ (self, conn_path):

        #if the conn_path (.db) does not exist, it will be created in this step
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        print("Connection made.")

    # Create songs table 
    def create_new_table(self):

        query = '''
        CREATE TABLE songs (
            ID TEXT PRIMARY KEY NOT NULL,
            song_name VARCHAR(50) NOT NULL,
            artist_name VARCHAR(50) NOT NULL,
            album VARCHAR(50) NOT NULL,
            genre VARCHAR(50) NOT NULL,
            song_len_seconds REAL NOT NULL
        );
        '''

        self.cursor.execute(query)
        self.connection.commit()
        
        print("Created table.")

    # Ingest data from the .csv
    def ingest_songs(self, csv_file):

        # Insert query
        query = '''
                INSERT INTO songs VALUES (?,?,?,?,?,?);
                '''

        # Open the songs.csv file
        with open(csv_file, mode = 'r') as file:

            csvFile = csv.reader(file)

            #skip the header
            next(csvFile)

            for line in csvFile: # Iterates through each row in the csv file
                self.cursor.execute(query,line)
            
        # Batch commit to playlist db
        self.connection.commit()

        print("Ingested your songs!")

    # Find Songs by artist
    def find_songs_artist(self):

        # Print all artists currently in the songs table
        artist_query = '''
        SELECT DISTINCT artist_name
        FROM songs;
        '''

        # Execute the select statement
        artist_results = self.cursor.execute(artist_query)

        # Print out results to the user
        artist_list = []
        for row in artist_results:
            artist_list.append(row[0])

        print("Please select an artist to search on:")
        for i in range(len(artist_list)):
            print(f"{i+1}. {artist_list[i]}")

        user_choice = input("Choice: ")

        # Query on artist name
        artist_query = '''
        SELECT song_name
        FROM songs 
        WHERE artist_name = '%s'
        '''

        # Execute the select statement
        song_results = self.cursor.execute(artist_query % artist_list[int(user_choice)-1])

        # Print the song results to the user
        for song in song_results:
            print(song[0])

    
    # Find Songs by Genre -- copy func above but change artist to genre
    def find_songs_genre(self):
        genre_query = 'SELECT DISTINCT genre FROM songs;'
        genre_results = self.cursor.execute(genre_query)
        genre_list = [row[0] for row in genre_results]

        print("Please select a genre to search on:")
        for i, genre in enumerate(genre_list, start=1):
            print(f"{i}. {genre}")

        user_choice = int(input("Choice: ")) - 1
        genre_query = 'SELECT song_name FROM songs WHERE genre = ?'
        song_results = self.cursor.execute(genre_query, (genre_list[user_choice],))
        for song in song_results:
            print(song[0])

    # Show all songs
    def show_songs(self):

        # SELECT * from our db to get all current songs
        query = '''
        SELECT song_name, artist_name, album, genre, song_len_seconds
        FROM songs;
        '''

        results = self.cursor.execute(query)

        # print out the playlist in a better way
        headers = ["Song Name", "Artist Name", "Album", "Genre", "Song Length (sec)"]

        # print headers with fixed column widths
        print(f"{headers[0]:<30} {headers[1]:<20} {headers[2]:<30} {headers[3]:<20} {headers[4]:<10}")

        # print separator
        print("-"*125)

        # iterate through the results
        for row in results:
            song_name, artist_name, album, genre, song_len = row
            print(f"{song_name:<30} {artist_name:<20} {album:<30} {genre:<20} {song_len:<10}")
            
    # Delete songs 
    def delete_song(self):
        self.show_songs()
        song_name = input("Enter song name to delete: ")
        artist_name = input("Enter artist name: ")
        query = 'DELETE FROM songs WHERE song_name = ? AND artist_name = ?'
        self.cursor.execute(query, (song_name, artist_name))
        self.connection.commit()
        print("Song deleted.")
    # Update songs
    def update_song(self):
        self.show_songs()
        song_name = input("Enter song name to update: ")
        artist_name = input("Enter artist name: ")
        column = input("Enter column to update (song_name, artist_name, album, genre, song_len_seconds): ")
        new_value = input(f"Enter new value for {column}: ")
        query = f'UPDATE songs SET {column} = ? WHERE song_name = ? AND artist_name = ?'
        self.cursor.execute(query, (new_value, song_name, artist_name))
        self.connection.commit()
        print("Song updated.")

    # Show stats for playlist
    def get_stats(self):
        total_length_query = 'SELECT SUM(song_len_seconds) FROM songs;'
        song_count_query = 'SELECT COUNT(*) FROM songs;'
        artist_count_query = 'SELECT artist_name, COUNT(*) FROM songs GROUP BY artist_name;'
        total_length = self.cursor.execute(total_length_query).fetchone()[0] / 60
        song_count = self.cursor.execute(song_count_query).fetchone()[0]
        artist_counts = self.cursor.execute(artist_count_query).fetchall()
        print(f"Total playlist length: {total_length:.2f} minutes")
        print(f"Total number of songs: {song_count}")
        for artist, count in artist_counts:
            print(f"{artist}: {count} song(s)")

    # Add new song
    def add_new_songs(self, csv_file):
        query = 'INSERT INTO songs VALUES (?, ?, ?, ?, ?, ?)'
    
        with open(csv_file, mode='r') as file:
        csvFile = csv.reader(file)
        next(csvFile, None)  # Skip header row

        for line in csvFile:
            if len(line) == 6: 
                song_id = line[0]
                
                # Check if the song ID already exists in the database
                self.cursor.execute("SELECT 1 FROM songs WHERE ID = ?", (song_id,))
                if self.cursor.fetchone():
                    continue  # Skip this song if the ID already exists

                # Insert the song if it's unique
                self.cursor.execute(query, line)
                
    # Commit the changes to save the new songs
    self.connection.commit()
