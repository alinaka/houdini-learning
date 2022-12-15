import hou

root = hou.node("/obj")
matnet = root.createNode("matnet", "UTILITY_PRESETS")

# P_world

box = matnet.createNetworkBox()
box.setComment("P_world")
box.setColor(hou.Color((1.0, 0, 0)))

global1 = matnet.createNode("global")
global1.parm("contexttype").set("surface")
global1.parm("usemenu").set(True)
global1.parm("varname").set("P")
global1.setColor(hou.Color((255, 0, 0)))
box.addItem(global1)

transform1 = matnet.createNode("transform")
transform1.parm("tospace").set("space:world")
transform1.setNamedInput("from", global1, "P")
transform1.setColor(hou.Color((255, 0, 0)))
transform1.move((3, 0))
box.addItem(transform1)

parm1 = matnet.createNode("parameter")
parm1.parm("parmname").set("P_world")
parm1.parm("parmlabel").set("Parameter")
parm1.parm("parmtype").set("float3")
parm1.parm("exportparm").set(1)
parm1.setInput(0, transform1)
parm1.setColor(hou.Color((255, 0, 0)))
parm1.move((6, 0))
box.addItem(parm1)

bind1 = matnet.createNode("bind")
bind1.parm("parmname").set("P_world")
bind1.parm("parmtype").set("vector")
bind1.parm("exportparm").set(1)
bind1.setInput(0, parm1)
bind1.move((9, 0))
box.addItem(bind1)

box.fitAroundContents()

# P_object

box = matnet.createNetworkBox()
box.setComment("P_object")
box.setColor(hou.Color((1.0, 0, 0)))
box.move((0, 3))

global1 = matnet.createNode("global")
global1.parm("contexttype").set("surface")
global1.parm("usemenu").set(True)
global1.parm("varname").set("P")
global1.setColor(hou.Color((255, 0, 0)))
global1.move((0, 4))
box.addItem(global1)

vectofloat = global1.createOutputNode("vectofloat")
box.addItem(vectofloat)
floattovec = vectofloat.createOutputNode("floattovec")
floattovec.move((3, 0))
box.addItem(floattovec)

transform1 = floattovec.createOutputNode("transform")
transform1.setColor(hou.Color((255, 0, 0)))
transform1.move((6, 0))
box.addItem(transform1)

bind1 = matnet.createNode("bind")
bind1.parm("parmname").set("P_object")
bind1.parm("parmtype").set("vector")
bind1.parm("exportparm").set(1)
bind1.setInput(0, transform1)
bind1.move((11, 4))
box.addItem(bind1)

box.fitAroundContents()


# P_ref

box = matnet.createNetworkBox()
box.setComment("P_ref")
box.setColor(hou.Color((1.0, 0, 0)))
box.move((0, 6))

global5 = matnet.createNode("global")
global5.parm("contexttype").set("surface")
global5.parm("usemenu").set(True)
global5.parm("varname").set("P")
global5.setColor(hou.Color((255, 0, 0)))
global5.move((0, 7))
box.addItem(global5)

transform4 = matnet.createNode("transform")
transform4.parm("tospace").set("space:camera")
transform4.setColor(hou.Color((255, 0, 0)))
transform4.setNamedInput("from", global5, "P")
transform4.move((2, 7))
box.addItem(transform4)

parm3 = matnet.createNode("parameter")
parm3.parm("parmname").set("P_ref")
parm3.parm("parmlabel").set("Parameter")
parm3.parm("parmtype").set("float3")
parm3.parm("exportparm").set(1)
parm3.setNamedInput("input", transform4, "to")
parm3.setColor(hou.Color((255, 0, 0)))
parm3.move((4, 7))
box.addItem(parm3)

box.fitAroundContents()
