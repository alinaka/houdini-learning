# "C:\Program Files\Side Effects Software\Houdini 18.5.759\bin\hython2.7.exe" "C:\Program Files\Side Effects Software\Houdini 18.5.759\bin\usdview" test_layout.usd
import hou
from pxr import Usd

stage = Usd.Stage.Open("test_layout.usd")

for prim in stage.Traverse():
    if prim.GetTypeName() in ["Material", "Shader"]:
        print(prim.GetPath())
        for attr in prim.GetAttributes():
            print("\t" + attr.GetName())

prim = stage.GetPrimAtPath("/layout/sceneimport1/obj/matnet1/earth")
albedomult = prim.GetAttribute("albedomult")
print(albedomult.Get(1.0))

node = hou.node("/stage/sublayer1")
stage = node.stage()
for prim in stage.Traverse():
    if prim.GetTypeName() in ["Material", "Shader"]:
        print(prim.GetPath())
        for attr in prim.GetAttributes():
            print("\t" + attr.GetName())
