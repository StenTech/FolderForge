import os
import json


class FileService:

	@classmethod
	def createFile(cls, path: str):
		"""
		Create a new file
		"""

		with open(path, "w"):
			pass


	@classmethod
	def createDirectory(cls, path: str):
		"""
		Create a new directory perhabs with subdirectories
		"""
		
		with ChangeDirectoryContext(""):
		 # Create folders sequentially
			for folder in path.split('/'):
				os.makedirs(folder, exist_ok=True)
				os.chdir(folder)

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
	


class FolderForgeService:
	
	@classmethod
	def readJSON(cls, path: str):
		"""
		Read a json file and return its content as a dictionary
		"""
		return json.load(open(path))
	
	@classmethod
	def searchPaths(cls, tree: list):
		"""
		An iterator method/function to
		explore tree nodes using DFS algorithm and create path property for all the node

		Example:
			for node in FolderForgeService.searchPaths(tree):
				print(node["path"])
		"""

		cur_list = tree
		visited = []

		while cur_list:
			node = cur_list.pop()
			visited.append(node) 

			if not node.get("path"):
				node["path"] = node["name"]  

			# return node for the current iteration
			yield node

			# explore node children if exists
			for child in node.get("children", []):
				if child not in visited:
					# child["parent"] = node["name"] + node.get("parent_path", "")
					child["path"] = os.path.join(node.get("path", ""), child["name"])

					cur_list.append(child)


class ChangeDirectoryContext:
	def __init__(self, new_directory):
		self.new_directory = new_directory
		self.old_directory = os.getcwd()

	def __enter__(self):
		if self.new_directory != "":
			os.chdir(self.new_directory)

	def __exit__(self, *args):
			os.chdir(self.old_directory)
