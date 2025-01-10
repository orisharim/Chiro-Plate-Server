import Settings


class User:

    def __init__(self, info: dict = None, user_id: int = None, user_password: str = None):
        if info is not None:
            self.set_dict(info)
        elif user_id is not None and user_password is not None:
            self.id = user_id
            self.password = user_password
            self.levels = []
            for i in range(0, Settings.NUMBER_OF_LEVELS):
                duration = 0
                difficulty = 0
                self.levels.append((duration, difficulty))
        else:
            raise Exception("a user must be initiated using a dict or a user id and password")

    def set_dict(self, info: dict):
        self.id = int(info['user_id'])
        self.password = info['user_password']
        self.levels = []
        for i in range(0, Settings.NUMBER_OF_LEVELS):
            duration = int(info[f'level_{i + 1}_duration'])
            difficulty = int(info[f'level_{i + 1}_difficulty'])
            self.levels.append((duration, difficulty))

    # def update_levels()

    def get_dict(self):
        dic = dict()
        dic['user_id'] = self.id
        dic['user_password'] = self.password
        for i in range(0, Settings.NUMBER_OF_LEVELS):
            duration = self.levels[i][0]
            difficulty = self.levels[i][1]
            dic[f'level_{i + 1}_duration'] = duration
            dic[f'level_{i + 1}_difficulty'] = difficulty
        return dic

    def get_id(self):
        return self.id

    def set_id(self, user_id: int):
        self.id = user_id

    def set_password(self, user_password: str or int):
        self.password = user_password
