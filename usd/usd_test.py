from pxr import Usd

stage = Usd.Stage.Open("test_layout.usd")

for prim in stage.Traverse():
    if prim.GetTypeName() in ["Material", "Shader"]:
        print(prim.GetPath())
        for attr in prim.GetAttributes():
            print("\t" + attr.GetName())
