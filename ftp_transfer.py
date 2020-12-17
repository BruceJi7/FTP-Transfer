import os, sys
from ftplib import FTP
import time

#Get config from file
THIS_FILE_LOC = os.path.dirname(__file__)
with open(os.path.join(THIS_FILE_LOC, 'CONFIG.txt'), 'r') as conf:
    cfg = conf.readlines()

IP_PREFIX = cfg[0].split(":")[1].strip()
if not IP_PREFIX.endswith('.'):
    IP_PREFIX = IP_PREFIX + '.'
    
PORT = int(cfg[1].split(":")[1].strip())
FOLDER_NAME = cfg[4].split(":")[1].strip()
BLOCKSIZE = int(cfg[5].split(":")[1].strip())

USER = cfg[2].split(":")[1].strip()
if USER == 'None':
    USER = None

PASS = cfg[3].split(":")[1].strip()
if PASS == 'None':
    PASS = None




drag_and_dropped_files = None
if len(sys.argv) > 1:
    drag_and_dropped_files = sys.argv[1:]


# Instructions printed
if not drag_and_dropped_files:
    print('Drag and drop files to the icon to use')
    time.sleep(3)
    exit()


print('FTP TRANSFER TOOL\n\n')
ip_suffix = input('Enter IP suffix: ')

print('Establishing connection...')
ftp_instance = FTP(user=USER, passwd=PASS)

try:
    ftp_instance.connect(host=IP_PREFIX+ip_suffix, port=PORT)
    print('Connection: Success')

except:
    print('Connection Failed')
    errors = sys.exc_info()
    for e in errors:
        print(str(e))
    input('\nPress key to exit.')
    exit()

ftp_instance.cwd(FOLDER_NAME)
for F in drag_and_dropped_files:

    sizeWritten = 0
    totalSize = os.path.getsize(F)
    percentComplete = -1
    def handle(block):
        global sizeWritten, percentComplete
        sizeWritten += BLOCKSIZE
        internalPercentComplete = int((sizeWritten / totalSize)*100)
        if internalPercentComplete > percentComplete:
            percentComplete = internalPercentComplete
            print(f"{str(percentComplete)}%...", end="\r")


    F_filename = os.path.basename(F)
    with open(F, 'rb') as F_binary:
        print(f'Transferring: {F_filename}')
        ftp_instance.storbinary(cmd=f"STOR {F_filename}", fp=F_binary, blocksize=BLOCKSIZE, callback=handle)
        print('\n')
        print('Done')
    

ftp_instance.quit()
print('FTP Operations completed.')
time.sleep(3)




