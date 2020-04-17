import os
import bidict
"""

"""

def getFilePathList(rootDir):
    filePath_list = []
    for walk in os.walk(rootDir):
        part_filePath_list = [os.path.join(walk[0], file) for file in walk[2]]
        filePath_list.extend(part_filePath_list)
    return filePath_list
def getFolderPathList(rootDir):
    FolderPath_list = []
    for walk in os.walk(rootDir):
        FolderPath_list.append(walk[0])
    FolderPath_list.remove(rootDir)
    return FolderPath_list