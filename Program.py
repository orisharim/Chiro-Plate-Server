import tkinter as tk
from Server import Server
import threading
import json
from Database import Database
from User import User
import Settings

screen = tk.Tk()
server = Server(Settings.SERVER_IP, Settings.SERVER_PORT)
database = Database(Settings.DB_KEY)
clients = {}  # structure of {plate_id(key): {
#                               'user_id': 0
#                               'user_password': 0
#                               'level_1_duration': 0,
#                               'level_1_difficulty': 0,
#                               .
#                               .
#                               .
#                               'level_x_duration' : 0,
#                               'level_x_difficulty' : 0
#                            }}

def receive(message):
    # message = {
    #            message_type: 0 (0 login)
    #            plate_id: 0,
    #            user_id: 0,
    #            user_password: 0,    }

    global clients, database
    message = json.loads(message)
    user_info = database.get_user(message['user_id']).get_dict()
    print(user_info)


def respond(message):
    global clients, database
    message = json.loads(message)
    user_info = database.get_user(message['user_id']).get_dict()
    user_info_json = json.dumps(user_info)
    return user_info_json


def create_user(user_id, user_password):
    user = User(user_id=user_id, user_password=user_password)
    database.add_user(user)


def on_press():

    create_user(user_id=(1234), user_password=('balls'))


def main():
    global database, screen, server

    # setup screen
    screen.title('chiro plate')
    button = tk.Button(screen, text='Send', width=25, command=on_press)
    button.pack()

    # setup server
    server_thread = threading.Thread(target=server.start_server,
                                     args=(receive, respond))

    # execution
    server_thread.start()
    screen.mainloop()


if __name__ == '__main__':
    main()
