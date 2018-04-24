# -*- coding:utf-8 -*-

import pickle


# 기본 셋팅 값
def set_value():

    global Setvalue
    global Laser
    global Chuck
    global Chuck_scale
    global Coordination
    global Frame

    # 파일 가져와서 저장하기, 만약에 파일이 없으면 생성하기 None 으로 지정하고.

    Setvalue = read_file()
    print 'set value len > ', Setvalue.__len__()

    if Setvalue.__len__() == 5:
        print 'Set value len is 4'
        # 레이저 사이의 거리.
        Laser = Setvalue[0]
        # 척 기본값 [ y, z ].
        Chuck = Setvalue[1]
        # 척 보정값 [ y, z ].
        Chuck_scale = Setvalue[2]
        # 좌표계 보정값 [ y, z ].
        Coordination = Setvalue[3]
        # 프레임 길이.
        Frame = Setvalue[4]

def get_value():
    return Setvalue[:]


def get_chuck():
    return Chuck[:]


def get_chuck_scale():
    return Chuck_scale[:]


def get_laser():
    return Laser[:]


def get_coor():
    return Coordination[:]


def get_frame():
    return Frame


def read_file():
    f = None
    try:
        f = open('value.txt', 'rb')
    except Exception as e:
        print 'read_file error > ', e
        f = open('value.txt', 'wb')
        temp = [
            [83, 43, -3, -37],
            [],
            [0, 0],
            [6, -23],
            1674
        ]
        pickle.dump(temp, f)
        f.close()
        f = open('value.txt', 'rb')
    finally:
        Setvalue = pickle.load(f)
        f.close()
        return Setvalue


def save_value():
    Setvalue[0] = Laser
    Setvalue[1] = Chuck
    Setvalue[2] = Chuck_scale
    Setvalue[3] = Coordination
    Setvalue[4] = Frame

    try:
        f = open('value.txt', 'wb')
        pickle.dump(Setvalue, f)
        f.close()
    except Exception as e:
        print 'error > ', e, '파일 저장에 오류가 있습니다.'


def set_laser(laser):
    if type(laser) == list:
        global Laser
        Laser = laser
        save_value()


def set_chuck(chuck):
    if type(chuck) == list:
        global Chuck
        Chuck = chuck
        save_value()


def set_chuck_scale(scale):
    if type(scale) == list:
        global Chuck_scale
        Chuck_scale = scale
        save_value()


def set_coordination(coor):
    if type(coor) == list:
        global Coordination
        Coordination = coor
        save_value()


def set_frame(frame):
    if type(frame) == int:
        global Frame
        Frame = frame
        save_value()

