import os
import hou

cur_desktop = hou.ui.curDesktop()
scene_viewer = hou.paneTabType.SceneViewer
scene = cur_desktop.paneTabOfType(scene_viewer)
scene.flipbookSettings().stash()
flip_book_options = scene.flipbookSettings()
hipPath = os.path.dirname(hou.hipFile.path())
hipName = hou.hipFile.basename()
splitName = hipName.split('.')
name = splitName[0]
filename = hipPath + '/flipbook/' + name + ".$F.exr"

start_frame = hou.hscriptExpression("$RFSTART")
end_frame = hou.hscriptExpression("$RFEND")

flip_book_options.output(filename) # Provide flipbook full path with padding.
flip_book_options.frameRange((start_frame, end_frame)) # Enter Frame Range Here in x & y
flip_book_options.useResolution(1)
flip_book_options.resolution((1080, 720)) # Based on your camera resolution
scene.flipbook(scene.curViewport(), flip_book_options)
