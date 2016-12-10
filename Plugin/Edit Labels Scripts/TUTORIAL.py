# This is a Python script. Before running it, make sure that Python
# interpreter is available in system 'PATH' variable.
#
# Scripts can be added/deleted/edited in following directory:
# <LabVIEW>\resource\dialog\QuickDrop\plugins\Edit Label Scripts
#
# 'labels' variable is predefined and contains list of currently selected labels.
# You should iterate through this list printing new name for each label.
# Example below turns all the letters in each label to upper case.
    
for label in labels:
    print(label.upper())
