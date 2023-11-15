#! /usr/bin/env python3
from os import path, system

try:
	from __init__ import FolderForge
	from utils.styles import Color
	from utils.functions import parser
except:
	from . import FolderForge
	from .utils.styles import Color
	from .utils.functions import parser


# the main function for all services testing
def main():
	args = parser()
	description_file = path.abspath(args.description_file)

	folderForge = FolderForge(description_file)
	project_path = path.abspath(args.path if len(args.path) > 0 else folderForge.path)
	
	# clear console
	system("cls | clear")
	
	# Printing the description file path
	print("[FOLDERFORGE]: Description file path: " + Color.primary(description_file))
	# Printing the path to the root directory in which the folder structure will be created
	print("[FOLDERFORGE]: Root directory path: " + Color.primary(project_path))
	print(Color.warning("\n[FOLDERFORGE]: Creating the folder structure...\n"))
	
	folderForge.forge(project_path)

	# With success emoji and party popper emoji \U0001F389 \U0001F389  
	print(Color.success("\n[FOLDERFORGE]:  \U0001F600 Folder structure created successfully!!!\U0001F389 \U0001F389 \U0001F389 \n"))

if __name__ == "__main__":
	main()