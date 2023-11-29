import argparse


def parser():
	parser = argparse.ArgumentParser(
		prog="folderforge",
		description="A simple tool to create folder structures from a JSON file",
		epilog="%(prog)s made with love by @StenTech and @RidoineEl, enjoy!!!",
	)
	parser.add_argument(
    	"--version", action="version", version="%(prog)s 1.0.0"
	)
	parser.add_argument(
		"--description_file", 
		help="The path to the structure file, it's a JSON file",
		default="description.json",
		nargs="?",
		type=str
	)
	parser.add_argument(
		"-p", 
		"--path", 
		help="The path to the root directory in which the folder structure will be created, it can be empty, a simple name or a path",
		default="",
		nargs="?", 
		type=str
	)
	

	return parser.parse_args()

def getFileContent(path: str) -> str:
	"""
	return the file content as string
	""" 

	content = ""
	
	with open(path, "r") as file:
		lines = file.readlines()
		content = "".join(lines)

	return content


# def main():
# 	args = parser()
# 	print(args)	

# if __name__ == "__main__":
# 	main()