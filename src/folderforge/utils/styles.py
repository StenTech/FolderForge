from os.path import isdir

class Color:
	success = lambda _str: '\033[92m' + _str + '\033[0m' # green
	danger = lambda _str: '\033[91m' + _str + '\033[0m' # red
	primary = lambda _str: '\033[96m' + _str + '\033[0m' # cyan
	warning = lambda _str: '\033[33m' + _str + '\033[0m' # yellow

class Style:
	bold = lambda _str: '\033[1m' + _str + '\033[0m'
	underline = lambda _str: '\033[4m' + _str + '\033[0m'
	blink = lambda _str: '\033[5m' + _str + '\033[0m'
