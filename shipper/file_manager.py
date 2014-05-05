import maya.cmds as cmds
import os

def all_staged_folders():
    all_folders = []
    for dir in os.walk(shipper_stage_root()):
        all_folders.append(dir[0])
    return all_folders

def shipper_stage_root():
    root = str(shipper_root()) + "/stage/"
    if os.path.isdir(root):
        return root
    else:
        os.mkdir(root)

def shipper_root():
    if cmds.optionVar(exists="shipper_dir") == 0:
        raise "Shipper directory not set!"
    else:
        return cmds.optionVar(q="shipper_dir")
