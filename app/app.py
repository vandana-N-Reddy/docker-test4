#app.py


from flask import Flask
import redis
import os

app = Flask(_name_)
redis_host = os.environ.get('REDIS_HOST', 'redis')  # service name as hostname

# Connect to Redis
r = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def index():
    count = r.incr('hits')  # Increment hit counter in Redis
    return f'Hello! This page has been viewed {count} times.'

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
