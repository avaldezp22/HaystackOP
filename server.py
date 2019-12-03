import time
import zmq

context = zmq.Context()
socket  = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait fpr next request from client
    message = socket.recv()
    print("Received request: %s"%message)
    #Do some "work"
    time.sleep(1)
    #Send reply back to client
    socket.send(b"world")
