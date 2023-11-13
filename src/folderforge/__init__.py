from os.path import dirname, join


try:
	# import services
	from services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)
	# import Color
	from utils.Class import Color
except:
	# import services
	from .services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)
	# import Color
	from .utils.Class import Color


class FolderForge:
	def __init__(self, description_file_path: str):
		self.description_file_path = description_file_path
		description = FolderForgeService.readJSON(description_file_path)
		self.path = description.get("path", "")
		self.tree = description.get("tree", [])
		
	def forge(self, _path: str=""):
		"""
		Create the folder structure
		_path: the path to the root directory in which the folder structure will be created, 
		it can be empty, a simple name or a path
		"""
		if _path=="":
			_path = self.path
			
		FileService.createDirectoryWithSubDirs(_path)

		with ChangeDirectoryContext(_path):	
			for node in FolderForgeService.searchPaths(self.tree):
				type = node["type"]
				path = node["path"]
				
				print(Color.primary("Creating " + type + " " + path))

				if type == "file":
					FileService.createFile(path)
				elif type == "directory":
					FileService.createDirectory(path)
				else:
					raise Exception("Unknown node type: " + type)
			
			return self
