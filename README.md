# RealSense Python Script

Uses realsense sdk with virtual environment

## Instructions

1. Clone the repository and cd into the root folder pythonProject.
2. If you are using pycharm create a virtual environment. 
 To create virtual environment simply follow:
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
3. To add the interpreter to an existing virtual environment
Follow the link below to see how you can do it in pycharm 
https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter
4. pip install -r reuirements.txt 

## usage

To save the point cloud data into a ply file simply run python SaveFilesToPly.py

This will save a saved.ply file with the point cloud data. A sample is in the repository which can be opened in blender directly. 

#Note: make sure that your virtual environment interpreter is python 3.9 realsense sdk does not support higher python versions. 


