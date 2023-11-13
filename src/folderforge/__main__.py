#! /usr/bin/env python3

try:
	from __init__ import FolderForge
	from utils.Class import Color
	from utils.functions import parser
except:
	from . import FolderForge
	from .utils.Class import Color
	from .utils.functions import parser


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