import hou

matRoot = hou.node("/mat")

builder_node = matRoot.createNode("materialbuilder")
shader_node = builder_node.createNode("principledshader")

output_collect_node = builder_node.node("output_collect")
output_collect_node.setNamedInput("shader1", shader_node, "surface")
