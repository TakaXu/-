import maya.cmds as cmds
import random
from pymel.core import *
import math

pnumber = 1000#粒子数目
long = 50#粒子长宽
width = 1#粒子高
eel = []
name = 'ship'
vortname = 'vortexField1'

agle = 22.5#角度
fortime = 180//agle#数量-1
abgle = (math.pi/180)* agle
kkk = int(fortime)-1




        
    

def create(pname):

    for i in range(pnumber):
        eel.append ((random.uniform(-1,1),random.uniform(-2,2),random.uniform(-1*long,long)))
    #for i in range(pnumber):
        #eel.append ((random.uniform(-1*long,long),random.uniform(-2,2),random.uniform(-1,1)))
    for i in range(kkk):
        for i in range(pnumber):
            cos = math.cos(abgle * i)
            sin = math.sin(abgle * i)
            eel.append((eel[i][0]*cos+eel[i][2]*sin,eel[i][1],eel[i][2]*cos-eel[i][0]*sin))
           
         
    
    cmds.particle(jbp = eel,n = name,c = 1)

    cmds.setAttr("%sShape.particleRenderType"%name,4)

    


def link (pname,vname):
    cmds.vortex(n = vortname,pos = (0,0,0),m = 5,ay = 1,att = 1,mxd = -1,vsw = 360,tsr = 0.5)
    cmds.connectAttr('%s.outputForce[0]'%vname,'%sShape.inputForce[0]'%pname)
    cmds.connectAttr('%sShape.fieldData'%pname,'%s.inputData[0]'%vname)
    cmds.connectAttr('%sShape.ppFieldData[0]'%pname,'%s.inputPPData[0]'%vname)

    
create(name)

       
link(name,vortname)

