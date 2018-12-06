import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import datetime
import io

from helpers import analyze, transcribe_file, entities_text

# Configure application
app = Flask(__name__)


UPLOAD_FOLDER = '' # Set upload folder to current directory
ALLOWED_EXTENSIONS = set(['wav', 'txt']) # Set allowed extansions

# Ensure templates are auto-reloaded
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        pass


@app.route("/record", methods=['GET', 'POST'])
def record():
    if request.method == "GET":
        return render_template("record.html")
    else:
        pass


@app.route("/analyze", methods=['POST'])
def trans():
    if request.method == 'POST':
        # Get text from website
        text = request.data

        #Analyze the decoded data from the website
        tmp = analyze(text.decode("utf-8"))
        entity = entities_text(text.decode("utf-8"))
        # Send response to website
        return 'sent: %f mag: %f' % (tmp[0], tmp[1])
        print(entity)


@app.route("/file_trans", methods=['GET', 'POST'])
def file_trans():
    if request.method == 'POST':
        # Check if file was actually submitted
        if 'file' not in request.files:
            print('no file')
            flash('No file part')
            return redirect(request.url)

        # Get submitted file from website
        file = request.files['file']

        # Make sure filename is secure
        # Save file to a temporary location

        # Save file to a temporary location
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        full_text = '' # Container for text

        # Handle text files
        tmp = filename.split('.')
        if tmp[1] == 'txt':
            # Open the file and read in contents
            with open(filename, 'r') as f:
                text = f.readlines()

            # Combine the lines to single string
            for item in text:
                full_text += item

        # Handle audio files
        else:
            # Get the transcribed text from the Speech-to-Text API
            full_text = transcribe_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Delete temporarily saved file
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Return the
        return full_text

    # Render template if request is GET
    return render_template('file_transcribe.html')


# Checks if file format is valid, from Flask documentation
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def errorhandler(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return render_template('error.html', title='HTTP Exception', text='You encountered an HTTP Exception, try again')


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
