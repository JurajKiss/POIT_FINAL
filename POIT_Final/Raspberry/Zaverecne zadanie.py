from threading import Lock
from flask import Flask, render_template, session, request, jsonify, url_for
from flask_socketio import SocketIO, emit, disconnect    
import serial
import time
import random
import math

ser=serial.Serial("/dev/ttyUSB0",9600)
ser.baudrate=9600

async_mode = None

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock() 

generate = False


def background_thread(args):
    count = 0             
    while True:
        if generate:
            socketio.sleep(2)
            data = ReadValue()
            count += 1
            socketio.emit('my_response',
                          {'data': data, 'count': count},
                          namespace='/test')  

@app.route('/')
def index():
    return render_template('tabs.html', async_mode=socketio.async_mode)
 
@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()
    
@socketio.on('generate_request', namespace='/test')
def generate_request():
    global generate
    generate = not generate
    print(generate)
    SendStop()

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread, args=session._get_current_object())
    emit('my_response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)
    
def ReadValue():
	read_ser=ser.read_all().decode("utf-8")
	lines = read_ser.split("\n")
	line = lines[-2]
	cleaned = line.strip()
	parts = cleaned.split()
	value = float(parts[1])
	
	return value

def SendStop():
	message = "Light"
	byte_message = message.encode("utf-8")
	ser.write(byte_message)

if __name__ == '__main__':
    
    
    socketio.run(app, host="0.0.0.0", port=80, debug=True)
