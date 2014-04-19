import maya.cmds as cmds
import unittest

def thisDirectory():
    path_to_file = cmds.pluginInfo("cop", query=True, path=True)
    path_components = path_to_file.split("/")
    path_components.pop()
    return "/".join(path_components)

def Cop():
    print "--- Running Cop ---"
    runner = unittest.TextTestRunner()
    loader = unittest.TestLoader()
    suite = loader.discover(thisDirectory() + "/test")
    runner.run(suite)

def unload():
    cmds.unloadPlugin()

def initializePlugin(maya_object):
    print "Cop Loaded."

def uninitializePlugin(maya_object):
    print "Cop Unloaded"
