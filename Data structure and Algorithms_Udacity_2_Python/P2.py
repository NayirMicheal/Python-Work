import os
import os.path
from os import path
def find_files(suffix, path):
	"""
	Find all files beneath path with file name suffix.

	Note that a path may contain further subdirectories
	and those subdirectories may also contain further subdirectories.

	There are no limit to the depth of the subdirectories can be.

	Args:
	suffix(str): suffix if the file name to be found
	path(str): path of the file system

	Returns:
	a list of paths
	"""
	list_of_c = list()
	list_of_paths = list()
	if os.path.isdir(path):
		list_of_paths.append(path) # first path to check
		for path_ in list_of_paths: # for every path in list of paths
			for sub in os.listdir(path_): # for every file or folder in the path
				if(os.path.isfile(os.path.join(path_, sub))): # check if it is a file 
					if os.path.join(path, sub).endswith(suffix): # if yes with the suffix append it to the return list
						list_of_c.append(sub)
					
				if(os.path.isdir(os.path.join(path_, sub))): #if it is a directory
					list_of_paths.append(os.path.join(path_, sub))# append another path to search on it on the list of paths	
		return list_of_c
	else:
		return "Path is not exist"

#test case 1
print(find_files(".c","./testdir"))

#test case 2
print(find_files(".c","./testdir/subdir1"))

#test case 3
print(find_files(".c","./testdir/subdir3/subsubdir1"))

#test case 4
print(find_files(".c","./testdir/subdir3/subsubdir"))