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

# motion_vectors

box = matnet.createNetworkBox()
box.setComment("P_world")
box.setColor(hou.Color((1.0, 0, 0)))

constant0 = matnet.createNode("constant")
constant0.parm("consttype").set("float")
constant0.parm("floatdef").set("1")
constant0.parm("constname").set("time0")
box.addItem(constant0)

constant1 = matnet.createNode("constant")
constant1.parm("consttype").set("float")
constant1.parm("floatdef").set("0")
constant1.parm("constname").set("time1")
constant1.move((0, -1.5))
box.addItem(constant1)

getblurP0 = matnet.createNode("getblurP")
getblurP0.move((2.5, 0))
getblurP0.setNamedInput("time", constant0, "time0")
box.addItem(getblurP0)

getblurP1 = matnet.createNode("getblurP")
getblurP1.move((2.5, -1.5))
getblurP1.setNamedInput("time", constant1, "time1")
box.addItem(getblurP1)

transform0 = matnet.createNode("transform")
transform0.parm("fromspace").set("space:camera")
transform0.parm("tospace").set("space:ndc")
transform0.move((5, 0))
transform0.setNamedInput("from", getblurP0, "blurP")
box.addItem(transform0)

transform1 = matnet.createNode("transform")
transform1.parm("fromspace").set("space:camera")
transform1.parm("tospace").set("space:ndc")
transform1.move((5, -1.5))
transform1.setNamedInput("from", getblurP1, "blurP")
box.addItem(transform1)

subtract0 = matnet.createNode("subtract")
subtract0.move((7.5, -0.75))
subtract0.setNamedInput("input1", transform0, "to")
subtract0.setNamedInput("input2", transform1, "to")
box.addItem(subtract0)

vecfloat0 = matnet.createNode("vectofloat")
vecfloat0.move((10, -0.75))
vecfloat0.setNamedInput("vec", subtract0, "diff")
box.addItem(vecfloat0)

floattovec0 = matnet.createNode("floattovec")
floattovec0.move((12.5, -0.75))
floattovec0.setNamedInput("fval1", vecfloat0, "fval2")
floattovec0.setNamedInput("fval2", vecfloat0, "fval1")
floattovec0.setNamedInput("fval3", vecfloat0, "fval3")
box.addItem(floattovec0)

renderstate0 = matnet.createNode("renderstate")
renderstate0.parm("signature").set("v")
renderstate0.parm("var").set("image:resolution")
renderstate0.move((12.5, -2.25))
box.addItem(renderstate0)

multiply0 = matnet.createNode("multiply")
multiply0.move((15, -1.5))
multiply0.setNamedInput("input1", floattovec0, "vec")
multiply0.setNamedInput("input2", renderstate0, "val")
box.addItem(multiply0)

bind0 = matnet.createNode("bind")
bind0.parm("parmname").set("motion_vector")
bind0.parm("parmtype").set("vector")
bind0.parm("overridetype").set(True)
bind0.parm("vectordef1").set("-1")
bind0.parm("useasparmdefiner").set(1)
bind0.parm("exportparm").set(1)
bind0.move((17.5, -1.5))
bind0.setNamedInput("input", multiply0, "product")
box.addItem(bind0)

box.fitAroundContents()
