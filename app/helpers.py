import base64
import sqlite3

# returns category list for categories navbar
def category_list():
    categories = ['Languages', 'Hardware', 'Software', 'Mathematics', 'Comp Sci', 'Dev Tools', 'Graphics', 'Operating Systems', 'Networking', 'CS History', 'Security']
    return categories

def format_date(date_string):
    date = date_string[0:11]
    return date

# creates dict for database entries values
def create_entry_dict():                   
    entry_dict_keys = ['id', 'title', 'url', 'body', 'image', 'datetime', 'user_id', 'filename', 'mimetype', 'username']
    entry = {key: None for key in entry_dict_keys}
    return entry

# fills entry dict with data for one library entry
def fill_entry_dict(data):       
                                               
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    entry = create_entry_dict()

    if data is not None:
        for i in range(0, len(data), 1):
            if i == 0:
                id = data[0]
                entry['id'] = id
            if i == 1:
                title = data[1]
                entry['title'] = title
                continue
            if i == 2:
                link = data[2]
                entry['url'] = link
                continue
            if i == 3:
                text = data[3]
                entry['body'] = text
                continue
            if i == 4:
                blob = base64.encodebytes(data[4])
                image = blob.decode('utf-8')
                entry['image'] = image
                image = None
                blob = None
            if i == 5:
                date = data[5]
                date = format_date(date)
                entry['datetime'] = date
                continue
            if i == 6:
                user_id = data[6]
                cursor.execute("SELECT username FROM users WHERE id=?", (user_id,))
                row = cursor.fetchone()   
                if row is not None: 
                    user = row[0]
                    entry['username'] = user
                else:
                    entry['username'] = None
                continue
            if i == 7:
                file = data[7]
                entry['filename'] = file
                continue
            if i == 8:
                mimetype = data[8]
                entry['mimetype'] = mimetype
                continue
                
        conn.close()
        return entry   

def get_default_entries():

    entries = []

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM entries")
    all_entries = cursor.fetchall()

    for item in all_entries:
        data = item
        filled_entry = fill_entry_dict(data)
        entries.append(filled_entry)

    conn.close()

    return entries

