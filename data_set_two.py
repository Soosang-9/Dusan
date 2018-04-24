# -*- coding: utf-8 -*-

class MeasureData:
    def __init__(self, data):
        # define values
        self.errorFlag = False
        self.laserData = data
        self.pipeY, self.pipeZ, self.pipeR = None, None, None
        self.chuckY, self.chuckZ = None, None
        self.laserState =None
        self.message = None

    def setting(self, argv):
        self.laserData = argv[0]
        self.pipeY, self.pipeZ, self.pipeR = argv[1], argv[2], argv[3]
        self.chuckY, self.chuckZ = argv[4], argv[5]
        self.laserState = argv[6]

        if self.laserState == [0, 0, 0, 0, 0, 0]:
            message = '\t값이 이상하게 측정되었습니다. 측정을 다시 시도해 주세요.'
        else:
            message = '\t파이프 좌표 y, z (%d, %d) / 파이프 지름 : %d \n\t척 y, z (%d, %d)' % (
                                    -self.pipeY, self.pipeZ, self.pipeR * 2, -self.chuckY, self.chuckZ)
        self.setting_message(message)

    def setting_message(self, message):
        self.message = message

    def getting(self):
        return self.pipeY, self.pipeZ, self.pipeR, self.chuckY, self.chuckZ, self.laserState, self.message


class ChuckMeasureData:
    def __init__(self, data):
        # define values
        self.errorFlag = False
        self.chuckData = data
        self.chuckY, self.chuckZ = None, None
        self.message = None

    def setting(self, argv):
        self.chuckY, self.chuckZ = argv[0], argv[1]
        self.message = '\t척 y,z (%d, %d)' % (-self.chuckY, self.chuckZ)