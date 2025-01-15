# Playlist Application

## Overview
This project is a **Playlist Management App** designed to manage song data, interact with structured files, and perform CRUD (Create, Read, Update, Delete) operations on an SQLite database.

---

## Features
- **Database Management**: 
  - Utilizes an SQLite database (`playlist.db`) to store and manage song and playlist data.
  - Includes functionality for creating, reading, updating, and deleting playlist entries.
- **CSV Integration**: 
  - Imports and exports song data using CSV files (`songs.csv`, `new_songs.csv`).
  - Processes and updates playlists efficiently through automated scripts.
- **Application Logic**: 
  - The `app.py` file provides the core functionality to interact with the playlist data.
- **Error Handling**: 
  - Robust handling of database and file operations to ensure smooth performance.

---

## Technologies Used
- **Python**: For implementing core application logic and data processing.
- **SQLite**: For managing and storing song and playlist data.
- **CSV Files**: For efficient data import/export and playlist management.

---

## Repository Structure
```plaintext
.
├── app.py                # Main application file for playlist management
├── db_operations.py      # Handles database interactions (CRUD operations)
├── db_operations.cpython-311.pyc  # Compiled Python bytecode
├── songs.csv             # Original song data
├── new_songs.csv         # Updated song data for playlist changes
├── playlist.db           # SQLite database storing song and playlist data
├── README.md             # Project documentation
