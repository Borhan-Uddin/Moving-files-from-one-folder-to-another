#this python sciprts print all the pdf files in a given directory

import os, glob

import shutil
base_dir = "C://Users//Borhan//Downloads"

destination_dir = "C://Users//Borhan//Downloads//pdf"
#method 1 using glob
os.chdir(base_dir)

for file in glob.glob("*.pdf"):
	shutil.move(file,destination_dir)

#method 2 using listdir

# for fname in os.listdir(base_dir):
# 	if fname.endswith(".pdf"):
# 		print(fname)

#move all pdfs to a specific folder



# for fname in os.listdir(base_dir):
# 	if fname.endswith(".pdf"):
# 		#shutil.copy(os.path.join(base_dir, fname), destination_dir)
# 		print(os.path.join(base_dir,fname))

