import json, datetime
import monitor
from flask import Flask
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

with open("settings.json") as json_file:
    config = json.load(json_file)

monitor_status_flag = 0

def monitor_test(ip_list, recording_directory, camera_name, expecting_video_numbers, monitor_status_flag):
    '''
    Test the connection of monitors and record files in this computer.
    '''
    monitor.connection_test(ip_list, monitor_status_flag)

    yesterday =  str(datetime.date.today() - datetime.timedelta(days=1))
    for camera in camera_name:
        monitor.recording_check(recording_directory + yesterday + camera, expecting_video_numbers, monitor_status_flag)
    
    return monitor_status_flag

def ok(bool):
    if bool:
        return "OK"
    return "Down"

app = Flask(__name__)

@app.route('/heartbeats', methods=['GET'])
def heartbeats():
    monitor_test(config["ip_list"], config["recording_directory"], config["camera_name"], config["expecting_video_numbers"], monitor_status_flag)
    result = {"monitor_connection": ok(not monitor.is_connection_error()), "monitor_recording": ok(not monitor.is_recording_error())}
    return result

s = HTTPServer(WSGIContainer(app))
s.listen(80)
IOLoop.current().start()