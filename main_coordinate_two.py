# -*- coding: utf-8 -*-

# made by Leni.

# import uiFile.
from uiFile.main import Ui_MainWindow
from uiFile.setting import Ui_SettingWindow
from func_connection import Connection
from func_calculation import Calculation

import value
import data_set_two

from main_setting import Setting
from info_socket import Socket

# import PyQt5 modules.
from PyQt5.QtGui import QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsLineItem, QMessageBox

# import other modules.
import sys
import time


# make Main_Function class.
class MainFunction(QMainWindow, QObject):
    def __init__(self):
        QMainWindow.__init__(self)

        # define values file upload.
        value.set_value()
        self.measureData = []
        self.tempMessage = []
        self.xlist, self.ylist, self.rlist, self.xclist, self.yclist, self.laserlist = [], [], [], [], [], []
        self.tempData = [self.measureData, self.xlist, self.ylist, self.rlist, self.xclist, self.yclist, self.laserlist]
        self.resultData = data_set_two.MeasureData(None)

        # start ui drawing.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # set window view size maximum.
        self.showMaximized()

        self.message_list = [self.ui.msg_1, self.ui.msg_2, self.ui.msg_3, self.ui.msg_4, self.ui.msg_5]

        # laser connect state ui values list.
        self.uiList = [self.ui.img_Rsock, self.ui.img_Lsock, self.ui.img_Bsock]
        self.uiBList = [self.ui.img_B1, self.ui.img_B2, self.ui.laser_state_B]

        # laser state ui values list.
        self.uiLaserList = [self.ui.img_R1, self.ui.img_R2, self.ui.img_R3, self.ui.img_R4, self.ui.img_L1, self.ui.img_L2, self.ui.img_L3, self.ui.img_L4]
        self.layerlist = [self.ui.layer_R1, self.ui.layer_R2, self.ui.layer_R3, self.ui.layer_R4, self.ui.layer_L1,
                          self.ui.layer_L2, self.ui.layer_L3, self.ui.layer_L4]

        # set range.
        self.gScene = QGraphicsScene(0, 0, value.get_frame()/4, value.get_frame()/4,
                                     self.ui.graphicsView)
        self.ui.graphicsView.setScene(self.gScene)

        # socket connection start
        self.th = Socket(self, self.uiList)
        self.th.start()
        self.dialog = Connection(self.th)
        self.calculation = Calculation()

        # setting window set.
        Setting.setting = Setting(self.th, self.uiBList)
        Setting.setting.ui = Ui_SettingWindow()
        Setting.setting.ui.setupUi(Setting.setting)
        Setting.setting.btnList = [Setting.setting.ui.btn_laser, Setting.setting.ui.btn_chuck_default,
                        Setting.setting.ui.btn_frame_set, Setting.setting.ui.btn_coor_set,
                        Setting.setting.ui.btn_chuck_set, Setting.setting.ui.btn_laser_set]
        Setting.setting.ui.setting_info.setText('척 기본값 : %s\n프레임 길이 : %d\n좌표계 보정값 : %s\n척 보정값 : %s\n레이저 사이 간격 : %s'
                                                % (value.get_chuck(), value.get_frame(), value.get_coor(), value.get_chuck_scale(), value.get_laser()))

        # drawing basic view ---------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------
        # pen, brush setting
        inside_color = QBrush(Qt.white)
        pen = QPen(Qt.red)
        pen.setWidth(4)

        # make 8 laser lines
        self.laser = []
        line = self.calculation.get_laser_location()
        for i in range(len(line)):
            line[i] = line[i] * 0.25
            self.laser.append(QGraphicsLineItem(0, (self.gScene.height() / 2-line[i]), self.gScene.width(), (self.gScene.height() / 2-line[i])))
            self.laser[i].setPen(pen)
            self.gScene.addItem(self.laser[i])

        # make circle
        pen.setColor(Qt.blue)
        self.circle = self.gScene.addEllipse(self.gScene.width() / 2 - 50,  self.gScene.height() / 2 - 50, 100, 100, pen, inside_color)
        self.circle_pot = self.gScene.addEllipse(self.gScene.width() / 2 - 2.25, self.gScene.height() / 2 - 2.25, 5, 5, pen, Qt.blue)

        # make chuck pot
        pen.setColor(Qt.red)
        self.chuck_pot = self.gScene.addEllipse(self.gScene.width() / 2 - 2.25, self.gScene.height() / 2 - 2.25, 5,
                                                5, pen, Qt.red)

        # make x, y lines
        self.x_line = QGraphicsLineItem(0, self.gScene.height() / 2, self.gScene.width(), self.gScene.height() / 2)
        self.gScene.addItem(self.x_line)
        self.y_line = QGraphicsLineItem(self.gScene.width() / 2, 0, self.gScene.width() / 2, self.gScene.height())
        self.gScene.addItem(self.y_line)

    def slot_menu(self):
        Setting.setting.show()

    def slot_exit(self):
        self.close()

    def closeEvent(self, event):
        result = QMessageBox.question(self, 'exit message', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            self.th.closet_socket()
            event.accept()

    def message_setting(self, message):
        # reset message list : new first old next.
        for i in range(len(self.message_list)-1, 0, -1):
            self.message_list[i].setText(self.message_list[i-1].text())
        self.message_list[0].setText(message)

    def double_arr(self, i, fot_int):
        temp_result = []
        for j in range(fot_int):
            temp = []
            for k in range(len(self.tempData[i])):
                temp.append(self.tempData[i][k][j])
            print 'slot_ok :: temp > ', temp
            temp.sort()
            print 'slot_ok :: temp sort > ', temp
            half = int(len(temp) / 2)
            print 'double_arr :: half >> ', half
            temp_result.append(temp[half + 1])

        print 'slot_ok :: temp_result > ', temp_result
        return temp_result[:]

    # 알고리즘 후 max choice.
    def slot_ok(self):
        self.chuck_define = Setting.setting.get_chuck()

        if len(self.chuck_define) != 2:
            # if system don't have chuck information, you can't start measure program.
            QMessageBox.question(self, 'Alert Box', '척 기본값을 먼저 셋팅해 주세요.', QMessageBox.Yes)

        else:
            # [ change ] image -> text.
            self.slot_ok_time = time.time()

            for_int = 0
            del self.measureData[:]
            del self.tempMessage[:]

            for i in range(len(self.tempData)):
                del self.tempData[i][:]

            object_name = self.sender().objectName()

            if object_name == 'btn_one':
                for_int = 1
            elif object_name == 'btn_all_ten':
                for_int = 10
            else:
                for_int = 5

            circle_scale = value.get_coor()
            chuck_scale = value.get_chuck_scale()

            self.resultData = data_set_two.MeasureData(None)

            for i in range(for_int):
                self.measureData.append(self.th.message('$MEASURE\0'))

            for i in range(for_int):
                laser_length = self.measureData[i]

                if len(laser_length) == 10:
                    pipe = self.calculation.func_calculation(laser_length)

                    # Scale pipeY, pipeZ, chuck_x, chuck_y.
                    pipeY = pipe[0] - circle_scale[0]
                    pipeZ = pipe[1] - circle_scale[1]

                    chuck_y = (laser_length[-2] - self.chuck_define[0]) - chuck_scale[0]
                    chuck_z = (laser_length[-1] - self.chuck_define[1]) - chuck_scale[1]

                    # self.tempData = [self.xlist, self.ylist, self.rlist, self.xclist, self.yclist, self.laserlist]
                    self.tempData[1].append(pipeY)
                    self.tempData[2].append(pipeZ)
                    self.tempData[3].append(pipe[2])
                    self.tempData[4].append(chuck_y)
                    self.tempData[5].append(chuck_z)
                    self.tempData[6].append(pipe[3])

                    self.tempMessage.append('\t파이프 좌표 y, z (%d, %d) / 파이프 지름 : %d \n\t척 y, z (%d, %d)\n\t%02d:%02d:%02d'
                                            % (-pipeY, pipeZ, pipe[2] * 2, -chuck_y, chuck_z, time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))

                else:
                    self.tempData[1].append('error')
                    self.tempData[2].append('error')
                    self.tempData[3].append(0)
                    self.tempData[4].append('error')
                    self.tempData[5].append('error')
                    self.tempData[6].append([0, 0, 0, 0, 0, 0])

                    self.tempMessage.append('\t측정이 잘못되었습니다. 측정을 다시 시도해주세요.\n\t%02d:%02d:%02d' %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))

            result = []
            half = int(for_int/2)
            for i in range(len(self.tempData)):

                if object_name == 'btn_one':
                    if self.tempData[i][0] == 'error':
                        self.resultData.errorFlag = True
                        break

                    else:
                        result.append(self.tempData[i][0])

                else:
                    if i == 0:
                        result.append(self.double_arr(i, 10))

                    elif i != len(self.tempData)-1:
                        self.tempData[i].sort()

                        if self.tempData[i][half+1] == 'error':
                            self.resultData.errorFlag = True
                            break

                        else:
                            result.append(self.tempData[i][half])

                    else:
                        result.append(self.double_arr(i, 6))

            if not self.resultData.errorFlag:
                self.resultData.setting(result)
                if len(self.measureData) > 0:

                    if object_name == 'btn_one':
                        message = self.resultData.message
                        self.message_setting(message+'\n\t%02d:%02d:%02d' %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))

                    else:
                        # error check
                        try:
                            # 일부러 5번으로 막아 놓았다. view 부분을 어떻게 수정하지?  scroll 을 넣을 것 인가?
                            for i in range(5):
                                self.message_list[-i-1].setText(str(i+1) + '번 측정\n' + self.tempMessage[i]+'\n\t%02d:%02d:%02d' %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
                        except Exception as e:
                            print 'slot_ok :: message maker error > ', e

                    self.ui.msg_0.setText('최종 값\n' +self.resultData.message+'\n\t%02d:%02d:%02d' %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
                    self.draw()

            else:
                self.ui.msg_0.setText('\t측정이 잘못되었습니다. 다시 측정해주세요.\n\t%02d:%02d:%02d' %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
                self.message_setting('\t측정이 잘못되었습니다. 다시 측정해주세요.\n\t%02d:%02d:%02d' %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
                self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/non-arrow.png'))
                self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/non-arrow.png'))
                self.ui.information_LR.setText('ㅡ')
                self.ui.information_UD.setText('ㅡ')

    def draw(self):
        if self.resultData is not None:
            laserLength = self.resultData.laserData
            pipe_y, pipe_z, pipe_r, chuckY, chuckZ, laser_state, message = self.resultData.getting()

            print '\n\ndef draw(self) in ---------------------------------------------------------------------------------------'
            print 'draw :: laserLength > %s' % laserLength
            print 'draw :: pipe_y > ', pipe_y
            print 'draw :: pipe_z > ', pipe_z
            print 'draw :: pipe_r > ', pipe_r
            print 'draw :: chuckX > ', chuckY
            print 'draw :: chuckY > ', chuckZ
            print 'draw :: laserState > ', laser_state
            print 'draw :: message > ', message
            print '----------------------------------------------------------------------------------------------------------------\n\n'

            # Show lasers measuring data.
            for i in range(len(laserLength) - 2):
                self.layerlist[i].display(int(laserLength[i]))

            # 이후에 대한 내용은 마지막 값에 대한 결과만 표시할 것.
            if laser_state[-2] == 1:
                self.ui.img_B1.setPixmap(QPixmap('Dusan-4/uiFile/red-check.png'))
            else:
                self.ui.img_B1.setPixmap(QPixmap('Dusan-4/uiFile/uncheck.png'))
            if laser_state[-1] == 1:
                self.ui.img_B2.setPixmap(QPixmap('Dusan-4/uiFile/red-check.png'))
            else:
                self.ui.img_B2.setPixmap(QPixmap('Dusan-4/uiFile/uncheck.png'))

            if laser_state[-1] == 1 and laser_state[-2] == 1:
                self.ui.laser_state_B.setText('후면 레이저의 측정이 완료되었습니다.')
            else:
                self.ui.laser_state_B.setText('후면 레이저의 측정을 실패하였습니다.')

            count = 0
            for i in range(len(laser_state)-2):
                if laser_state[i] == 1:
                    count += 1
                    self.uiLaserList[i].setPixmap(QPixmap('Dusan-4/uiFile/red-check.png'))
                    self.uiLaserList[i+4].setPixmap(QPixmap('Dusan-4/uiFile/red-check.png'))
                else:
                    self.uiLaserList[i].setPixmap(QPixmap('Dusan-4/uiFile/uncheck.png'))
                    self.uiLaserList[i+4].setPixmap(QPixmap('Dusan-4/uiFile/uncheck.png'))

            if count == (len(laser_state)-2):
                self.ui.laser_state_RL.setText('정확도가 가장 높은 상태입니다.')
            elif count == 2:
                self.ui.laser_state_RL.setText('정확도가 가장 낮은 상태입니다.')
            elif count < 2:
                self.ui.laser_state_RL.setText('측정을 위해서\n최소 4개의 데이터가 필요합니다.\n재측정 해주세요.')
            else:
                if laser_state[0] == 0:
                    self.ui.laser_state_RL.setText('파이프 위치를 조금 위로 조정해주시면\n정확도가 올라갑니다.')
                elif laser_state[3] == 0:
                    self.ui.laser_state_RL.setText('파이프 위치를 조금 아래로 조정해주시면\n정확도가 올라갑니다.')

            # 원을 좌표계에 그리기 시작함.
            self.circle.setRect(self.gScene.width() / 2 - pipe_r,
                                self.gScene.height() / 2 - pipe_r,  pipe_r * 2,  pipe_r * 2)
            self.circle.setPos(float(pipe_y), float(-pipe_z))
            self.circle_pot.setPos(float(pipe_y), float(-pipe_z))

            # 척을 좌표계에 그리기 시작함.
            self.chuck_pot.setPos(chuckY, -chuckZ)

            if int(pipe_y - chuckY) > 0:
                self.ui.information_LR.setText('척을 y+ 방향으로 %dmm 이동하세요.' % abs(pipe_y - chuckY))
                self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/left-arrow.png'))
            elif int(pipe_y - chuckY) < 0:
                self.ui.information_LR.setText('척을 y- 방향으로 %dmm 이동하세요.' % abs(pipe_y - chuckY))
                self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/right-arrow.png'))
            else:
                self.ui.information_LR.setText('파이프와 척의 좌우가 일치합니다.')
                self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/arrow.png'))

            if int(pipe_z - chuckZ) > 0:
                self.ui.information_UD.setText('척을 Down 방향으로 %dmm 이동하세요.' % abs(pipe_z - chuckZ))
                self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/down-arrow.png'))
            elif int(pipe_z - chuckZ) < 0:
                self.ui.information_UD.setText('척을 Up 방향으로 %dmm 이동하세요.' % abs(pipe_z - chuckZ))
                self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/up-arrow.png'))
            else:
                self.ui.information_UD.setText('파이프와 척의 상하가 일치합니다.')
                self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/arrow.png'))

            # 사용자에게 움직임을 알려줄 UI tip 생성.
            # if int(self.circle.x() - self.chuck_pot.x()) > 0:
            #     self.ui.information_LR.setText('척을 y- 방향으로 %dmm 이동하세요.' % abs(pipe_y - chuckY))
            #     self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/right-arrow.png'))
            # elif int(self.circle.x() - self.chuck_pot.x()) < 0:
            #     self.ui.information_LR.setText('척을 y+ 방향으로 %dmm 이동하세요.' % abs(pipe_y - chuckY))
            #     self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/left-arrow.png'))
            # else:
            #     self.ui.information_LR.setText('파이프와 척의 좌우가 일치합니다.')
            #     self.ui.img_LR.setPixmap(QPixmap('Dusan-4/uiFile/arrow.png'))
            #
            # if int(self.circle.y() - self.chuck_pot.y()) < 0:
            #     self.ui.information_UD.setText('척을 Up 방향으로 %dmm 이동하세요.' % abs(pipe_z - chuckZ))
            #     self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/up-arrow.png'))
            # elif int(self.circle.y() - self.chuck_pot.y()) > 0:
            #     self.ui.information_UD.setText('척을 Down 방향으로 %dmm 이동하세요.' % abs(pipe_z - chuckZ))
            #     self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/down-arrow.png'))
            # else:
            #     self.ui.information_UD.setText('파이프와 척의 상하가 일치합니다.')
            #     self.ui.img_UD.setPixmap(QPixmap('Dusan-4/uiFile/arrow.png'))

            print '----------------------------------------------------------- end main program : %s' %(self.slot_ok_time - time.time())


# start Main process.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainFunction = MainFunction()
    sys.exit(app.exec_())
