import base64
import sqlite3

# returns category list for categories navbar
def category_list():
    categories = ['Languages', 'Hardware', 'Software', 'Mathematics', 'Comp Sci', 'Dev Tools', 'Graphics', 'Operating Systems', 'Networking', 'CS History', 'Security']
    return categories

# formats datetime string to remove the time
def format_date(date_string):
    date = date_string[0:11]
    return date

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# creates dict for database entries values
def create_entry_dict():                   
    entry_dict_keys = ['title', 'url', 'body', 'datetime', 'image', 'mimetype', 'user_id', 'username']
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
                title = data[0]
                entry['title'] = title
                continue
            if i == 1:
                link = data[1]
                entry['url'] = link
                continue
            if i == 2:
                text = data[2]
                entry['body'] = text
                continue
            if i == 3:
                user_id = data[3]
                cursor.execute("SELECT username FROM users WHERE id=?", (user_id,))
                row = cursor.fetchone()    
                user = row[0]
                entry['username'] = user
                continue
            if i == 4:
                date = data[4]
                date = format_date(date)
                entry['datetime'] = date
                continue
            if i == 5:
                mimetype = data[5]
                entry['mimetype'] = mimetype
                continue
            if i == 6:
                blob = base64.encodebytes(data[6])
                image = blob.decode('utf-8')
                entry['image'] = image
                image = None
                blob = None

        conn.close()
        return entry
                


