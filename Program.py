import tkinter as tk
from Server import Server
import threading
import json

clients = {} #structure of {plate_id: { user_id: 0
             #                          user_password: 0
             #                         'level 1 start time': 0,
             #                         'level 1 stars': 0,
             #                          .
             #                          .
             #                          .
             #                          'level 10 start time' : 0,
             #                          'level 1 stars' : 0
             #                            }}


def receive(message):
    global clients
    message = json.loads(message)
    client_plates[message['plate_id']] = 1
    print(client_plates)

def respond():
    return 'balls'


def onPress():
    print('k')


def main():
    global client_plates

    #setup screen
    screen = tk.Tk()
    screen.title('chiro plate')
    button = tk.Button(screen, text='Send', width=25, command=onPress)
    button.pack()

    #setup server
    server = Server('localhost', 12345)
    server_thread = threading.Thread(target=server.start_server,
                                     args=(receive, respond))

    #execution
    server_thread.start()
    screen.mainloop()


if __name__ == '__main__':
    main()
