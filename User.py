import Settings


class User:

    def __init__(self, info: dict):
        self.id = int(info['user_id'])
        self.password = info['user_password']
        self.levels = []
        for i in range(0, Settings.NUMBER_OF_LEVELS):
            duration = int(info[f'level_{i + 1}_duration'])
            difficulty = int(info[f'level_{i + 1}_difficulty'])
            self.levels[i] = (duration, difficulty)

    def get_dict(self):
        dic = dict()
        dic['user_id'] = self.id
        dic['user_password'] = self.password
        for i in range(0, Settings.NUMBER_OF_LEVELS):
            duration = self.levels[i][0]
            difficulty = self.levels[i][1]
            dic[f'level_{i + 1}_duration'] = duration
            dic[f'level_{i + 1}_difficulty'] = difficulty
