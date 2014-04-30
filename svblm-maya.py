import maya.cmds as cmds
import os
import cop.cop as cop
import shipper.shipper as shipper

def thisDirectory():
    path_to_file = cmds.pluginInfo("svblm-maya", query=True, path=True)
    path_components = path_to_file.split("/")
    path_components.pop()
    return "/".join(path_components)

def initializePlugin(maya):
    print "-----------------------"
    print "SVBLM Maya Suite v0.0.1"
    print "-----------------------"
    print "loading cop..."
    cmds.loadPlugin(thisDirectory() + "/cop/cop.py")
    print "Loading shipper..."
    cmds.loadPlugin(thisDirectory() + "/shipper/shipper.py")


def uninitializePlugin(maya_object):
    print "---------------------------"
    print "Unloading SVBLM maya suite:"
    print "---------------------------"
    print "unloading cop..."
    cmds.unloadPlugin('cop')
    print "unloading shipper..."
    cmds.unloadPlugin('shipper')
