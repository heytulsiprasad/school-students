import sqlite3
import database
from contxtmgr import DatabaseManager

# generating a table for students
# column heading are; name, class, section, roll no, branch, city
# here, the user gets a prompt to do the following things
# 'add' | add students to the database
# 'delete' | delete students from the database
# 'find' | find students from databse
# 'update' | update the student details
# 'quit' | exit the program
# prompt when user quits to give some feedback
# prompt user to press none if don't want to give any
# end of code

def menu():
    print('Welcome to Students Database!')
    print('Add | add students to the database\nUpdate | update the student details\nDelete | delete sudents from the database\nFind | find something in the database\nQuit | Close the database')
    
    create_table_database()
    
    while True:
        user_input = input('What do you want to do? : ')
        enter = user_input.lower()

        if enter == 'add':
            add_to_database()
        elif enter == 'update':
            update_database()
        elif enter == 'delete':
            delete_from_database()
        elif enter == 'show' or enter == 'find':        
            while True:
                new_txt = input('Do you want to see anything in particular? (y/n) : ')
                txt = new_txt.lower()
                if txt == 'y':
                    show_part_database()
                    break
                elif txt  == 'n':
                    show_full_database()
                    break
                else:
                    print('Please, enter a valid input')
        elif enter == 'quit':
            quit_database()
            break
        else:
            print('Please, enter a valid input.')
        

# functions to be created are as follows:
# def add_to_database() ask the user what do they want to enter
# def update_database() ask the user to update any values in the database
# def delete_from_database() prompt the user to delete any values from the database
# def find_from_database() to find something from the database  (submerged with show, as show_part_database)
# def show_part_database() to show the user required rows/columns from the database
# def show_full_database() to display the complete database
# def quit_database() to close the program, prompt user to give some feedback before closing


def add_to_database():
    name = input('Enter student name: ')                            # NAME   
    std = input('Enter student class name: ')                       # CLASS
    section = input('Enter the section student is in: ')            # SECTION
    roll = input('Enter the roll no of student: ')                  # ROLL
    school = input('Enter the school name: ')                       # SCHOOL
    city = input('Enter the name of your city: ')                   # CITY

    database.add_to_sql(name, std, section, roll, school, city)
    print('Your entry was successfully added')


def update_database():
    what = input('What do you want to update?\nNAME, CLASS, SECTION, ROLL, SCHOOL, CITY: ')
    text = what.lower()
    exact = input('What change do you want to make? ')

    database.update_sql(text, exact)
    print('Your entry was successfully insert into our database')


# def delete_from_database():
#     what = input('What do you want to delete? ')
#     exact = input('What among them do you want to delete? ')
    
def quit_database():
    while True:
        msg = input('Are you sure, you want to quit? (Y/N) ')
        txt = msg.lower()
        if txt == 'n':
            menu()
            break
        elif txt == 'y':
            print('We are going to close...')
            database.get_feedback()
            break
        else:
            print('Please, enter a valid input')
    

def show_full_database():
    with DatabaseManager('students.db') as connector:
        cursor = connector.cursor()
        cursor.execute("SELECT * FROM mystudent")
        my_list = cursor.fetchall()
        for line in my_list:
            print(line)


def show_part_database():
    print('CATEGORIES AVAILABLE: \nNAME, CLASS, SECTION, ROLL, SCHOOL, CITY')
    msg1 = input('What category do you want to see? : ')
    msg_upper = msg1.upper()
    msg2 = input('What exactly are you looking for? : ')
    msg_title = msg2.title()

    database.show_from_sql(msg_upper, msg_title)


def delete_from_database():
    txt1 = input('Which category do you want to delete from? : ')
    txt_upper = txt1.upper()
    txt2 = input('What exactly in that you want to delete? : ')
    txt_title = txt2.title()

    database.del_from_sql(txt_upper, txt_title)
    
    print('Transanction Complete!\nThe found data was successfully deleted.')
    pop = input('Do you want to see the database, now? (y/n) : ')
    while True:
        if pop == 'y':
            show_full_database()
            break
        elif pop == 'n':
            print('Thank you, for using our database. Have a nice day!')
            break
        else:
            print('Please, enter a valid input')

def create_table_database():
    # with DatabaseManager('students.db') as connector:
    #     cursor = connector.cursor()
    #     cursor.execute("CREATE TABLE IF NOT EXISTS mystudent(NAME text, CLASS text, SECTION text, ROLL integer primary key, SCHOOL text, CITY text)")

    connector = sqlite3.connect('students.db')
    cursor = connector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mystudent(NAME text, CLASS text, SECTION text, ROLL integer primary key, SCHOOL text, CITY text)")
    
    connector.commit()
    connector.close()
    
menu()
