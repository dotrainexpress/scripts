# Written by Jason Dotray
# Updated 2019/01/24
# Utilizing Python3
#
# Tool to mount image files to linux for
# browsing the filesystem in Read-Only

from subprocess import PIPE, run

def kick(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

# Get Source and Destination
print('Source name of E01 (ie: /mnt/hgfs/F/CaseTEST/C_DRIVE.E01):')
srcE01 = input()
print('Source destination of EWF (ie: /mount/rawimage/):')
dstEWF = input()
print('Filesystem mount point (ie: /mount/mountpoint/:')
fsmnt = input()

# First, let's clear those directories...
kick("umount -f " + fsmnt)
kick("umount -f " + dstEWF)


# Mount the E01 to EWF container
kick("ewfmount " + srcE01 + ' ' + dstEWF)

# Before we can mount the EWF1 we need to determine the offset of the primary partition
# Grab offset of the largest partition (we'll assume it's the OS)
offset = kick("fdisk -l " + dstEWF + "ewf1 |sort -nrk 4 |awk 'FNR == 1 {print $2}'")
print('Offset value is: ' + offset)

# Should also calculate the sector size
sector = kick("fdisk -l " + dstEWF + "ewf1 |awk 'FNR == 2 {print $8}'")

# Mount the ewf1
kick("mount " + dstEWF + "ewf1 " + fsmnt + " -o ro,loop,show_sys_files,streams_interface=windows,offset=$((" + sector + "*" + offset + "))")