import os
import shutil, csv
from time import sleep
import wx
import sys

Download_Loc = ''
Sorting_Loc = ''
Project_Dir = os.getcwd()

def Read_CSV():
    global Project_Dir
    course_data = []
    with open('Course_List.csv','r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            if row !=[]:
                course_data.append(row)
    return(course_data)

def Scan_Sort():
    sorted_files = []
    download_list = os.listdir(Download_Loc)
    for filename in download_list:
        if(filename[0:7] == 'FALLSEM' or filename[0:6] == 'WINSEM'):
            sorted_files.append(filename)
    return(sorted_files)

def Classify_Split_Files(course_data, sorted_files):
    split_files = []
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
        for i in range(7,len(file_split)-1,1):
            name += file_split[i] + ' '
        name += file_split[6] + '.' + file_split[len(file_split)-1]
        file_details.append(name)
        date = file_split[7]
        file_details.append(date)
        split_files.append(file_details)
    return(split_files)

def Folder_Check_Create(split_files):
    current_dir = Sorting_Loc
    folder_list = os.listdir(current_dir)
    if 'VIT_NOTES' not in folder_list:
        os.mkdir('VIT_NOTES')
    current_dir += '/VIT_NOTES/'
    os.chdir(current_dir)
    for file in split_files:
        folder_list = os.listdir(current_dir)
        if file[2] not in folder_list:
            os.chdir(current_dir)
            os.mkdir(file[2])
            os.chdir(current_dir + str(file[2]))
            os.mkdir("Fall_Sem")
            os.mkdir("Win_Sem")
        os.chdir(current_dir + str(file[2]) + '/' + str(file[1]))
        sub_list = os.listdir()
        if file[3] not in sub_list:
            os.mkdir(file[3])
        os.chdir(current_dir + str(file[2]) + "/" + str(file[1]) + "/" + file[3])
        topic_list = os.listdir()
        if file[4] not in topic_list:
            os.mkdir(file[4])

def Move_Replace(split_files):
    for file in split_files:
        move_folder = Sorting_Loc + '/VIT_NOTES/' + str(file[2]) + "/" + str(file[1]) + "/" + str(file[3]) + "/" + str(file[4])
        file_duplication_check = os.listdir(move_folder)
        if str(file[5]) in file_duplication_check:
            os.chdir(move_folder)
            try:
                os.remove(str(file[5]))
            except:
                continue
        try:
            shutil.move(Download_Loc + "/" + file[0], move_folder + "/" + str(file[5]))
        except:
                continue    



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

        """# put some text with a larger bold font on it
        st = wx.StaticText(panel, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)



        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        panel.SetSizer(sizer)"""

        #Show DieDialog-1 button
        dirDlgBtn1 = wx.Button(panel, label="Browse" , id = 1 )
        sizer.Add(dirDlgBtn1, pos=(1, 14), flag=wx.TOP|wx.RIGHT, border=5)
        dirDlgBtn1.Bind(wx.EVT_BUTTON, self.onDir , dirDlgBtn1)

        #Storage location-1
        text2 = wx.StaticText(panel, label="Storage Location")
        sizer.Add(text2, pos=(1, 0), flag=wx.LEFT|wx.TOP, border=10)

        #Panel-1 next to Storage location
        #will display the file location here
        self.tc1 = wx.TextCtrl(panel, value = "Default")
        sizer.Add(self.tc1, pos=(1, 1), span=(1, 13), flag=wx.TOP|wx.EXPAND,border=5)

        #Show DieDialog-2 button
        dirDlgBtn2 = wx.Button(panel, label="Browse" , id = 2)
        sizer.Add(dirDlgBtn2, pos=(2, 14), flag=wx.TOP|wx.RIGHT, border=5)
        dirDlgBtn2.Bind(wx.EVT_BUTTON, self.onDir)

        #Storage location-2
        text3 = wx.StaticText(panel, label="Download Location")
        sizer.Add(text3, pos=(2, 0), flag=wx.LEFT|wx.TOP, border=10)

        #Panel-2 next to Storage location
        #will display the file location here
        self.tc2 = wx.TextCtrl(panel, value = "Default")
        sizer.Add(self.tc2, pos=(2, 1), span=(1, 13), flag=wx.TOP|wx.EXPAND,border=5)




        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Still in trial")


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
        helloItem = fileMenu.Append(-1, "&ComingSoon\tCtrl-H","Under Development")
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
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def info1(self):
        return str(self.loc1)
    def info2(self):
        return str(self.loc2)

    def OnExit(self, event):
        """Close the frame, terminating the application."""

        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Under Develpoment")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("Under Development",
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
    try:
        os.chdir(Accepted_Download_Loc)
        os.chdir(Project_Dir)
    except:
        Accepted_Download_Loc += '/'
    try:
        os.chdir(Accepted_Sorting_Loc)
        os.chdir(Project_Dir)
    except:
        Accepted_Sorting_Loc += '/'
    temp_data=[['Start',''],['Download',Accepted_Download_Loc],['Sorting',Accepted_Sorting_Loc]] + course_data
    os.chdir(Project_Dir)
    with open('Course_List.csv','w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(temp_data)
    main()


def main():
    global Download_Loc, Sorting_Loc, Project_Dir
    Project_Dir = os.getcwd()
    course_data = Read_CSV()
    download_file_no = 0
    while True:
        if course_data[1][0] == 'default':
            UI_Accept_Address(course_data)
        else:
            Download_Loc = course_data[1][1]
            Sorting_Loc = course_data[2][1]
        if len(os.listdir(Download_Loc))>download_file_no:
            sorted_files = Scan_Sort()
            split_files = Classify_Split_Files(course_data, sorted_files)
            Folder_Check_Create(split_files)
            Move_Replace(split_files)
            download_file_no = len(os.listdir(Download_Loc))
        if len(os.listdir(Download_Loc))<download_file_no:
            download_file_no= len(os.listdir(Download_Loc))
        else:
            os.chdir(Project_Dir)
            sleep(60)
    
    
if __name__=='__main__':
    main()
