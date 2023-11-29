# FolderForge

FolderForge is a Python utility for creating directory structures based on a description file in JSON format.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
## Introduction

FolderForge simplifies the process of creating directory structures by using a JSON description file. It allows you to define folders, subfolders, and files along with their hierarchy and content.

## Installation

```bash
pip install folderforge
```

## Usage	

To use FolderForge, run the following command in the terminal:

```bash
folderforge --description_file path/to/description.json --path path/to/create/structure
```

- **`--description_file`**: Path to the JSON description file.
- **`--path`** (optional): Path to the root directory where the folder structure will be created

## Description

FolderForge uses a JSON description file to define the folder structure. The configuration file should have the following format:

```json
{
	"path": "project/sub1/sub2/",
	"tree": [
		{
			"name": "folderforge",
			"type": "directory",
			"children": [
				{
					"name": "subdir",
					"type": "directory",
					"children": [

					]
				},
				{
					"name": "init.py",
					"type": "file",
					"content": {
						"type": "plaintext",
						"value": "Hello World"
					}
				},
				{
					"name": "core.py",
					"type": "file",
					"content": {
						"type": "filepath",
						"value": ".gitignore"
					}
				},
				{
					"name": "file_formats.py",
					"type": "file",
					"content": {
						"type": "url",
						"value": "https://jsonip.com"
					}
				}
			]
		},
		{
			"name": "RREADME.md",
			"type": "file"
		},
		...
	]
}
```

### Configuration Properties

- **`path`**: (Optional) The base path where the folder structure will be created. If not specified, the structure will be created in the current working directory.

- **`tree`**: An array representing the directory structure. Each element in the array is an object with the following properties:

	- **`name`**: The name of the directory or file.

	- **`type`**: The type of the node, either "directory" or "file".

	- **`children`** (for directories only): An array of objects representing the contents of the directory. Each child follows the same structure as its parent.

	- **`content`** (for files only): An object specifying the content of the file. The properties depend on the type of content:
		- **`type`**: The type of content, such as **"plaintext"**, **"filepath"**, or **"url"**.
		- **`value`**: The actual content, whether it's text, a file path, or a URL.

### Notes

- Folders and files are created recursively based on the provided configuration.
- Content types for files include "plaintext" for raw text, "filepath" for content from a file, and "url" for content fetched from a URL.

Adjust the description file as needed for your project's directory structure.

<br />

## Examples

Create an `example.json` file with the following description:

```json
{
	"path": "project/",
	"tree": [
		{
			"name": "src",
			"type": "directory",
			"children": [
				{
					"name": "folderforge",
					"type": "directory",
					"children": [
						{
							"name": "__init__.py",
							"type": "file",
							"content": {
								"type": "plaintext",
								"value": "Initialization file for FolderForge"
							}
						},
						{
							"name": "__main__.py",
							"type": "file",
							"content": {
								"type": "url",
								"value": "https://raw.githubusercontent.com/ridoineel/FolderForge/main/src/folderforge/__main__.py"
							}
						}
					]
				},
				{
					"name": "utils",
					"type": "directory",
					"children": [
						{
							"name": "styles.py",
							"type": "file",
							"content": {
								"type": "plaintext",
								"value": "Utility functions for styling"
							}
						},
						{
							"name": "functions.py",
							"type": "file",
							"content": {
								"type": "url",
								"value": "https://raw.githubusercontent.com/ridoineel/FolderForge/main/src/folderforge/utils/functions.py"
							}
						}
					]
				}
			]
		},
		{
			"name": ".gitignore",
			"type": "file",
			"content": {
				"type": "url",
				"value": "https://raw.githubusercontent.com/ridoineel/FolderForge/main/.gitignore"
			}
		},
		{
			"name": "README.md",
			"type": "file",
			"content": {
				"type": "plaintext",
				"value": "This is the README file for the project."
			}
		}
	]
}
```

**Run the Command**

Run the following command in your terminal to create the folder and file structure based on the description file:

```bash
folderforge --description_file example.json
```

**Expected Result**

The command should create the file and folder structure defined in the example.json description file. You should see confirmation messages for each item created. Check the directory specified in your description file (in this example, "project/") to see the structure created. Make sure the files contain the expected content.

```bash
[FOLDERFORGE]: Creating the folder structure..

[FOLDERFORGE]: Creating directory src/folderforge
[FOLDERFORGE]: Creating file src/folderforge/__init__.py
[FOLDERFORGE]: Creating file src/folderforge/__main__.py (from URL)
[FOLDERFORGE]: Creating directory src/utils
[FOLDERFORGE]: Creating file src/utils/styles.py
[FOLDERFORGE]: Creating file src/utils/functions.py (from URL)
[FOLDERFORGE]: Creating file .gitignore (from URL)
[FOLDERFORGE]: Creating file README.md (from PLAINTEXT)
[FOLDERFORGE]: 🎉 Folder structure created successfully!!!
```

<br />

## Contributing

Contributions are welcome! Please check the [	](./CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for 
details.															