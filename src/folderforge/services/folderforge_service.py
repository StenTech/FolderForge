import os
import json


class FolderForgeService:
	
	@classmethod
	def readJSON(cls, path: str) -> None:
		"""
		Read a json file and return its content as a dictionary
		
		Agrs:
			path (str): The json file path
		"""

		return json.load(open(path))
	
	@classmethod
	def searchPaths(cls, tree: list) -> None:
		"""
		An iterator method/function to
		explore tree nodes using DFS algorithm and create path property for all the node

		Args:
			tree (list): The list of files or directories according to description file 

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



