import os
import shutil
from time import sleep
import csv
'''
This program is developed by Himanshu Savargaonkar :)

This program will startup when the computer is booted, will check your downloads folder for any updates every 1 min and sort the files in the VIT VTOP format.
Follow the following step to make that happen.

1. Change the location where you want the program to put the sorted data (There is no need to make any folders the code will do it by itself)
2. Change the Downloads dictoinary. Incase your downloaded VTOP files are not stored in the downloads folder please update your Downloads variable below. If your
   Downloads path doesnt match the one given below pls change that too. Also change the csv_File variable to where ever your csv file is saved to
3. The code is set to do the sorting. If you do not want to make a executeable out of this, then you are done. Once you download more files just manually run this py file.
4. Run the code and make sure no errors popup. You can see that all the VIT files vanish from the Downloads folder and new folders appear in the given put location.
5. For making an excuteable we will use the pyinstaller lib, download and install it using pip.
6. Open cmd in the folder in which this py code is saved.
7. Run the command 'pyinstall -w -F File_Sorter3.0.py'
8. Copy the exe file and paste it in the following folder : 'C:/Users/ADMIN/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
   
'''

Sorted_Folder_Location = "D:/Drive/"                                            #The folder path where you want to store the sorted files
Downloads = "C:/Users/Himanshu/Downloads"                                       #The downloads folder path
CSV_File = "'D:/Offline_Projects/VIT-Notes-Sorting-master/Course_List.csv'"     #The location of the csv file

def scan_sort(course_data):                                                 #This function scans downloads and returns the list of files fitting VIT file format.
    sorted_files = []

    download_list = os.listdir(Downloads)
    for filename in download_list:
        if(filename[0:7] == 'FALLSEM' or filename[0:6] == 'WINSEM'):
            sorted_files.append(filename)
    classified_file_list = divide_and_sort(sorted_files,course_data)            #divide and sort function is called so the list is classified
    return classified_file_list

def divide_and_sort(sorted_files,course_data):                                       #This function accepts files one by one and makes a class object which has its (Year/Sem/SubCode/Type)
    classified_files = []
    for file in sorted_files:
        file_split = file.split('_')
        temp = file_split[len(file_split)-1].split('.')
        file_split.pop()
        file_split.append(temp[0])
        file_split.append(temp[1])
        file_details = []
        file_details.append(file)
        if(file_split[0][0] == 'F'):
            file_details.append('Fall_Sem')
            year = file_split[0][7:11]
        elif(file[0:6] == 'WINSEM'):
            file_details.append('Win_Sem')
            year = file_split[0][6:10]
        file_details.append(year)
        code = file_split[1]
        for sub in course_data:
            if code in sub:
                code = code + ' ' + sub[1]
        file_details.append(code)
        if file_split[2] == 'TH':
            file_details.append('Theory')
        elif file_split[2] == 'LO':
            file_details.append('Lab Only')
        elif file_split[2] == 'ETH':
            file_details.append("Embedded_Theory")
        elif file_split[2] == 'ELA':
            file_details.append('Embedded_Lab')
        else:
            file_details.append(file_split[2])
        name =''
        for i in range(len(file_split)-2,5,-1):
            name += file_split[i] + ' '
        name += file_split[5] + '.' + file_split[len(file_split)-1]
        file_details.append(name)
        classified_files.append(file_details)
    return classified_files

def check_file_tree(file):                                          #Checks that the folder in which this file needs to be put exists. If not it creates that folder
    main_list = os.listdir(Sorted_Folder_Location)
    if file[2] not in main_list:
        os.chdir(Sorted_Folder_Location)
        os.mkdir(file[2])
        os.chdir(Sorted_Folder_Location + str(file[2]))
        os.mkdir("Fall_Sem")
        os.mkdir("Win_Sem")
    os.chdir(Sorted_Folder_Location + str(file[2]) + '/' + str(file[1]))
    sub_list = os.listdir()
    if file[3] not in sub_list:
        os.mkdir(file[3])
    os.chdir(Sorted_Folder_Location + str(file[2]) + "/" + str(file[1]) + "/" + file[3])
    topic_list = os.listdir()
    if file[4] not in topic_list:
        os.mkdir(file[4])



def move_file_rename(file):                                         #Moves that file to its folder and renames the file as per its initial name
    file_duplication_check = os.listdir(Sorted_Folder_Location + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4]))
    if str(file[5]) not in file_duplication_check:
        shutil.move(Downloads + "/" + file[0], Sorted_Folder_Location + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4]) + "/" + str(file[5]))

def main():
    course_data = [] 
    with open(CSV_File,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row != []:
                course_data.append(row)
    no_of_files = 0
    while True:
        if len(os.listdir(Downloads))>no_of_files:
            file_names = scan_sort(course_data)
            for file in file_names:
                check_file_tree(file)
                move_file_rename(file)
            no_of_files = len(os.listdir(Downloads))
        if len(os.listdir(Downloads))<no_of_files:
            no_of_files = len(os.listdir(Downloads))
        else:
            sleep(60)



if __name__ == '__main__':
    main()



