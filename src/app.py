"""Module providingFunction printing python version."""
import socket

"""Module providingFunction printing python version."""
from flask import Flask,render_template

app = Flask(__name__)

"""Module providingFunction printing python version."""
@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')

"""Module providingFunction printing python version."""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
