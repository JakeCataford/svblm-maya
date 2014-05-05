import maya.cmds as cmds
import unittest

"""
Cop - Unit Testing Wrapper for Maya Scenes

What:

We love testing. It lets us have confidence in what we are shipping without
having to get other reviewers to look into it. This module wraps a unit testing
framework around maya, letting us identify simple common problems in an automated
way.

Here are some examples of things Cop could prevent:

- Huge texture files (for a small scale object)
- Polycount problems (way too many polygons)
- Geometry problems (non-manifold Geometry, lamina faces)
- Draw call hell (too many materials, too many meshes)

All of these have simple solutions, but are easy to miss when exporting. Cop
yells at you when your tests fail, so nobody will have these problems again.

How:

Add tests to cop/test/. They have to start with the word "test_" and contain a
class that extends unittest.TestCase. all of the functions of that class will be
run so make sure they all assert something (failing your tests if things aren't)
right.

"""

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
    return runner.run(suite)

def initializePlugin(maya_object):
    print "Cop Loaded."

def uninitializePlugin(maya_object):
    print "Cop Unloaded"
