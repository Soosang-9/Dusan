# -*- coding: utf-8 -*-

# made by Leni.
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import value


class Setting(QMainWindow):
    def __init__(self, th, ui_list):
        QMainWindow.__init__(self)
        self.chuck_define = value.get_chuck()
        self.th = th

        self.img_b_list = ui_list
        self.toggle = True
        print 'setting main > ', value.get_value()

    def get_chuck(self):
        return self.chuck_define

    def slot_ok(self):
        while True:
            self.chuck_define = []
            result = self.th.back_message(self.chuck_define, '$MEASURE\0')
            print '%s, %s' %(result, len(self.chuck_define))
            if (result != 'error') & (len(self.chuck_define) == 2):
                if self.chuck_define != 0:
                    self.img_b_list[0].setPixmap(QPixmap('Dusan-4/uiFile/red-check.png'))
                else:
                    self.img_b_list[0].setPixmap(QPixmap('Dusan-4/uiFile/uncheck.png'))
                if self.chuck_define[1] != 0:
                    self.img_b_list[1].setPixmap(QPixmap('Dusan-4/uiFile/red-check.png'))
                else:
                    self.img_b_list[1].setPixmap(QPixmap('Dusan-4/uiFile/uncheck.png'))
                if (self.chuck_define[0] != 0) & (self.chuck_define[1] != 0):
                    self.img_b_list[2].setText('후면 레이저의 측정이 완료되었습니다.\n초기값을 변경하였습니다.')
                    value.set_chuck(self.chuck_define)
                else:
                    self.img_b_list[2].setText('후면 레이저의 측정을 실패하였습니다.\n초기값이 변경되지 않았습니다.')
                    self.chuck_define = value.get_chuck()

                self.ui.setting_com.setText('')
                self.ui.setting_info.setText('척 기본값 : %s\n프레임 길이 : %d\n좌표계 보정값 : %s\n척 보정값 : %s\n레이저 사이 간격 : %s'
                                             % (value.get_chuck(), value.get_frame(), value.get_coor(),
                                                value.get_chuck_scale(), value.get_laser()))
                break

    def slot_locate(self):
        if self.toggle:
            result = self.th.locate_message('$LOCATE\0')
            if result:
                self.toggle = not self.toggle
                for i in range(len(Setting.setting.btnList)):
                    if i != 0:
                        Setting.setting.btnList[i].setEnabled(False)
                self.ui.btn_laser.setText('레이저 셋팅 종료')

        else:
            result = self.th.locate_message('$LOCATE_END\0')
            if result:
                self.toggle = not self.toggle
                for i in range(len(Setting.setting.btnList)):
                    if i != 0:
                        Setting.setting.btnList[i].setEnabled(True)
                self.ui.btn_laser.setText('레이저 위치 설정')

    def slot_action(self):
        command = self.sender().objectName()
        passNumber = None

        if self.toggle:
            self.toggle = not self.toggle
            self.ui.setting_com.setEnabled(True)

            if command == 'btn_frame_set':
                self.ui.setting_info.setText('< ex >\n\t1670\n\t1674\n\t1660\n\n#현재 프레임 길이\n\t>> %d' % value.get_frame())
                self.ui.setting_com.setPlaceholderText('프레임 길이를 입력해주세요.')
                self.ui.btn_frame_set.setText('프레임 길이설정 완료')
                passNumber = 2

            elif command == 'btn_coor_set':
                self.ui.setting_info.setText('< ex >\n\t6, -32\n\t0, 0\n\t50, 50\n\n#현재 좌표계 보정 값\n\t>> %s' % value.get_coor())
                self.ui.setting_com.setPlaceholderText('보정할 y, x 좌표를 입력해주세요.')
                self.ui.btn_coor_set.setText('좌표계 보정 완료')
                passNumber = 3

            elif command == 'btn_chuck_set':
                self.ui.setting_info.setText('< ex >\n\t10, 10\n\t-10, 3\n\t0, 0\n\n#현재 척 보정 값\n\t>> %s' % value.get_chuck_scale())
                self.ui.setting_com.setPlaceholderText('보정할 y, x 좌표를 입력해주세요.')
                self.ui.btn_chuck_set.setText('척 보정 완료')
                passNumber = 4

            elif command == 'btn_laser_set':
                self.ui.setting_info.setText('< ex > 중심을 기준으로 제일 위쪽 레이저모듈 부터\n\t제일 아래쪽 레이저모듈 순서로 적어주세요.'
                                             '\n\t60, 20, -20, -60\n\t83, 43, -3, -37\n\n#현재 레이저 모듈사이 간격\n\t>> %s' % value.get_laser())
                self.ui.setting_com.setPlaceholderText('레이저 모듈사이 간격( 순서 : R1, R2, R3, R4 )을 입력해주세요.')
                self.ui.btn_laser_set.setText('좌표계 보정 완료')
                passNumber = 5

            for i in range(len(Setting.setting.btnList)):
                if i != passNumber:
                    Setting.setting.btnList[i].setEnabled(False)

        else:
            temp = None
            result = False

            if command == 'btn_frame_set':
                try:
                    temp = self.ui.setting_com.text()
                    temp = int(temp)
                    result = not result
                except Exception as e:
                    QMessageBox.warning(Setting.setting, '경고메시지', '값을 잘못입력하였습니다.\n다시 입력하세요.', QMessageBox.Yes)
                    print 'error > ', e

                # 프레임길이가 너무 큰 경우 막아야 하는데 최대값 뭐로 하지?
                if result:
                    self.ui.btn_frame_set.setText('프레임 길이설정')
                    value.set_frame(temp)
                    passNumber = 2

            elif command == 'btn_coor_set':
                try:
                    temp = self.ui.setting_com.text()
                    temp = temp.split(', ')

                    if len(temp) == 2:
                        temp[0] = int(temp[0])
                        temp[1] = int(temp[1])
                    else:
                        raise Exception

                    result = not result

                except Exception as e:
                    QMessageBox.warning(Setting.setting, '경고메시지', '값을 잘못입력하였습니다.\n다시 입력하세요.', QMessageBox.Yes)
                    print 'error > ', e

                if result:
                    self.ui.btn_coor_set.setText('좌표계 보정값 설정')
                    value.set_coordination(temp)
                    passNumber = 3

            elif command == 'btn_chuck_set':
                try:
                    temp = self.ui.setting_com.text()
                    temp = temp.split(', ')

                    if len(temp) == 2:
                        temp[0] = int(temp[0])
                        temp[1] = int(temp[1])
                    else:
                        raise Exception

                    result = not result

                except Exception as e:
                    QMessageBox.warning(Setting.setting, '경고메시지', '값을 잘못입력하였습니다.\n다시 입력하세요.', QMessageBox.Yes)
                    print 'error > ', e

                if result:
                    self.ui.btn_chuck_set.setText('척 보정값 설정')
                    value.set_chuck_scale(temp)
                    passNumber = 4

            elif command == 'btn_laser_set':
                try:
                    temp = self.ui.setting_com.text()
                    temp = temp.split(', ')

                    if len(temp) == 4:
                        temp[0] = int(temp[0])
                        temp[1] = int(temp[1])
                        temp[2] = int(temp[2])
                        temp[3] = int(temp[3])
                    else:
                        raise Exception

                    result = not result

                except Exception as e:
                    QMessageBox.warning(Setting.setting, '경고메시지', '값을 잘못입력하였습니다.\n다시 입력하세요.', QMessageBox.Yes)
                    print 'error > ', e

                if result:
                    self.ui.btn_laser_set.setText('레이저 사이 간격 설정')
                    value.set_laser(temp)
                    passNumber = 5

            if result:
                for i in range(len(Setting.setting.btnList)):
                    if i != passNumber:
                        Setting.setting.btnList[i].setEnabled(True)

                self.ui.setting_com.setPlaceholderText('')
                self.ui.setting_com.setEnabled(False)
                self.toggle = not self.toggle
                self.ui.setting_info.setText('척 기본값 : %s\n프레임 길이 : %d\n좌표계 보정값 : %s\n척 보정값 : %s\n레이저 사이 간격 : %s'
                                             % (value.get_chuck(), value.get_frame(), value.get_coor(),
                                                value.get_chuck_scale(), value.get_laser()))

            self.ui.setting_com.setText('')

            print 'setting 으아아악 > ', value.get_value()




