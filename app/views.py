from app import app
from app import helpers

import sqlite3
from datetime import datetime

from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

@app.route("/macha-default", methods=["GET"])
def default():

    categories = helpers.category_list()
    bool_nosearch = True

    if request.method == "GET":

        message = ""

        return render_template('macha-default.html', bool_nosearch=bool_nosearch, message=message, categories=categories)


@app.route("/macha-login", methods=["GET", "POST"])
def login():

    categories = helpers.category_list() 
    bool_nosearch = True

    if request.method == "POST":

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        if not request.form.get('username') or not request.form.get('password'):
            message = ""
            return render_template("macha-login.html", bool_nosearch=bool_nosearch, categories=categories, message=message)

        pw = request.form.get('password')
        username = request.form.get('username')

        cursor.execute("SELECT pwd_hash FROM users WHERE username=?", [username])
        row = cursor.fetchone()

        if row is not None:
            user_hash = row[0]

# checking password hash against user data
        if row is not None and check_password_hash(user_hash, pw) is True:

            session['user'] = username
            session.modified = True

            conn.close()

            message = "You are now logged in"

            entries = helpers.get_default_entries()
            categories = helpers.category_list()

            return render_template("macha-browse.html", bool_nosearch=bool_nosearch, message=message, entries=entries, categories=categories)

        else:
            message = "Login not successful - try again!"
            bool_nosearch = True

            return render_template("macha-login.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

    else:
        message = ""

        bool_nosearch = True

        return render_template("macha-login.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

@app.route("/macha-logout", methods=["POST"])
def logout():

    categories = helpers.category_list()
    bool_nosearch = True
    entries = helpers.get_default_entries()

    if request.method == "POST":

# removing user session from flask session variable
        session.pop('user', None)

        message = "You are logged out"
        return render_template('macha-browse.html', bool_nosearch=bool_nosearch, entries=entries, message=message, categories=categories)
    
    
@app.route("/macha-register", methods=["GET", "POST"])
def register():

    categories = helpers.category_list()
    bool_nosearch = True

    code_list = ['TEST', '#5966', '#8888', '#6582', '#5880', '#2475', '#6666', '#0189', '#7056', '#4269', '#6558', '#1873', '#1671', '#0001']

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS codes (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
                            unique_code TEXT NOT NULL);""")
    conn.commit()

    test = 'TEST'
    test = str(test)

    cursor.execute("SELECT id FROM codes WHERE unique_code=?", [test])
    row = cursor.fetchone()

    # row is None for some reason even tho 'TEST' exists in the db

    if row is None:
        for item in code_list:
            cursor.execute(f"INSERT INTO codes (unique_code) VALUES (?)", (item,))
            conn.commit()

    if request.method == "POST":

        if not request.form.get('createUsername') or not request.form.get('createPassword') or not request.form.get('uniqueCode'):
            message = "Username & password fields must not be blank"
            return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

        user_code = request.form.get('uniqueCode')
        user_code = str(user_code)

        cursor.execute("SELECT id FROM codes WHERE unique_code=?", [user_code])
        db_code = cursor.fetchone()

        if db_code is None:
            message = "Unique code is invalid - please try again"
            return render_template('macha-register.html', bool_nosearch=bool_nosearch, message=message, categories=categories)
        else:
            cursor.execute("DELETE FROM codes WHERE unique_code=?", [user_code])
            conn.commit()

        username = request.form.get('createUsername')

        if (len(username) < 3 or len(username) > 15):
            message = "Username should be 3 - 15 characters"
            return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

        pw = request.form.get('createPassword')

        if (len(pw) < 8 or len(pw) > 30):
            message = "Password should be 8 - 30 characters"
            return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

        for char in username:
            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9'):
                continue
            else:
                message = "Username should contain only letters or digits"
                return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

        cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
                            username TEXT NOT NULL, pwd_hash TEXT NOT NULL);""")
        conn.commit()

        cursor.execute("SELECT id FROM users WHERE username=?", [username])
        row = cursor.fetchone()

        if row is not None:
            message = "Username already exists - please try again!"
            return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

# hashing password with werkzeug module and storing in database
        hash = generate_password_hash(pw)

        if (pw != request.form.get('confirmPassword')):
            message = "Password and Password Confirmation do not match"
            return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)
        else:
            conn.execute(f"INSERT INTO users (username, pwd_hash) VALUES (?, ?)", (username, hash))
            conn.commit()
            conn.close()

        message = "Registration successful - please log in to browse"
        return render_template("macha-login.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

    else:
        message = ""
        return render_template("macha-register.html", bool_nosearch=bool_nosearch, message=message, categories=categories)


@app.route("/macha-entry", methods=["GET", "POST"])
def entry():

    categories = helpers.category_list()
    bool_nosearch = True

    if request.method == "POST":

        if not session.get('user'):
            message = "Please log in to contribute"
            return render_template("macha-login.html", bool_nosearch=bool_nosearch, categories=categories, message=message)

        if not request.form.get('entry-title') or not request.form.get('entry-link') or not request.form.get('entry-body'):
            message = "All fields should be completed"
            return render_template("macha-entry.html", bool_nosearch=bool_nosearch, categories=categories, message=message)

        title = request.form.get('entry-title')
        url = request.form.get('entry-link')
        desc = request.form.get('entry-body')
        username = session['user']

        if len(title) > 100:
            message = "Character limit exceeded for title - max 100 characters"
            return render_template('macha-entry.html', bool_nosearch=bool_nosearch, message=message, categories=categories)

        if len(url) > 300:
            message = "Character limit exceeded for URL - max 300 characters"
            return render_template('macha-entry.html', bool_nosearch=bool_nosearch, message=message, categories=categories)
        
        if len(desc) > 300:
            message = "Character limit exceeded for description - max 300 characters"
            return render_template('macha-entry.html', bool_nosearch=bool_nosearch, message=message, categories=categories)

# currently no character limits on text inputs - this is TODO
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE username=?", [username])
        row = cursor.fetchone()
        users_table_id = row[0]

        datetime_now = datetime.now()
        datetime_now = str(datetime_now)

# storing image file in database as blob data, without interim server upload
        if request.files:
            image = request.files['entry-file']
            img_filename = secure_filename(image.filename)
            img_file = image.read()
            img_mimetype = image.mimetype

        else:
            img_file = None

        cursor.execute("""CREATE TABLE IF NOT EXISTS entries (id INTEGER CONSTRAINT "UNIQUE" PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
                            title TEXT, url TEXT, body TEXT, image BLOB, datetime STRING NOT NULL, user_id INTEGER NOT NULL,
                            filename STRING, mimetype STRING);""")
        conn.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
                        category STRING NOT NULL, entry_id STRING REFERENCES entries (id) NOT NULL);""")
        conn.commit()
                
        cursor.execute(f"INSERT INTO entries (title, url, body, image, filename, mimetype, datetime, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                        (title, url, desc, img_file, img_filename, img_mimetype, datetime_now, users_table_id))
        conn.commit()

        cursor.execute("SELECT id FROM entries WHERE datetime=?", (datetime_now,))
        row = cursor.fetchone()
        entries_table_id = row[0]

        if not request.form.getlist('options'): 
            message = "Category field is required"
            return render_template("macha-entry.html", bool_nosearch=bool_nosearch, message=message, categories=categories)

        category_selected = request.form.getlist('options')

        for item in category_selected:
            cursor.execute(f"INSERT INTO categories (entry_id, category) VALUES (?, ?)", (entries_table_id, item))
            conn.commit()

        entries = helpers.get_default_entries()
        
        message = "Upload Successful - hooray!"

        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

    else:

        if not session.get('user'):

            entries = helpers.get_default_entries()

            message = "Please log in to contribute"

            return render_template("macha-login.html", bool_nosearch=bool_nosearch, message=message, categories=categories)
        else:

            message = ""

            return render_template("macha-entry.html", bool_nosearch=bool_nosearch, message=message, categories=categories)


@app.route("/", methods=["GET", "POST"])
def browse():

    categories = helpers.category_list()
    entries = []
    bool_nosearch = True

    if request.method == "POST":

        if not session.get('user'):
            entries = helpers.get_default_entries()
            message = "Please log in to browse by category"
            return render_template("macha-browse.html", bool_nosearch=bool_nosearch, entries=entries, categories=categories, message=message)
 
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        entry_category = request.form.get('category')

        cursor.execute("SELECT entry_id FROM categories WHERE category=?", (entry_category,))
        entry_ids_by_category = cursor.fetchall()

        if len(entry_ids_by_category) < 1:
            return render_template('macha-browse.html', bool_nosearch=bool_nosearch, categories=categories, entries=entries)

        for item in entry_ids_by_category:

            entry_id = item[0]      
            cursor.execute("SELECT * FROM entries WHERE id=?", (entry_id,))
            data = cursor.fetchone()

# blob image data decoded in helpers.py
            if data is not None:
                filled_entry = helpers.fill_entry_dict(data)
                entries.append(filled_entry)

        conn.close()

        message = ""

        bool_nosearch = False
                   
        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

    else:

        entries = helpers.get_default_entries()

        message = ""
                                    
        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

@app.route("/macha-search", methods=["GET", "POST"])
def search():

    categories = helpers.category_list()
    bool_nosearch = True
    
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    if request.method == "POST":

        if not request.form.get('text-search'):
            return redirect("/")
                               
        if not session.get('user'):

            message = "Please log in to search the library"
            return render_template("macha-login.html", bool_nosearch=bool_nosearch, categories=categories, message=message)

# searching database using SQL like query - this functionality should be improved upon
        search = request.form.get('text-search')
        search = '%' + search + '%'

        entry_id_list = []

    # at the moment this turns up duplicate items - need to improve the code

        cursor.execute("SELECT id FROM entries WHERE title LIKE (?)", (search,))
        ids = cursor.fetchall()
        entry_id_list.append(ids)

        cursor.execute("SELECT id FROM entries WHERE body LIKE (?)", (search,))
        ids = cursor.fetchall()
        entry_id_list.append(ids)

        cursor.execute("SELECT id FROM entries WHERE url LIKE (?)", (search,))
        ids = cursor.fetchall()
        entry_id_list.append(ids)

        entries = []

        if len(entry_id_list) >= 1:
            for item in entry_id_list:
                for i in range(0, len(item), 1):

                    x = item[i][0]

                    cursor.execute("SELECT * FROM entries WHERE id=?", (x,))
                    data = cursor.fetchone()

                    filled_entry = helpers.fill_entry_dict(data)
                    entries.append(filled_entry)
        else:

            entries = helpers.get_default_entries()
            message = "No search results found - try again!"

            return render_template("macha-browse.html", bool_nosearch=bool_nosearch, entries=entries, categories=categories, message=message)

        conn.close()

        bool_nosearch = False
        message = ""
                        
        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

    else:

        entries = helpers.get_default_entries()

        message = "No search results found"

        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)


@app.route("/delete-entry", methods=["GET", "POST"])
def delete():

    categories = helpers.category_list()
    bool_nosearch = True
    
    entries = helpers.get_default_entries()

    if request.method == "POST":

        if not request.form.get('urlInput'):
            message = ""
            return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

        url = request.form.get('urlInput')

        print("this is the url data" + url)

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM entries WHERE url=?", (url,))
        row = cursor.fetchone()

        if row == None:
            message = "Resource deleted - select category to browse"
            return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

        entry_id = row[0]

        cursor.execute("DELETE FROM entries WHERE id=?", (entry_id,))
        cursor.execute("DELETE FROM categories WHERE entry_id=?", (entry_id,))
        conn.commit()
        conn.close()

        message = "Resource deleted - select category to browse"

        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)

    else:
        
        message = ""

        return render_template("macha-browse.html", bool_nosearch=bool_nosearch, categories=categories, entries=entries, message=message)