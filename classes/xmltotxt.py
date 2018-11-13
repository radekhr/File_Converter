class Xmltotxt():
	def __init__(self, filename):
		self.filename = filename
		
		
	def convert_xml_to_txt(self):
		words_list = []
		with open(self.filename) as fxml:
			while True:
				line = fxml.readline()
				if line:
					if line.startswith('<row'):
						pass
					else:
						words_list.append(line[5:-7].strip()) #delete tags <col> from line
				else:
					self.generate_txt_file(words_list)
					print('Sucessfull conversion XML -> TXT.\n File XML is \
located in working directory.\n Filename: ' + self.new_filename )
					break
		
	def generate_txt_file(self, words_list):
		new_filename = self.change_format_to_txt()
		with open(new_filename, 'w') as nf:
			for word in words_list:
				if word != '':
					nf.write(word + ' ')
				else:
					nf.write('\n')
		
				
		
	def change_format_to_txt(self):
		self.new_filename = self.filename.replace('.xml', '.txt')
		return self.new_filename
		
		
		
			
