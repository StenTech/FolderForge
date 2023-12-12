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

		Args:
			path (str): The file's path

		Returns:
			File: the file created as File object 
		"""

		with open(path, "w"):
			pass
		
		# return File instance
		file = File(path)

		return file

	@classmethod
	def createDirectory(cls, path: str) -> None:
		"""
		Create a new directory

		Args:
			path (str): The directory's path
		"""

		if not cls.pathExists(path):
			os.mkdir(path)

	@classmethod
	def createDirectoryWithSubDirs(cls, path: str) -> None:
		"""
		Create a new directory with subdirectories
		
		Args:
			path (str): The directory's path
		"""

		if not cls.pathExists(path):
			os.makedirs(path, exist_ok=True)

		

	@classmethod
	def pathExists(cls, path: str) -> bool:
		"""
		Check if a path exists

		Args:
			path (str): The path
		
		Returns:
			bool: True if the path exists, otherwise False
		"""

		return os.path.exists(path)
	
	@classmethod
	def isdIr(cls, path: str) -> bool:
		"""
		Check if a path is a directory

		Args:
			path (str): The directory's path
		
		Returns:
			bool: True if it's directory, otherwise False
		"""

		return os.path.isdir(path)


def main():
	FileService.createDirectoryWithSubDirs("home/stentech/Documents/project/folderforge/src/folderforge")

if __name__ == "__main__":
	main()