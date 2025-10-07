from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker and Jenkins Build!"

if __name__ == '__main__':
    print("Hello Jenkins Build")  # From the remote version
    app.run(host='0.0.0.0', port=5000)

