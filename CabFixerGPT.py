import os
import sys
import re
import glob

# Extract Python version
fullVer = str(sys.version_info)
verList = re.findall(r'\d+', fullVer)
ver = f"{verList[0]}.{verList[1]}"

# Define paths
cabPath = os.path.expandvars('%LocalAppData%') + '\\Packages\\PythonSoftwareFoundation.Python.'
cabPath2 = '\\LocalCache\\local'
cabPath3 = f'packages\\Python{verList[0]}{verList[1]}\\site'
cabPath4 = 'packages\\MeCab\\'

srcAlt = 'packages\\lib\\site'
srcFilePattern = f"{cabPath}{ver}*{cabPath2}-{srcAlt}-{cabPath4}libmecab.dll"

# Find source file
source_files = glob.glob(srcFilePattern)
if not source_files:
    print('\nFAIL: Could not locate source file.')
else:
    print(f'\nFound: {source_files[0]}')
    print('\nSearching...')

    # Find destination path
    destPathPattern = f"{cabPath}{ver}*{cabPath2}-{cabPath3}-{cabPath4}"
    destPaths = glob.glob(destPathPattern)
    if destPaths:
        destPath = destPaths[0]
        print(f'\nFound: {destPath}')
        print('\nMoving libmecab.dll')

        try:
            os.rename(source_files[0], os.path.join(destPath, 'libmecab.dll'))
            if os.path.isfile(os.path.join(destPath, 'libmecab.dll')):
                print('\nProcess successful!')
        except Exception as e:
            print(f"Error moving file: {e}")
    else:
        print('\nNo destination path found.')
