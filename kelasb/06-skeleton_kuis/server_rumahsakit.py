import socket
import threading

def handle_server():
    print("Bagian Server")
    # To Do : Bagian RPC / HTTP Server

while True :    
    t = threading.Thread(target=handle_thread, args=(conn,))
    t.start()

    # To Do : Bagian Subscriber