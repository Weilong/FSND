import os

def rename_files():
	file_list = os.listdir("/Users/tonyaziten/Documents/FSND/prank")
	print(file_list)
	
	saved_path = os.getcwd()
	print saved_path
	os.chdir("/Users/tonyaziten/Documents/FSND/prank")
	
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None, "0123456789"))

rename_files()