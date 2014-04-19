import unittest
import maya.cmds as cmds

class TestPolyCount(unittest.TestCase):
    def testScenePolyCount(self):
        """ Test that the scene does not exceed a million polygons """
        count = 0
        count += int(cmds.polyEvaluate(cmds.ls(), triangle=True))
        self.assertTrue(count < 1000000)
