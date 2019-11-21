import os

compiler = 'g++' # g++ for C++, gcc for C
file_to_compile = 'example.cpp' 
libraries_to_link = ['curl', 'jsoncpp'] # add any required libraries here

libstring = ''
for library in libraries_to_link:
	library = ' -l' + library
	libstring += library

while True:
	if input('Compile and run me? (ENTER)') == '':
		print('Here we go!', '\n________________________________________________________\n')
		os.system(compiler + ' ' + file_to_compile + libstring)
		os.system('./a.out')
		print('\n________________________________________________________\nAll done!')
