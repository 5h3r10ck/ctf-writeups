![](https://i.ibb.co/QnvzbJ0/Screenshot-2.png)


We are given an image of a Windows XP Machine and we are asked to look for deleted files.

An easy but uninteresting way you can use to solve this challenge is load the system image in FTK imager or Autopsy or any other forensics tool. And use the keyword search feature.

![](https://i.ibb.co/m49N3J6/Screenshot-1.png)

If we want to act like we dont know what we are looking for. we can proceed as follows:

As you may know, Windows uses NTFS(New Technology File System) which has many features, one that we took advantage of is data recovery.
To perform data recovery, NTFS uses journaling. The NTFS Journal is kept inside NTFS Metadata in a file called $LogFile.
This $LogFile keeps record of all operations that occurred in the NTFS volume such as file creation, deletion, renaming, copy, etc.

There is also an attribute you can look for called $I30. This attribute contains information about file names and directories that are stored inside a particular directory.

Read more about this [here](https://countuponsecurity.com/2016/05/30/digital-forensics-ntfs-indx-and-journaling/).
