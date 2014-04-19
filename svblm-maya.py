import maya.cmds as cmds
import os
import cop.cop as cop

def thisDirectory():
    path_to_file = cmds.pluginInfo("svblm-maya", query=True, path=True)
    path_components = path_to_file.split("/")
    path_components.pop()
    return "/".join(path_components)

def initializePlugin(maya):
    print "-----------------------"
    print "SVBLM Maya Suite v0.0.1"
    print "-----------------------"
    print "loading cop:"
    cmds.loadPlugin(thisDirectory() + "/cop/cop.py")


def uninitializePlugin(maya_object):
    print "Unloading SVBLM maya suite:"
    print "---------------------------"
    print "unloading cop:"
    cop.unload()
