import unittest

def Cop():
    print "--- Running Cop... ---\n\n\n"
    runner = unittest.TextTestRunner()
    loader = unittest.TestLoader()
    suite = loader.discover("./test")
    runner.run(suite)

Cop()
