from flask import Flask, render_template
import socket

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Get the local IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print(f" * Running on http://{ip_address}:5000 (Local Network)")
    
    # Run the server on all available interfaces (for access via IP)
    app.run(host='0.0.0.0', port=5000, debug=True)
