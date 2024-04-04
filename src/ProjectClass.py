
from tools import create_folder

from pathlib import Path

class ProjectClass():
    """
    Properties:
        project_name: the name of the project
        home: the folder containing the project
        folder: the project path
    """


    userhome = "/Users/sebastiengalvagno/"
    piqv="piqv/plankton/zooscan_monitoring/"
    piqvhome=userhome+piqv

    def __init__(self,project_name) -> None:
        self.project_name = project_name
        # if project_name:
        self.folder = Path(self.piqvhome, project_name)
        self.home = Path(self.piqvhome)
        self.raw = Path(self.folder, "Zooscan_scan", "_raw")
        self.work = Path(self.folder, "Zooscan_scan", "_work")
        self.tempFolder = Path(self.folder, "temp")
        self._createFolders()

    def _createFolders(self):
        create_folder(self.home)
        create_folder(self.work)
        create_folder(self.raw)
        create_folder(self.tempFolder)

   
    def homeFolder(self):
        return self.home.absolute().as_posix()

    def workFolder(self):
        return self.work.absolute().as_posix()

    def rawFolder(self):
        return self.raw.absolute().as_posix()

    def tempFolder(self):
        return self.tempFolder.absolute().as_posix()


