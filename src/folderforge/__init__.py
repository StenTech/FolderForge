from os.path import dirname, join

# import services
try:
	from services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)
except:
	from .services import (
		FolderForgeService,
		FileService,
		ChangeDirectoryContext
	)


class FolderForge:
	def __init__(self, description_file_path: str):
		self.description_file_path = description_file_path
		description = FolderForgeService.readJSON(description_file_path)
		self.path = description.get("path", "")
		self.tree = description.get("tree", [])
		
	def forge(self):
		FileService.createDirectory(self.path)

		with ChangeDirectoryContext(self.path):	
			for node in FolderForgeService.searchPaths(self.tree):
				type = node["type"]
				path = node["path"]
				
				if type == "file":
					FileService.createFile(path)
				elif type == "directory":
					FileService.createDirectory(path)
				else:
					raise Exception("Unknown node type: " + type)
			
			return self


# the main function for all services testing
def main():
	_dir = dirname(dirname(dirname(__file__)))

	folderForge = FolderForge(join(_dir, "config.json"))
	folderForge.forge()
		
if __name__ == "__main__":
	main()