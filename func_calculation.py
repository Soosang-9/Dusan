# -*- coding: utf-8 -*-
import numpy as np
import numpy.linalg as la
import math

import value


class Calculation:
    def __init__(self):

        self.lHeight = value.get_laser()
        print 'ㄹ에저ㅓ 계측기의 높이값 : ', self.lHeight

    def get_laser_location(self):
        return self.lHeight[:]

    def func_calculation(self, laserLength):

        self.tLength = value.get_frame()
        self.lHeight = value.get_laser()
        print 'tLength > ', self.tLength
        # 레이저 계측기의 높이값
        print 'lHeight > ', self.lHeight

        laser_UI = []

        lR = [round(laserLength[0]), round(laserLength[1]), round(laserLength[2]), round(laserLength[3])]
        lL = [round(laserLength[4]), round(laserLength[5]), round(laserLength[6]), round(laserLength[7])]

        pipeChordBisect = [(self.tLength - (lR[0] + lL[0])), (self.tLength - (lR[1] + lL[1])), (self.tLength - (lR[2] + lL[2])),
                           (self.tLength - (lR[3] + lL[3]))]

        # print('파이프의 pipeChordBisect : ', pipeChordBisect[0], pipeChordBisect[1], pipeChordBisect[2], pipeChordBisect[3])

        pipe_pointXY = []

        for i in range(0, 4):
            # 현의 길이가 0이면 계산에서 제외
            if pipeChordBisect[i] > 0:
                pipe_pointXY.append([self.tLength / 2 - lR[i], self.lHeight[i]])
                pipe_pointXY.append([lL[i] - self.tLength / 2, self.lHeight[i]])
                laser_UI.append(1)
            else:
                laser_UI.append(0)

        if laserLength[-2] != 0:
            laser_UI.append(1)
        else:
            laser_UI.append(0)

        if laserLength[-1] != 0:
            laser_UI.append(1)
        else:
            laser_UI.append(0)


        # print('유효한 원 위의 측정 좌표 : ', pipe_pointXY)

        # 유효한 좌표만 마구마구 집어 넣어서
        # 헤론의 공식을 응용하여 외접원의 공식 적용 -> 반지름 나온다
        # 문제는 레이저 계측기가 1mm 이하 측정을 못해서 오차가 생기는데
        # 이 문제를 해결하기 위해 최소제곱법을 적용... 즉 이용할 수 있는 모든 측정된 좌표를 이용하자... 어렵다..젠장

        pipeX = pipeY = pipeR = 0

        if pipe_pointXY.__len__() >= 3:
            pipe_pointXYnp = np.matrix(pipe_pointXY)
            avgA = 0
            avgB = 0
            uu = 0
            vv = 0
            uv = 0
            uuu = 0
            vvv = 0
            uvv = 0
            vuu = 0

            for i in pipe_pointXYnp:
                avgA += i[0, 0]
                avgB += i[0, 1]

            avgA /= len(pipe_pointXYnp)
            avgB /= len(pipe_pointXYnp)

            for i in pipe_pointXYnp:
                i[0, 0] -= avgA
                i[0, 1] -= avgB

            for i in pipe_pointXYnp:
                uu += i[0, 0] * i[0, 0]
                vv += i[0, 1] * i[0, 1]
                uv += i[0, 0] * i[0, 1]
                uuu += i[0, 0] * i[0, 0] * i[0, 0]
                vvv += i[0, 1] * i[0, 1] * i[0, 1]
                uvv += i[0, 0] * i[0, 1] * i[0, 1]
                vuu += i[0, 1] * i[0, 0] * i[0, 0]

            U = np.matrix([[uu, uv], [uv, vv]])
            UU = np.matrix([[0.5 * (uuu + uvv)], [0.5 * (vvv + vuu)]])
            S = la.inv(U).dot(UU)

            pipeX = np.squeeze(np.asarray(S[0] + avgA))
            pipeY = np.squeeze(np.asarray(S[1] + avgB))
            pipeR = 0

            # 도출될 x,y에서 측정된 모든 좌표로의 Euclidean Distance의 평균.. 오차율 줄이려고 쑈를한다...
            for i in range(0, pipe_pointXY.__len__()):
                pipeR += math.sqrt((pipe_pointXY[i][0] - pipeX) ** 2 + (pipe_pointXY[i][1] - pipeY) ** 2)
            pipeR = pipeR / pipe_pointXY.__len__()

        return pipeX, pipeY, pipeR, laser_UI