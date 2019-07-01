import json
import contxtmgr
import main

# this is an API: application programming interface
# this keeps the code simpler and understandable
# makes this return all the values that are asked by the user for 
def create_table_database():
    with contxtmgr.DatabaseManager('students.db') as connector:
        cursor = connector.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS mystudent(NAME text, CLASS text, SECTION text, ROLL integer primary key, SCHOOL text, CITY text)")

def add_to_sql(name, std, section, roll, school, city):
    with contxtmgr.DatabaseManager('students.db') as connector:
        cursor = connector.cursor()
        cursor.execute("INSERT INTO mystudent VALUES(?, ?, ?, ?, ?, ?)", (name, std, section, roll, school, city))


def get_feedback():
    print('Your feedback is valuable to us.\nGive us feedback on what you liked or disliked about us. ')
    user_name = input('What do we call you? : ')
    message = input('How can we improve your service? : ')
    
    foo = {
        'user name': user_name,
        'message': message
    }

    with contxtmgr.MyOpen('feedback.json', 'r') as file:
        text = json.load(file)      # text is the complete list

        
    text.append(foo) 

    with contxtmgr.MyOpen('feedback.json', 'w') as another_file:
        json.dump(text, another_file, indent = 8)

    print('Your valuable comments have been added.\nThank You so much.')


def update_sql(text, exact):
    with contxtmgr.DatabaseManager('students.db') as connector:
        cursor = connector.cursor()
        if text == 'name':
            cursor.execute("UPDATE mystudent SET NAME = ?", (exact,))
        elif text == 'class':
            cursor.execute("UPDATE mystudent SET CLASS = ?", (exact,))
        elif text == 'section':
            cursor.execute("UPDATE mystudent SET SECTION = ?", (exact,))
        elif text == 'roll':
            cursor.execute("UPDATE mystudent SET ROLL = ?", (exact,))
        elif text == 'school':
            cursor.execute("UPDATE mystudent SET SCHOOL = ?", (exact,))
        elif text == 'city':
            cursor.execute("UPDATE mystudent SET CITY = ?", (exact,))
        else:
            print('Oops! Such data does not exist in our database.\nPlease, try again.')
            main.update_database()


def show_from_sql(msg_upper, msg_title):
    with contxtmgr.DatabaseManager('students.db') as connector:
        cursor = connector.cursor()
        if msg_upper == 'NAME':
            cursor.execute("SELECT * FROM mystudent WHERE NAME = ?", (msg_title,))
        elif msg_upper == 'CLASS':
            cursor.execute("SELECT * FROM mystudent WHERE CLASS = ?", (msg_title,))
        elif msg_upper == 'SECTION':
            cursor.execute("SELECT * FROM mystudent WHERE SECTION = ?", (msg_title,))
        elif msg_upper == 'ROLL':
            cursor.execute("SELECT * FROM mystudent WHERE ROLL = ?", (msg_title,))
        elif msg_upper == 'SCHOOL':
            cursor.execute("SELECT * FROM mystudent WHERE SCHOOL = ?", (msg_title,))
        elif msg_upper == 'CITY':
            cursor.execute("SELECT * FROM mystudent WHERE CITY = ?", (msg_title,))
        else:
            print('Oops! Such data does not exist in our database.\nPlease, try again.')
            main.show_part_database()
        
        
        my_list = cursor.fetchall()       
        for line in my_list:
            print(line)

      
def del_from_sql(del_what, del_exact):
    with contxtmgr.DatabaseManager('students.db') as connector:
        cursor = connector.cursor()
        if del_what == 'NAME':
            cursor.execute("DELETE FROM mystudent WHERE NAME = ?", (del_exact,))
        elif del_what == 'CLASS':
            cursor.execute("DELETE FROM mystudent WHERE CLASS = ?", (del_exact,))
        elif del_what == 'SECTION':
            cursor.execute("DELETE FROM mystudent WHERE SECTION = ?", (del_exact,))
        elif del_what == 'ROLL':
            cursor.execute("DELETE FROM mystudent WHERE ROLL = ?", (del_exact,))
        elif del_what == 'SCHOOL':
            cursor.execute("DELETE FROM mystudent WHERE SCHOOL = ?", (del_exact,))
        elif del_what == 'CITY':
            cursor.execute("DELETE FROM mystudent WHERE CITY = ?", (del_exact,))
        else:
            print('Oops! Such data does not exist in our database.\nPlease, try again.')
            main.delete_from_database()
            

