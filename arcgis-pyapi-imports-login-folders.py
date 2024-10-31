import os
from arcgis.gis import GIS
from arcgis.mapping import WebMap
from arcgis.features import FeatureLayer, FeatureLayerCollection

gis = GIS("pro", verify_cert = False)

me = gis.users.me

# Name of folder I want
proj = "Sample Folder"

# Get all my folders
folders = me.folders

# Keep track of whether folder found
proj_folder = False

# Rifle messily through folders
for folder in folders:
    
    # If folder found, choose and stuff in variable
    if not folder["title"] == proj:
        continue
        
    proj_folder = folder
    print(f"Selected {me.firstName}'s folder '{proj}'")
    break
        
# Message if folder not found
if not proj_folder:
    print("Folder not found! Check folder name and try again.")
