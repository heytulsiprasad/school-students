import database

print("<-------------Welcome to the Movie Manager---------------->\n")
USER_CHOICE = """
Enter 'a' to add a movie;
'f' to find a movie;
'w' to mark the movie as watched;
's' to show all the movies in the database;
'd' to Delete a movie;
and 'q' to Quit the Program:  
"""


def menu():
    database.create_movies_table()
    user_input = input(USER_CHOICE)
    if user_input != 'q':
        while user_input != 'q':
            if user_input == 'a':
                prompt_add_movie()
            elif user_input == 'w':
                prompt_mark_as_watched()
            elif user_input == 's':
                prompt_show_movies()
            elif user_input == 'd':
                prompt_delete_movie()
            elif user_input == 'f':
                prompt_find_movie()
            else:
                print("Invalid Input. Please Try Again.!\n")
            user_input = input(USER_CHOICE)
    else:
        print("Quitting the Movie Manager Application")


def prompt_add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie's director's name: ")
    year = input("Enter the year of release: ")
    location = input("Enter the Shelf number and Row name: ")

    database.add_movie(name, director, year, location)


def prompt_mark_as_watched():
    name = input("Enter the movie name which you have seen: ")
    database.mark_as_watched(name)


def prompt_show_movies():
    database.show_movies()


def prompt_delete_movie():
    name = input("Enter the movie name which you have seen: ")
    database.delete_movie(name)


def prompt_find_movie():
    attribute = input("Enter the attribute by which you wanna find the movies: ")
    value = input("Enter the value of the above attribute: ")
    database.find_movie(attribute, value)


menu()
