from flask import Flask, request, make_response
import os

FLAG1 = 'mission 1 success<br>'
FLAG2 = 'mission 2 success<br>'
FLAG3 = 'mission 3 success<br>'
FLAG4 = 'mission 4 success<br>'
FLAG5 = 'mission 5 success<br>'

PAGE = """
        <h1>your mission:</h1><br>
        1.use parameter: UwU=u<br>
        2.post **form**: Luv=u<br>
        3.use admin character<br>
        4.request from 127.0.0.1<br>
        5.use browser 'MoeBrowser'<br>
        Complete All Missions<br><br>"""

app = Flask(__name__)


# get parameter
# post form
# check cookie
# try xff
# define ua
@app.route("/", methods=["GET", "POST"])
def application():
    ret = PAGE
    flag = 0

    try:
        if request.args.get('UwU') == 'u':
            ret += FLAG1
            flag += 1
    except:
        pass
    if request.method == 'GET':
        ret = 'this is GET method, ' + ret
    if request.method == 'POST':
        ret = 'this is POST method, ' + ret
        try:
            if request.form['Luv'] == 'u':
                ret += FLAG2
                flag += 1
        except: pass
    if request.cookies.get('character') == 'admin':
        ret += FLAG3
        flag += 1
    if request.headers.get('X-Forwarded-For') == '127.0.0.1':
        ret += FLAG4
        flag += 1
    if request.user_agent.string == 'MoeBrowser':
        ret += FLAG5
        flag += 1
    if flag == 5:
        ret += f"<br>Brilliant! Now I give you my flag: {os.getenv('FLAG')}"
    resp = make_response(ret)
    if request.cookies.get('character') is None or request.cookies.get('character') != 'admin':
        resp.set_cookie('character', 'guest')
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
