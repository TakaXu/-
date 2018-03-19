import maya.cmds as cmds
import os
import random
import math


class AR_poly(object):
    use = None

    def showUI(cls, uifile):
        win = cls(uifile)
        win.create()
        return win

    def __init__(self, filepath):
        AR_poly.use = self
        self.window = '0000'
        self.uifile = filepath

    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        self.window = cmds.loadUI(uiFile=self.uifile, verbose=True)
        cmds.showWindow(self.window)


class tplink(object):
    use = None

    def __init__(self, time, pname, long, kkk, pnumber,  shipname='ship'):
        self.time = time
        self.pname = pname
        self.long = long
        self.kkk = kkk
        self.pnumber = pnumber
        #self.abgle = abgle
        self.name = shipname
        self.eel = []
        tplink.use = self

    def run(self):
        cmds.polyCube(h=self.time)

    def create(self, *args):
        abgle = None
        try:
            path = '|'.join(['box','getagle'])
            abgle = float(cmds.textField(path,q=True,text=True))
        except:raise 


        for i in range(self.pnumber):
            self.eel.append((random.uniform(-1, 1), random.uniform(-2, 2), random.uniform(-1 * self.long, self.long)))
        for i in range(self.kkk):
            for i in range(self.pnumber):
                cos = math.cos(abgle * i)
                sin = math.sin(abgle * i)
                self.eel.append((self.eel[i][0] * cos + self.eel[i][2] * sin, self.eel[i][1],
                                 self.eel[i][2] * cos - self.eel[i][0] * sin))

        cmds.particle(jbp=self.eel, n=self.name, c=1)

        cmds.setAttr("%sShape.particleRenderType" % self.name, 4)


opcc = tplink(time=3, pname='fut', long=20, kkk=4, pnumber=500)
win = AR_poly(os.path.join(os.getenv('HOME'), 'poly.ui'))
win.create()
