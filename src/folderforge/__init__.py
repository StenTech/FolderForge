from os.path import dirname, join


# import services
try:
	# from folderforge.utils.Class import Color
	from utils.functions import parser
	from services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)
except:
	# from .utils.Class import Color
	from .utils.functions import parser
	from .services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)

class Color:
	success = lambda _str: '\033[92m' + _str + '\033[0m' # green
	danger = lambda _str: '\033[91m' + _str + '\033[0m' # red
	primary = lambda _str: '\033[96m' + _str + '\033[0m' # cyan
	warning = lambda _str: '\033[33m' + _str + '\033[0m' # yellow


class FolderForge:
	def __init__(self, description_file_path: str):
		self.description_file_path = description_file_path
		description = FolderForgeService.readJSON(description_file_path)
		self.path = description.get("path", "")
		self.tree = description.get("tree", [])
		
	def forge(self, _path: str=""):
		"""
		Create the folder structure
		_path: the path to the root directory in which the folder structure will be created, it can be empty, a simple name or a path
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


# the main function for all services testing
def main():
	print()
	args = parser()
	folderForge = FolderForge(args.description_file)

	# Printing the description file path
	print("Description file path: " + Color.primary(args.description_file))
	# Printing the path to the root directory in which the folder structure will be created
	print("Root directory path: " + Color.primary(args.path if len(args.path) > 0 else folderForge.path))
	print(Color.warning("\nCreating the folder structure...\n"))
	
	folderForge.forge(args.path)

	# With success emoji and party popper emoji \U0001F389 \U0001F389  
	print(Color.success("\n \U0001F600 Folder structure created successfully!!!\U0001F389 \U0001F389 \U0001F389 \n"))

if __name__ == "__main__":
	main()