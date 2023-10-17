from flask import Flask, render_template, request
import subprocess

subprocess.run(['python', 'gen.py'])
app = Flask(__name__)


@app.route('/')
def index():
    d = request.args.get('id')
    if d is not None and d.isdigit():
        int_d = int(d)
        if 1000 >= int_d >= 1:
            return render_template(f"ChatLog{d}.html")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
