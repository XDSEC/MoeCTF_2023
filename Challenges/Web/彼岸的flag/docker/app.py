from flask import Flask, render_template
import subprocess
import os

subprocess.run(['python', f'{os.path.dirname(__file__)}/templates/gen.py'])
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("ChatLog.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
