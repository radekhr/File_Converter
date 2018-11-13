import sys
import os
from classes.txttoxml import Txttoxml
from classes.xmltotxt import Xmltotxt

if ((len(sys.argv) == 2 )): # check nums of args in console
	filename = sys.argv[1]
	try:
		with open(filename) as f_obj:
			if f_obj.tell() == 0:
				if filename[-3:] == 'txt':				
					txt_file = Txttoxml(filename)
					txt_file.convert_txt_to_xml()
				elif filename[-3:] == 'xml':
					xml_file = Xmltotxt(filename)
					xml_file.convert_xml_to_txt()
				else:
					print('Invalid file format. Acceptable: .txt or .xml')
					sys.exit(0)
	except FileNotFoundError:
		message = print('Sorry, but file ' + filename + ' does NOT exist in work directory')
		print(message)		
else:
	print('Please write 2 args. Not less, not more.')
	sys.exit(0)
	
