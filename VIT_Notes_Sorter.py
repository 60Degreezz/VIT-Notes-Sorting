import os
import shutil
import csv
from time import sleep
import wx
import sys
import appdirs

'''
This program is written by Himanshu Savargaonkar :)

This program will startup when the computer is booted, will check your downloads folder for any updates every 1 min and sort the files in the VIT VTOP format.
Follow the following step to make that happen.


'''


Download_Loc = ''                #Download location 
Sorting_Loc = ''                 #Sorting file saving location
Project_Dir = ''        #Project Directory
AppData_Dir = ''
CSV_File = "/Course_List.csv"     #The location of the csv file


def Read_CSV():
    global Project_Dir, CSV_File
    course_data = []
    with open(CSV_File,'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            if row !=[]:
                course_data.append(row)
    return(course_data)
    
def Scan_Sort(course_data):                                                 #This function scans downloads and returns the list of files fitting VIT file format.
    sorted_files = []

    download_list = os.listdir(Download_Loc)
    for filename in download_list:
        if(filename[0:7] == 'FALLSEM' or filename[0:6] == 'WINSEM'):
            sorted_files.append(filename)
    classified_file_list = Divide_And_Sort(sorted_files,course_data)            #divide and sort function is called so the list is classified
    return classified_file_list

def Divide_And_Sort(sorted_files,course_data):                                       #This function accepts files one by one and makes a class object which has its (Year/Sem/SubCode/Type)
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
            file_details.append('')
        elif file_split[2] == 'LO':
            file_details.append('')
        elif file_split[2] == 'ETH':
            file_details.append("Embedded_Theory")
        elif file_split[2] == 'ELA':
            file_details.append('Embedded_Lab')
        else:
            file_details.append(file_split[2])
        name =''
        name += file_split[7] + ' '
        for i in range(8,len(file_split)-1):
            name +=file_split[i] + ' '
        name += '.' + file_split[len(file_split)-1]
        print(name)
        file_details.append(name)
        classified_files.append(file_details)
    return classified_files

def Check_File_Tree(file):                                          #Checks that the folder in which this file needs to be put exists. If not it creates that folder
    global Download_Loc, Sorting_Loc
    main_list = os.listdir(Sorting_Loc)
    if file[2] not in main_list:
        os.chdir(Sorting_Loc)
        os.mkdir(file[2])
        os.chdir(Sorting_Loc + str(file[2]))
        os.mkdir("Fall_Sem")
        os.mkdir("Win_Sem")
        os.chdir(Sorting_Loc + str(file[2]) + '/Fall_Sem')
        os.mkdir("1.Books")
        os.mkdir("2.Digital Assignments")
        os.mkdir("3.Syllabus")
        os.chdir(Sorting_Loc + str(file[2]) + '/Win_Sem')
        os.mkdir("1.Books")
        os.mkdir("2.Digital Assignments")
        os.mkdir("3.Syllabus")
    os.chdir(Sorting_Loc + str(file[2]) + '/' + str(file[1]))
    sub_list = os.listdir()
    if file[3] not in sub_list:
        os.mkdir(file[3])
    os.chdir(Sorting_Loc + str(file[2]) + "/" + str(file[1]) + "/" + file[3])
    topic_list = os.listdir()
    if file[4] not in topic_list and file[4]!='':
        os.mkdir(file[4])



def Move_File_Rename(file):                                         #Moves that file to its folder and renames the file as per its initial name
    file_duplication_check = os.listdir(Sorting_Loc + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4]))
    if str(file[5]) not in file_duplication_check:
        try:
            shutil.move(Download_Loc + "/" + file[0], Sorting_Loc + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4]) + "/" + str(file[5]))
        except:
            flag = 1
    else:
        try:
            os.remove(Sorting_Loc + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4]) + "/" + str(file[5]))
            shutil.move(Download_Loc + "/" + file[0], Sorting_Loc + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4]) + "/" + str(file[5]))
        except:
            flag = 1

