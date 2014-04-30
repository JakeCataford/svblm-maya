import maya.cmds as cmds
import os
import file_manager
"""
Svblm Shipper - A 3D Asset Pipeline

What:

Shipper is a way to manage reviewing and shipping assets to production.
It focuses on integrating tightly with maya and dropbox to ensure that
files remain well organized and easy to navigate when they reach production.
The local->stage->production approach means that assets get reviewed before
they hit production, ensuring high quality

How:

Shipper integrates with a local dropbox install. A shared directory
is set as the shipper root, from there, shipper ensures that two
subfolders exist, stage and production. stage is where we store candidates,
any models that need to be reviewed before they are available in unity.

The format for storing is like this:
stage/
    model_name/
        model.fbx
        model.fbm
        meta.json

meta.json is the metadata file, it contains the real name of the file and
any useful other information. (grouping, tags, notes). We will build an
asset pallette plugin in unity to filter these assets by tag and view them
in a logical way, similar to the UDK content browser.

There is a browser for all staged files in this plugin, where you can open
staged files and ship them to production. production is just another folder
with identical structure to stage that we use to store production ready assets.

"""


def initializePlugin(maya_object):
    if cmds.optionVar(exists="shipper_dir") == 0:
        show_setup_window()
    else:
        print cmds.optionVar(q="shipper_dir")

def uninitializePlugin(maya_object):
    return True

def show_setup_window():
    print "No configuration found. Prompting to set a shipper directory."
    fileName = cmds.fileDialog2(caption="Set the shipper directory", fileMode=3, okCaption="Set Directory")
    cmds.optionVar(sv=("shipper_dir", fileName[0]))

def ship_to_stage():
    raise NotImplementedError()

def complete_ship_to_stage():
    raise NotImplementedError()
    # Check for collisions, is there any object with the same names? (Overwrite?)
    # Create folder, export FBX into folder.
    # Write metadata file (.ship? yaml?)

def open_stage():
    if(cmds.window("svblm shipper stage", exists=True)):
        cmds.deleteUI("svblm shipper stage")

    cmds.window("svblm shipper stage", title="SVBLM Shipper: Stage", width=500)
    file_manager.all_staged_folders()

def view(assetName):
    raise NotImplementedError()
    # New maya file, import .fbx from asset. (Setup global vars to populate name fields for shipToStage()?)

def ship(assetName):
    # Check for collisions, confirm update?
    raise NotImplementedError()
    # Ship to production asset folder. This folder will be linked to in unity.
    # write metadata file.

