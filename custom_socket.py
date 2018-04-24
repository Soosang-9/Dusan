# -*- coding:utf-8 -*-

from socket import *
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

import time

class Socket():
    def __init__(self, main, img_list):
        QThread.__init__(self)
        self.__HOST = ''
        self.__PORT1 = 5556

        self.__ADDR1 = (self.__HOST, self.__PORT1)

        self.addr = [self.__ADDR1, self.__ADDR2, self.__ADDR3]

        self.client = [None, None, None]
        self.img_list = img_list

        self.dialog = None

    def connect(self, dialog):
        self.dialog = dialog
        self.closet_socket()
        for i in range(len(self.addr)):
            self.client[i] = self.connect_acting(self.addr[i], i)

    def connect_acting(self, addr, i):
        client = None
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            sock.bind(addr)
            sock.listen(5)
            client, addr = sock.accept()
            sock.close()

        except Exception as e:
            print 'error > ', e
            print '%d connect_acting error' % i
            return client

        if client is not None:
            if i < 3:
                self.img_list[i].setStyleSheet('font: bold 11pt; color:rgb(0, 170, 0);')
                self.img_list[i].setText('연결 완료')

        return client

    def back_message(self, chuck, send_message):
        result = self.message_acting(2, send_message)
        if result is False:
            return 'error'

        self.message_recving(2)
        self.message_to_data(chuck, 2)

        return True

    def chuck_message(self, send_message):
        rtnv = []
        result = self.message_acting(2, send_message)
        if result is False:
            return 'error'

        self.data[2] = None
        self.message_recving(2)
        self.message_to_data(rtnv, 2)

        return rtnv

    def locate_message(self, send_message):
        for i in range(len(self.client)):
            result = self.message_acting(i, send_message)
            if result is False:
                return False

        return True

    def message(self, send_message):
        rtnv = []
        self.message_start_time = time.time()
        for i in range(len(self.client)):
            result = self.message_acting(i, send_message)
            if result is False:
                return 'error'

        self.data = [None, None, None]
        for i in range(len(self.client)):
            self.message_recving(i)

        if self.data[0] and self.data[1] and self.data[2] is not None:
            for i in range(len(self.client)):
                self.message_to_data(rtnv, i)

            if send_message == '$MEASURE\0':
                self.message_end_time = time.time()
                print '----------------------------------------------------------- 메시지 반환 시간 %s' %(self.message_start_time - self.message_end_time)
                print 'rtnv {0}'.format(rtnv)
                return rtnv

        return send_message

    def message_acting(self,  i,  send_message):
        try:
            self.send_time = time.time()
            self.client[i].send(send_message)
            print '----------------------------------------------------------- send command [ %s ]' % time.ctime()
        except Exception as e:
            result = QMessageBox.question(self.dialog, 'Alter Box', '연결을 다시 시도합니다...', QMessageBox.No | QMessageBox.Yes)
            if result == QMessageBox.Yes:
                self.client[i] = self.connect_acting(self.addr[i], i)
            print 'send error >', e
            return False

        return True

    def message_recving(self, i):
        message = ''
        try:
            message = self.client[i].recv(256)
            self.data[i] = message
            print '----------------------------------------------------------- %d client message return time : %s' %(i, (self.send_time - time.time()))
            if len(message) == 0:
                print '--------------------- message_recving [ if len(message) == 0 ] %s ' % time.ctime()
                raise Exception
        except Exception as e:
            print 'connect error'
            if i < 3:
                print '--------------------- message_recving [ if i<3 ]'
                self.img_list[i].setStyleSheet('font: bold 11pt; color: rgb(255, 32, 47);')
                self.img_list[i].setText('연결 실패')

            # reconnection acting - - - - - - - - - - -
            result = QMessageBox.question(self.dialog, 'Alter Box', '연결을 다시 시도합니다...', QMessageBox.No|QMessageBox.Yes)
            if result == QMessageBox.Yes:
                self.client[i] = self.connect_acting(self.addr[i], i)

            print 'recv error > ', e

    def message_to_data(self, rtnv, i):
        message = self.data[i].split(",")
        print 'split message > ', message
        for j in range(len(message)-1):
            # try:
            #     if message[j][0] == 'E':
            #         return 'error'
            # except Exception as e:
            #     return 'error'
            print 'value.get_frame() = {0}'.format(value.get_frame())
            if i != 1:
                print '--------------------- message_to_data [ if i != 1 ] %s ' % time.ctime()
                try:
                    rtnv.append(float(message[j]) * 1000)
                    print 'rtnv[{0}] = {1}'.format(j, rtnv[j])
                    if rtnv[j] > value.get_frame():
                        print 'if error return'
                        return 'error'
                except Exception as e:
                    print 'Exception error return'
                    return 'error'
            elif i == 1:
                print '--------------------- message_to_data [ elif i == 1 ] %s ' % time.ctime()
                try:
                    rtnv.append(float(message[-2-j]) * 1000)
                    print 'rtnv[{0}] = {1}'.format(j, rtnv[j])
                    if rtnv[j] > value.get_frame():
                        print 'if error return'
                        return 'error'
                except Exception as e:
                    print 'Exception error return'
                    return 'error'

        print 'len len here > ', len(rtnv)
        print '----------------------------------------------------------- %d client message split time : %s' %(i, (self.send_time - time.time()))
        return True

    def closet_socket(self):
        try:
            for i in range(len(self.client)):
                if self.client[i] is not None:
                    print '%d not none' % i
                    self.client[i].close()
                self.img_list[i].setStyleSheet('font: bold 11pt; color: rgb(0, 0, 0);')
                self.img_list[i].setText('연결 종료')
        except Exception as e:
            print 'error > ', e
