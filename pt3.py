from flask import Flask, render_template
import platform
import cpuinfo
import socket

app = Flask(__name__)

class SystemInfo:
    def __init__(self):
        self.system = platform.system()
        self.processor = cpuinfo.get_cpu_info()['brand_raw']
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)

@app.route('/')
def home():
    system_info = SystemInfo()
    return render_template('system_info.html', system_info=system_info)

if __name__ == '__main__':
    app.run(debug=True)
