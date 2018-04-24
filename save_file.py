class LaserSaveFile:
    def __init__(self):
        self.__total_data = ''

    def add_data(self, data):
        # 4개면 이쁘게 정리하고 그 외는 그냥 나열하기?
        self.__total_data += data

    def save_file(self, data):
        with open('test file start time to end time', 'wb') as laser_data_file:
            laser_data_file.write(self.__total_data)
