from curses import flash
from flask import Flask, request, render_template, redirect, session, url_for, flash
import os
import dataSql
import datetime
from hashlib import md5

app = Flask(__name__)

app.template_folder = os.path.join("static/templates")
app.static_folder = os.path.join("static")

app.secret_key = "This-random-secretKey-you-can't-get" + os.urandom(2).hex()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' not in session:
        if request.method == 'GET':
            return render_template('login.html')
        username = request.form['user']
        password = request.form['password']
        if dataSql.canLogin(username, password):
            session['user'] = username
            session['power'] = dataSql.getPower(username)
            return redirect('/index')
        else:
            flash("username or password incorrect")
            return redirect('login')
    else:
        return '''<script>alert("You have already logged in.");window.location.href="/index";</script>'''

# change the password


@app.route('/change', methods=['GET', 'POST'])
def foundpwd():
    if request.method == 'GET':
        return render_template('changepwd.html')
    username = request.form['user']
    oldPassword = request.form['oldPassword']
    newPassword = request.form['newPassword']
    a = dataSql.changePassword(username, oldPassword, newPassword)
    if a == True:
        return '''
    change successfully
    <br>
    <a href='login'>login now</a>
    '''
    else:
        flash(a)
        return redirect('change')


# register for enter the message board
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    id = dataSql.usersName()
    username = request.form['user']
    password = request.form['password']
    power = 'guest'
    if dataSql.register(id, username, password, power):
        return '''
    register successfully
    <br>
    <a href='login'>login now</a>
    '''
    else:
        flash('username already exists')
        return redirect('register')


@app.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user')
        return redirect('/login')
    else:
        return '''
    you are not logged in
    <br>
    <a href='login'>login now</a>
    '''


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'user' in session:
        if request.method == 'GET':
            msg = getMsgList()
            if session['power'] == 'guest':
                for i in msg:
                    # remove the message send by other user on private condition
                    if i[3] == "1" and session['user'] != i[0]:
                        msg.remove(i)
            return render_template('index.html', username=session['user'], msg=msg)
        else:
            message = request.form['message']
            username = session['user']
            nowtime = str(datetime.datetime.now())
            if 'private' in request.form:
                private = 1
            else:
                private = 0
            if message == '':
                return '''<script>alert("invalid input");window.location.href="/index";</script>'''
            dataSql.uploadMessage(username, message, nowtime, private)
            return '''<script>alert("upload successfully");window.location.href="/index";</script>'''
    else:
        return redirect('/login')


@app.route('/delete', methods=['GET'])
def delete():
    if 'user' in session:
        psg = request.args.get('psg')
        msg = list(dataSql.showMessage())
        for i in range(len(msg)):
            h1 = md5()
            h1.update(str(msg[i][2]).encode(encoding='utf-8'))
            h2 = h1.hexdigest()
            if (msg[i][0] == session['user'] or session['power'] == 'root') and h2 == psg:
                dataSql.deleteMessage(msg[i][0], msg[i][2])
                return redirect('/index')
        return '''<script>alert("Permission denied");window.location.href="/index";</script>'''
    else:
        return '''<script>alert("login first");window.location.href="/index";</script>'''


@app.route('/index/api/getMessage', methods=['GET'])
def getMessage():
    username = request.args.get('username')
    password = request.args.get('password')
    if(username == None or password == None):
        return {'status': 'failed', 'message': 'invalid input'}
    elif(not dataSql.canLogin(username, password)):
        return {'status': 'failed', 'message': 'username or password incorrect'}
    elif(dataSql.canLogin(username, password)):
        msg = getMsgList()
        if dataSql.getPower(username) == 'guest':
            for i in msg:
                # remove the message send by other user on private condition
                if i[3] == "1" and username != i[0]:
                    msg.remove(i)
        return msg


def getMsgList():
    msg = list(dataSql.showMessage())
    for i in range(len(msg)):
        h1 = md5()
        h1.update(str(msg[i][2]).encode(encoding='utf-8'))
        msg[i] += tuple([h1.hexdigest()])
    return msg


if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True, port=8080)
