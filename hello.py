from flask import Flask , render_template

#create a flask instance
app = Flask(__name__)

#create route decorator
@app.route("/")

#def index ():
    #return "<h>Hello world</h1>"

def index():
    first_name ="John"
    stuff="this text is <strong>bold</strong> not so??"
    food=["mowongo","lumode",'matooke']
    return render_template("index.html",
    first_name=first_name,
    stuff=stuff,
   food=food )

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

#create  custom error page
#invlid page error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
#internal server error
@app.errorhandler(500)
def Internal_Server_error(e):
    return render_template("500.html"),500
