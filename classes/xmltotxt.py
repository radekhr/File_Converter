import xml.etree.ElementTree as ET
import re

class Xmltotxt():
	def __init__(self, filename):
		self.filename = filename
		
	def convert_xml_to_txt(self):
		tree = ET.parse(self.filename)
		root = tree.findall('row')
		
		
		
			
