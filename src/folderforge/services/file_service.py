import os

try:
	from models import File
except:
	from ..models import File


class FileService:

	@classmethod
	def createFile(cls, path: str) -> File:
		"""
		Create a new file
		"""

		with open(path, "w"):
			pass
		
		# return File instance
		file = File(path)

		return file

	@classmethod
	def createDirectory(cls, path: str):
		"""
		Create a new directory
		"""

		if not cls.pathExists(path):
			os.mkdir(path)

	@classmethod
	def createDirectoryWithSubDirs(cls, path: str):
		"""
		Create a new directory with subdirectories
		"""
		if not cls.pathExists(path):
			os.makedirs(path, exist_ok=True)

		

	@classmethod
	def pathExists(cls, path: str):
		"""
		Check if a path exists
		"""

		return os.path.exists(path)
	
	@classmethod
	def isdIr(cls, path: str) -> bool:
		"""
		Check if a path is a directory
		"""

		return os.path.isdir(path)


def main():
	FileService.createDirectoryWithSubDirs("home/stentech/Documents/project/folderforge/src/folderforge")

if __name__ == "__main__":
	main()