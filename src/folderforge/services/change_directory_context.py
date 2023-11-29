import os

class ChangeDirectoryContext:
	def __init__(self, new_directory):
		self.new_directory = new_directory
		self.old_directory = os.getcwd()

	def __enter__(self):
		if self.new_directory != "":
			os.chdir(self.new_directory)

	def __exit__(self, *args):
			os.chdir(self.old_directory)