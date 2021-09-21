from app import app

app.run()

# error handling functionality required
@app.errorhandler(Exception)          
def basic_error(e):          
    return "an error occured: " + str(e)