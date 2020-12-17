 # FTP-Transfer

FTP-Transfer is a small Python script for sending files via FTP.

For iOS, consider using the app FTPManager.


### Usage

##### Setting Up

The script loads config data from the config file.

First, make sure the computer and the other device are connected to the same Wi-Fi network.

If you are using FTPManager, find the built-in servers option, and push start.

You will see an IP address and port. Make sure the IP prefix (e.g `192.168.0.`, including the final dot) is entered correctly in the config file.

The user and password are optional.

##### Using The Script

To send a file, drag the file and drop it onto the script. You can drag and drop multiple files.

The script will ask you for the final part of the IP (it may vary between usages)

Enter it and the script will transfer the files.