class Notes(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Notes, self).__init__(*args, **kw)

        self.loc1="default"
        self.loc2="default"

        # create a panel in the frame
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(15, 15)

        text1 = wx.StaticText(panel, label="Notes-Sharing")
        sizer.Add(text1, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap(os.path.join(sys.path[0], Project_Dir + "/icon.png")))
        sizer.Add(icon, pos=(0, 8), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=5)

        text0 = wx.StaticText(panel, label="INSTRUCTIONS: \n\n Download Folder: The folder in which your notes get downloaded from VTOP" +
                              " \n\n Storage Folder: The folder in which you want your VTOP notes to be sorted into.")
        sizer.Add(text0, pos=(1,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)

        #Show DieDialog-2 button
        dirDlgBtn2 = wx.Button(panel, label="Browse" , id = 2)
        sizer.Add(dirDlgBtn2, pos=(2, 14), flag=wx.TOP|wx.RIGHT, border=5)
        dirDlgBtn2.Bind(wx.EVT_BUTTON, self.onDir)

        #Storage location-2
        text3 = wx.StaticText(panel, label="Download Folder ")
        sizer.Add(text3, pos=(2, 0), flag=wx.LEFT|wx.TOP, border=10)

        
        #Panel-2 next to Storage location
        #will display the file location here
        self.tc2 = wx.TextCtrl(panel, value = "Default")
        sizer.Add(self.tc2, pos=(2, 1), span=(1, 13), flag=wx.TOP|wx.EXPAND,border=5)


        #Show DieDialog-1 button
        dirDlgBtn1 = wx.Button(panel, label="Browse" , id = 1 )
        sizer.Add(dirDlgBtn1, pos=(3, 14), flag=wx.TOP|wx.RIGHT, border=5)
        dirDlgBtn1.Bind(wx.EVT_BUTTON, self.onDir , dirDlgBtn1)

        #Storage location-1
        text2 = wx.StaticText(panel, label="Storage Folder")
        sizer.Add(text2, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        
        #Panel-1 next to Storage location
        #will display the file location here
        self.tc1 = wx.TextCtrl(panel, value = "Default")
        sizer.Add(self.tc1, pos=(3, 1), span=(1, 13), flag=wx.TOP|wx.EXPAND,border=5)
        
        Okbtn = wx.Button(panel, label="OK")
        sizer.Add(Okbtn, pos=(4,13), flag=wx.LEFT|wx.TOP, border=5)
        Okbtn.Bind(wx.EVT_BUTTON, self.OnOk)

        Cancelbtn = wx.Button(panel, label="Cancel")
        sizer.Add(Cancelbtn, pos=(4,14), flag=wx.LEFT|wx.TOP, border=5)
        Cancelbtn.Bind(wx.EVT_BUTTON, self.OnExit)
        


        
        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("V1.0")
        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)

    #To get dir folder location
    def onDir(self, event):
            """
            Show the DirDialog and print the user's choice to stdout
            """
            dlg = wx.DirDialog(self, "Choose a directory:",
                               style=wx.DD_DEFAULT_STYLE
                               #| wx.DD_DIR_MUST_EXIST
                               #| wx.DD_CHANGE_DIR
                               )
            if dlg.ShowModal() == wx.ID_OK:
                #print("%s" %dlg.GetPath())
                btn = event.Id
                
                if btn == 1:
                    self.tc1.SetValue(str(dlg.GetPath()))
                    self.loc1 = str(dlg.GetPath())
                elif btn == 2:
                    self.tc2.SetValue(str(dlg.GetPath()))
                    self.loc2 = str(dlg.GetPath())
            dlg.Destroy()

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """
        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        futureitem = fileMenu.Append(-1, "&ComingSoon\tCtrl-H","Under Development \U0001f60E")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnFuture, futureitem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def info1(self):
        return self.loc1
    def info2(self):
        return self.loc2

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        global loc1,loc2
        loc1="default"
        loc2="default"
        self.Close(True)

    def OnOk(self,event):
        self.Close(True)

    def OnFuture(self, event):
        wx.MessageBox("Future updates will be Coming Soon \U0001f60E")

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a app for sorting files from download to a specified location \U0001f60E \nFor any issues and suggestions please submit in:\n\U000027A1https://github.com/60Degrees/VIT-Notes-Sorting/",
                      "About",
                      wx.OK|wx.ICON_INFORMATION)


def UI_Accept_Address(course_data):
    global Sorting_Loc, Download_Loc, Project_Dir
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.    
    app = wx.App()
    frm = Notes(None, title='Notes Sharing')
    frm.Show()
    app.MainLoop()
    #Storage Location
    Accepted_Sorting_Loc = str(frm.info1())
    #Download Location
    Accepted_Download_Loc = str(frm.info2())
    if (Accepted_Sorting_Loc=="default" or Accepted_Download_Loc=="default"):
        sys.exit()
    Accepted_Sorting_Loc += '/'
    Accepted_Download_Loc += '/'
    top_list = os.listdir(Accepted_Sorting_Loc)
    vit = "VIT_Sorted"
    if vit not in top_list:
        os.chdir(Accepted_Sorting_Loc)
        os.mkdir(vit)
    Accepted_Sorting_Loc += vit + "/"
    temp_data=[['Start',''],['Download',Accepted_Download_Loc],['Sorting',Accepted_Sorting_Loc]] + course_data
    os.chdir(Project_Dir)
    with open(CSV_File,'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(temp_data)
    

def init():
    global Download_Loc, Sorting_Loc, Project_Dir, AppData_Dir, CSV_File
    AppData_Dir = appdirs.user_data_dir()
    Project_Dir = os.getcwd()
    os.chdir(AppData_Dir)
    app_list = os.listdir(AppData_Dir)
    folder = 'VIT_Notes_Sorter'
    AppData_Dir = AppData_Dir + '/' + folder
    if folder not in app_list:
        os.mkdir(folder)
        scr = Project_Dir + CSV_File
        dest = AppData_Dir + CSV_File
        shutil.copy2(scr, dest)
    CSV_File = AppData_Dir + CSV_File

def main():
    global Download_Loc, Sorting_Loc, Project_Dir
    init()
    print(CSV_File)
    course_data = Read_CSV()
    no_of_files = 0 
    while True:
        if course_data[1][0] == 'default':
            UI_Accept_Address(course_data)
            course_data = Read_CSV()
            continue
        else:
            Download_Loc = course_data[1][1]
            Sorting_Loc = course_data[2][1]
        if len(os.listdir(Download_Loc))>no_of_files:
            file_names = Scan_Sort(course_data)
            for file in file_names:
                Check_File_Tree(file)
                Move_File_Rename(file)
            no_of_files = len(os.listdir(Download_Loc)) 
        if len(os.listdir(Download_Loc))<no_of_files:
            no_of_files = len(os.listdir(Download_Loc)) 
        else:
            os.chdir(Project_Dir)
            sleep(60)



if __name__ == '__main__':
    main()



