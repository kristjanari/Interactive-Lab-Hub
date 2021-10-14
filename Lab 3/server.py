from flask import Flask
import sys

note = ""

for line in sys.stdin:
    note += line

app = Flask(__name__)

@app.route('/')
def index():
    return note

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


