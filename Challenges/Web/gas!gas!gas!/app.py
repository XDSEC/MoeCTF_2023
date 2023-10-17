import random
import time
import os

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(16)


def gen_control():
    steering_control = random.choice([['弯道向左', -1], ['弯道直行', 0], ['弯道向右', 1]])
    throttle = random.choice([['抓地力太小了！', 0], ['保持这个速度', 1], ['抓地力太大了！', 2]])
    return [steering_control[1], throttle[1]], steering_control[0] + '，' + throttle[0]


def check_control(steering_control, throttle, control):
    flag = 0
    if (steering_control == '0' and control[0] == 0) or (steering_control == '1' and control[0] == -1) or (
            steering_control == '-1' and control[0] == 1):
        flag += 1
    if throttle == str(control[1]):
        flag += 1
    if flag == 2:
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', next_prompt=None)
    if request.method == 'POST':

        if request.form.get('driver') is None:
            return render_template('index.html', next_prompt='<h3><font color="red">你选手呢？？</font></h3>')

        #  新选手
        if request.form.get('driver') != session.get('driver'):
            session['driver'] = request.form.get('driver')
            session['round'] = 0
            session['start_time'] = time.time()
            session['time'] = time.time()
            session['next_control'], session['control_hint'] = gen_control()
            return render_template('index.html', next_prompt='<h2>比赛开始！</h2>'
                                                             '<h3><font color="red">' + session['control_hint'] + "</font></h3>")

        #  老选手
        if request.form['driver'] == session.get('driver'):

            #  胜利
            if session.get('round') == 5:
                ua = request.user_agent.string

                if session.get('flag') is None:
                    session['flag'] = str(time.time() - session.get("start_time"))

                return render_template('index.html', next_prompt='<h3>完美的漂移！你的记录会被载入史册！</h3><br>'

                                                                 f'座驾: {ua if ua != "" else "诶你的User-Agent是空的"}<br>'
                                                                 f'用时(s): {session["flag"]}<br>'
                                                                 f'这是你的奖励！ {os.getenv("FLAG")}')

            if time.time() - session['time'] > 3:
                session['driver'] = None
                return render_template("index.html", next_prompt=f"<h3><font color='red'>太慢了！车手，下次反应快一点</font></h3>")
            if check_control(request.form.get('steering_control'), request.form.get('throttle'),
                             session['next_control']):
                session['round'] += 1
                session['time'] = time.time()
                session['next_control'], session['control_hint'] = gen_control()
                return render_template('index.html', next_prompt= '<h3><font color="red">' + session['control_hint'] + "</font></h3>")
            else:
                session['driver'] = None
                return render_template('index.html', next_prompt='<h3><font color="red">失误了！别紧张，车手，重新来过吧</font></h3>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
