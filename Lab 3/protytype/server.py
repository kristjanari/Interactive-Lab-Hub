from flask import Flask, render_template
import sys


app = Flask(__name__)

@app.route('/')
def index():
    notes = []
    for line in sys.stdin:
        notes.append(line)
        print(line)
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


