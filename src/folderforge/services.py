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
		Create a new directory
		"""

		if not os.path.exists(path):
			os.mkdir(path)

class FolderForgeService:
	
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

# th€ main function for all services testing
def main():
	config = json.load(open("config.json"))

	path = config.get("path")
	tree = config.get("tree")

	for node in FolderForgeService.searchPaths(tree):
		type = node["type"]
		path = node["path"]
		
		print(path)

		if type == "file":
			FileService.createFile(path)
		else:
			FileService.createDirectory(path)
		
if __name__ == "__main__":
	main()