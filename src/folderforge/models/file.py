import requests
from os.path import dirname, join

try:
	from utils.functions import getFileContent
	from utils.enums import CONTENT_TYPES
	from utils.styles import Style
except:
	from ..utils.functions import getFileContent
	from ..utils.enums import CONTENT_TYPES
	from ..utils.styles import Style


class File:
	def __init__(self, path):
		"""
		Initialize a File object with the specified path.

		Args:
			path (str): The path to the file.
		"""

		self.path = path

	def putContent(self, content_type: str, content_value: str, description_file_path: str):
		"""
		Put content into the file based on the specified content type.

		Args:
			content_type (str): The type of content to be added. Should be one of CONTENT_TYPES enum values.
			content_value (str): The actual content to be added.
			description_file_path (str): The path to the description file.

		Raises:
			ValueError: If an unsupported content type is provided.
		"""

		content_type = content_type.upper()

		# Use a match statement to handle different content types
		match content_type:
			case CONTENT_TYPES.PLAINTEXT:
				self._putPlaintextContent(content_value)
			case CONTENT_TYPES.FILEPATH:
				self._putFilePathContent(
					filepath=content_value, 
					parent_dir=dirname(description_file_path)
				)
			case CONTENT_TYPES.URL:
				self._putUrlContent(content_value)
			case _:
				pass
	
	def _putPlaintextContent(self, plaintext: str):
		"""
        Put plaintext content into the file.

        Args:
            plaintext (str): The plaintext content to be added to the file.
        """

		with open(self.path, "w") as file:
			file.write(plaintext)
	
	def _putFilePathContent(self, filepath: str, parent_dir: str):
		"""
		Put content from another file into the current file.

		Args:
			filepath (str): The path to the file whose content should be added.
			parent_dir (str): The directory containing the description file.
		"""

		abs_filepath = join(parent_dir, filepath)

		try:
			content = getFileContent(abs_filepath)
		except:
			raise ValueError(Style.bold(f"file {abs_filepath} not exists or it's not plaintext file"))

		# put content to the file
		with open(self.path, "w") as file:
			file.write(content)

	def _putUrlContent(self, url: str):
		"""
		Download content from a URL and put it into the file.

		Args:
			url (str): The URL from which to download content.
		"""

		# make the request to retrieve the text response from the url
		response = requests.get(url)

		if response.status_code == 200:
			with open(self.path, "w") as file:
				file.write(response.text)
		else:
			raise ValueError(f"Retrieving data from the URL {url} for the file {self.path} failed. Verify that the URL is correct and accessible.")
		