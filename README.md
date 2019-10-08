# VIT-Notes-Sorting

This project is only aimed at students of the Vellore Institue of Technology.
As the students may now the notes downloaded from the VTOP online portal are downloaded with long file names and are a mess to organize and handle, especially during the exam times.

This Code that can be converted into a startup program will auto sort the notes, shorten the file name and place them in neatly organized folder system that is auto created.

Required libs:
1. os
2. shutil
3. time
4. pyinstaller

After downloading the python file, open it and do the following:

Change the Sorted_Folder_Location and Downloads variable paths to the locations to which you want the notes to get dumped and where the downloaded files go from the VTOP portal.

Run the code and make sure that the code runs properly on your system.

To convert the python file into a executeable go to the folder in which the code is saved and open cmd in the folder. 

Run the following command : "pyinstaller -w File_Sorter.py". This will create 2 folders, the executable will be in the dist folder.

Copy the executabel and paste a shortcut in this folder: 'C:/Users/ADMIN/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'


In my experience this code running in the background dosen't cause the PC to slow down or anything like this. If you have any suggestions or comments so ask.

Authors    
Himasava     
Praneeth    
