import os
import sys
import re
import glob

fullVer = str(sys.version_info)
verList = re.findall(r'\w*\d', fullVer)
ver = verList[0] + '.' + verList[1]

cabPath = os.path.expandvars('%LocalAppData%') + '\\Packages\\PythonSoftwareFoundation.Python.'
cabPath2 = '\\LocalCache\\local'
cabPath3 = 'packages\\Python' + verList[0] + verList[1] + '\\site'
cabPath4 = 'packages\\MeCab\\'

srcAlt = 'packages\\lib\\site'
destPath = str(glob.glob(cabPath + ver + '*' + cabPath2 + '-' + cabPath3 + '-' + cabPath4)[0])

looper = [1]

for i in looper:
	if ((glob.glob(cabPath + ver + '*' + cabPath2 + '-' + srcAlt + '-' + cabPath4 + 'libmecab.dll'))):
		print('\n Found: ', cabPath + ver + '*' + cabPath2 + '-' + srcAlt + '-' + cabPath4 + 'libmecab.dll')
		print('\n Searching...')
	else:
		print('\n FAIL: Unable to locate source file.')
		break

	if destPath:
		print('\n Found: ', destPath)
		print('\n Moving libmecab.dll')
		os.rename(glob.glob(cabPath + ver + '*' + cabPath2 + '-' + srcAlt + '-' + cabPath4  + 'libmecab.dll')[0], destPath + 'libmecab.dll')
		if (os.path.isfile(destPath + 'libmecab.dll')):
			print('\n Process successful!')
	else:
		print('\n FAIL: Unable to locate destination path. Did you install Python from the Microsoft Store?')





