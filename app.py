# ---------------------------------------------------------------
# This program shows how the webservice for searching google results works
# The webservice uses webpage as webinterface on localhost to have an interaction with webserver
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------
import json
from flask import Flask, request, render_template
import authVerify
import tParser_Post

app = Flask(__name__)
gtoken = "7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE"
qrcodepath = "../static/7UG7ETJ43ORR332TYPNKD7QTPG3X5ZYQPFIVYTJ6B42A7GSGKP4BYYGLZLEKEKWE.png"


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html', qrcodepath=qrcodepath)


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    verifycode = request.form['verifycode']
    if username == 'admin' and password == 'password':
        # supposed that user has already his own QRcode after registration.
        if authVerify.Google_Verify_Result(gtoken, verifycode):
            return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/search', methods=['POST'])
def search():
    # show all searchresults on the webpage directly
    keyword = request.form['keyword']
    filename = tParser_Post.searchresults(keyword)  # json file
    io = open(filename, "r")
    dictionary = json.load(io)  # jsonfile to python object
    print(dictionary)
    return render_template('search.html', data=dictionary)  # Content of dictionary will be shown on the webpage

###########################################
#   another option to show a download link on the webpage
#    keyword = request.form['keyword']
#    filename = tParser_Post.searchresults(keyword)  # json file
#    return render_template('search_old.html', filename=filename)   # A link for downloading of file is available on the
# webpage
###########################################


if __name__ == '__main__':
    app.run()
