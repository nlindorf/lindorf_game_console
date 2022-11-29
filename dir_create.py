import os

selected_user = "Kristen"

directory = selected_user + '_nerd'
parent_dir = "/Users/nathanlindorf/desktop/python_work"
path = os.path.join(parent_dir, directory)
isExist = os.path.exists(path)
if isExist == True:
	print(path)
elif isExist == False:
	os.mkdir(path)
	print("Directory '% s' created" % directory)