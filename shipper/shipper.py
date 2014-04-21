import maya.cmds as cmds
import os

def initializePlugin(maya_object):
    #check if shipper is set...
    if cmds.optionVar(exists="shipper_dir") == 0
        showSetupWindow()

def showSetupWindow():
    window = cmds.window( title="Set Shipper Directory", widthHeight=(200, 55) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.textField( text='Please pick the shipper directory.' )
    cmds.button( label='Close', command=('shipper.shipper.setupCallback()'))
    cmds.setParent( '..' )
    cmds.showWindow( window )

def setupCallback():
    #set optionvar for shipper directory

def shipToStage():
    # Run cop, whine if things are shit.
    # Spawn a window to edit description and name, groupings, tags, categories...
    # On clicking ship in the UI: completeShip()
    # Export and name FBX file, put in appropriate folder

def completeShipToStage():
    # Check for collisions, is there any object with the same names? (Overwrite?)
    # Create folder, export FBX into folder.
    # Write metadata file (.ship? yaml?)

def openStage():
    # Open window that lists staged assets.
    # Pick one and ship it to production with button click. (ship(assetName))
    # Or open an asset to review it with a button click. (view(assetName))
    # wipe a staged asset (delete(assetName))

def view(assetName):
    # New maya file, import .fbx from asset. (Setup global vars to populate name fields for shipToStage()?)

def ship(assetName):
    # Check for collisions, confirm update?
    # Ship to production asset folder. This folder will be linked to in unity.
    # write metadata file.

