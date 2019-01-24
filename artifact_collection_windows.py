# Written by Jason Dotray
# Updated 2019/01/24
# Utilizing Python3
#
# Tool to extract Windows artifacts
# from mounted evidence file

from subprocess import PIPE, run

def kick(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Get Source and Destination
print('Enter the path to source (ie: /mount/mountpoint/:')
srcpath = input()

print('Enter destination (ie: /tmp/test/:')
dstpath = input()

print('What\'s the username on this system (ie: Joe_BagoDonuts:')
userName = input()

# Artifact Collection

# Grab AmCache
kick("cp " + srcpath + "Windows/appcompat/Programs/Amcache.hve " + dstpath)

# Prefetch
kick("cp -aR " + srcpath + "Windows/Prefetch " + dstpath)

# Registry
kick("cp " + srcpath + "Windows/System32/config/SYSTEM " + dstpath)
kick("cp " + srcpath + "Windows/System32/config/SECURITY " + dstpath)
kick("cp " + srcpath + "Windows/System32/config/SAM " + dstpath)
kick("cp " + srcpath + "Windows/System32/config/SOFTWARE " + dstpath)

# NTUSER.DAT
kick("cp " + srcpath + "Users/" + userName + "/NTUSER.DAT " + dstpath)

# USRCLASS.DAT
kick("cp " + srcpath + "Users/" + userName + "/AppData/Local/Microsoft/Windows/UsrClass.dat " + dstpath)

# MFT
kick("cp " + srcpath + "'$MFT' " + dstpath + "MFT")

# Windows Logs
kick("cp -aR " + srcpath + "Windows/System32/winevt/Logs " + dstpath)

# User's Jumplist
kick("cp -aR " + srcpath + "Users/" + userName + "/AppData/Roaming/Microsoft/Windows/Recent/AutomaticDestinations " + dstpath)

# Shortcut/LNK files
kick("cp -aR " + srcpath + "Users/" + userName + "/AppData/Roaming/Microsoft/Office/Recent " + dstpath + "Shortcut-Office/")
kick("cp -aR " + srcpath + "Users/" + userName + "/AppData/Roaming/Microsoft/Windows/Recent " + dstpath + "Shortcut-Windows/")
