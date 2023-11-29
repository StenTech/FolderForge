from os.path import dirname, join

try:
	from services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)
	from utils.styles import Color, Style
	from models import File
except:
	from .services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)
	from .utils.styles import Color, Style
	from .models import File


class FolderForge:
	def __init__(self, description_file_path: str):
		self.description_file_path = description_file_path
		description = FolderForgeService.readJSON(description_file_path)
		self.path = description.get("path", "")
		self.tree = description.get("tree", [])
		
	def forge(self, path: str=""):
		"""
		Create the folder structure
		path: the path to the root directory in which the folder structure will be created, 
		it can be empty, a simple name or a path
		"""

		if path=="":
			path = self.path
			
		FileService.createDirectoryWithSubDirs(path)

		with ChangeDirectoryContext(path):	
			for node in FolderForgeService.searchPaths(self.tree):
				type = node["type"]
				path = node["path"]
				content = node.get("content")
				
				print(Color.primary("[FOLDERFORGE]: Creating " + Style.bold(type)) + Color.primary(" " + path), end="")

				if type == "file":
					print(f" (from {content['type'].upper()})")
				else:
					print()

				if type == "file":
					file: File = FileService.createFile(path)

					# manage file content
					if content:
						file.putContent(
							content_type=content["type"],
							content_value=content["value"],
							description_file_path=self.description_file_path
						)
				elif type == "directory":
					FileService.createDirectory(path)
				else:
					raise Exception("Unknown node type: " + type)
			
			return self
