# import os
import xml.etree.ElementTree as ET

class Txttoxml():
	def __init__(self, filename):
		self.filename = filename
		
	def convert_txt_to_xml(self):
		words_list = []
		with open(self.filename) as ftxt:
			lines = ftxt.readlines()		
			for line in lines:	
				if line != '\n':		
					words_list += line.split()
					self.generate_xml_doc(words_list)
					words_list = []
		print('Sucessfull conversion TXT->XML. File XML is located in working \
directory. Filename: ' + self.new_filename )
				
		
	def generate_xml_doc(self, words_list):
		new_filename = self.change_format_to_xml()
		with open(new_filename, 'a') as nf:
			root = ET.Element('row')
			for word in words_list:
				child_el = ET.SubElement(root, 'col')
				child_el.text = word
			my_data = ET.tostring(root).decode()
			nf.write(str(my_data))
		
		
	def change_format_to_xml(self):
		self.new_filename = self.filename.replace('.txt', '.xml')
		return self.new_filename
	
		
