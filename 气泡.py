import maya.cmds as cmds
from pymel import  *


class jbface_popo(object):
    def create(self,*args):
        myem = emitter(dx=1, dy=0, dz=0, sp=15.0, pos=(1, 1, 1), type='dir', speedRandom=10, rate=0.7, n='myEmitter')

        mypa = particle(n='emittedParticles', c=0.5)
        mypa[0].particleRenderType.set(4)

        connectDynamic(mypa[0], em=myem)

        pname = 'emittedParticles'
        vname = 'zhongli'

        cmds.select(cl=True)
        mygr = gravity(name=vname, dy=1.0)

        cmds.connectAttr('%s.outputForce[0]' % vname, '%sShape.inputForce[0]' % pname)
        cmds.connectAttr('%sShape.fieldData' % pname, '%s.inputData[0]' % vname)
        cmds.connectAttr('%sShape.ppFieldData[0]' % pname, '%s.inputPPData[0]' % vname)





popo = jbface_popo()
popo.create()
