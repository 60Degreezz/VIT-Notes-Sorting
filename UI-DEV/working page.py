import os
import shutil
import csv
from time import sleep
import wx
import sys
import appdirs

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

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap(os.path.join(sys.path[0], "D:\Offline_Projects\GIT\VIT-Notes-Sorting" + "/icon.png")))
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
        workItem = helpMenu.Append(-1, "How it works")
        
        
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
        self.Bind(wx.EVT_MENU, self.OnWork, workItem)

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
    def OnWork(self,event):
        """Display an About Dialog"""
        wx.MessageBox("To see the functioning of this neat application go to this link: \n https://github.com/60Degrees/VIT-Notes-Sorting/")

def main():
    app = wx.App()
    frm = Notes(None, title='Notes Sharing')
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


