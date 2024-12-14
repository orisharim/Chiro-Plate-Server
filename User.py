class User:
    def __init__(self, info : dict):
        self.id = int(info['user_id'])
        self.password = info['user_password']
        

        