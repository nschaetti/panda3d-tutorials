
# Loading a model
myNodePath = loader.loadModel("path/to/models/myModel.egg")

# Reparenting nodes and models
myModel.reparentTo(render)
myModel.detachNode()
myModel.removeNode()

dummyNode = render.attachNewNode("Dummy Node Name")
myModel.reparentTo(dummyNode)
myOtherModel.reparentTo(dummyNode)

myModel.wrtReparentTo(newParent)

# State change cheat sheet
myNodePath.setPos(X, Y, Z)
myNodePath.setHpr(Yaw, Pitch, Roll)

myNodePath.setScale(S)

myNodePath.setX(X)
myNodePath.setY(Y)
myNodePath.setZ(Z)
myNodePath.setH(H)
myNodePath.setP(P)
myNodePath.setR(R)
myNodePath.setSx(SX)
myNodePath.setSy(SY)
myNodePath.setSz(SZ)

myNodePath.setPosHprScale(X, Y, Z, H, P, R, SX, SY, SZ)

myNodePath.getPos()
myNodePath.getX()
myNodePath.getY()
myNodePath.getZ()

myNodePath.setTag("Key", "value")

myNodePath.setPos(otherNodePath, X, Y, Z)
myNodePath.getPos(otherNodePath)

# Move myNodePath 3 units forward in the x
myNodePath.setPos(myNodePath, 3, 0, 0)

myNodePath.lookAt(otherObject)

myNodePath.setColor(R, G, B, A)

myNodePath.clearColor()

myNodePath.setTransparency(TransparencyAttrib.MAlpha)

myNodePath.setColorScale(R, G, B, A)

myNodePath.setAlphaScale(SA)

myNodePath.hide()
myNodePath.show()

camera1.node().setCameraMask(BitMask32.bit(0))
camera2.node().setCameraMask(BitMask32.bit(1))
myNodePath.hide(BitMask32.bit(0))
myNodePath.show(BitMask32.bit(1))
# Now myNodePath will only be shown on camera2...

myNodePath.place()

myNodePath.ls()

myNodePath.find("<Path>")
myNodePath.findAllMatches("<Path>")

myNodePath.find("house/door")

myNodePath.find("**/red*")

shipNP.findAllMatches("**/=type=weaponMount")

for child in myNodePath.getChildren():
  print child


