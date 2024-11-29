import tkinter as tk
from Server import Server
import threading
import json


def receive(message):
    message = json.loads(message) #convert from json to dict
    print(message)
def respond():
    return 'balls'

def onPress():
    print('k')

if __name__ == '__main__':
    plates = {
        1: 0,
        2: 0,
        3: 0
    }

    screen = tk.Tk()
    screen.title('chiro plate')
    button = tk.Button(screen, text='Send', width=25, command=onPress)
    button.pack()
    server = Server('localhost', 12345)
    server_thread = threading.Thread(target=server.start_server,
                                     args=(receive, respond))
    server_thread.start()
    screen.mainloop()

