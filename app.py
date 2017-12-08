# import the Flask class from the flask module
from flask import Flask, render_template, flash, request, url_for, redirect
import speech_recognition as sr
from os import system
from flask.ext.mysql import MySQL
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('home.html')  # return a string

@app.route('/project' , methods = ['GET','POST'])
def welcome():


    error = ''
    try:
        if request.method == 'POST':
            request.args.get('key' , 'q')
            parse_query(q)

        return render_template('project.html' , error = error)
    except Exception as e:
        flash(e)
        return render_template('project.html' , error = error)  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

# Record Audio
@app.route('/recordspeech' , methods=['GET','POST'])
def recordspeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        user_speech = r.recognize_google(audio)
        print("You said: " + user_speech)

        # this is for the text to speech portion

        #system('say %s' %(user_speech))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def parse_query(q):
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'acdcacdc2'
    #app.config['MYSQL_DATABASE_DB'] = ''
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'

    
