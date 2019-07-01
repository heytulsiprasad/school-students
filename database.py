import sqlite3


def create_movies_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS movies(name text primary key,director text,year integer,location text, watched integer)")
    connection.commit()
    connection.close()


def add_movie(name, director, year, location):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT OR IGNORE INTO movies VALUES(?,?,?,?,0)", (name, director, year, location))
    connection.commit()
    connection.close()


def get_all_movies():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = [{'name': row[0], 'director': row[1], 'year': row[2], 'location': row[3], 'watched': row[4]} for row in
              cursor.fetchall()]
    connection.close()
    return movies


def show_movies():
    movies = get_all_movies()
    for movie in movies:
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Year of Release: {movie['year']}")
        print(f"Location: {movie['location']}")
        movie['watched'] = 'Yes' if movie['watched'] else 'No'
        print(f"Watched: {movie['watched']}\n")


def mark_as_watched(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE movies SET watched=1 WHERE name=?", (name,))
    connection.commit()
    connection.close()


def delete_movie(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE name=?", (name,))
    connection.commit()
    connection.close()


def find_movie(attribute, value):
    movies = get_all_movies()
    for movie in movies:
        try:
            if movie[attribute] == value:
                print(f"Name: {movie['name']}")
                print(f"Director: {movie['director']}")
                print(f"Year of Release: {movie['year']}")
                print(f"Location: {movie['location']}")
                movie['watched'] = 'Yes' if movie['watched'] else 'No'
                print(f"Watched: {movie['watched']}\n")
        except KeyError:
            print("\nInvalid Key provided")
