
import wx

class Notes(wx.Frame):
    """
    A Frame that says Hello World
    """



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
        return self.loc1
    def info2(self):
        return self.loc2

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


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = Notes(None, title='Notes Sharing')
    frm.Show()
    app.MainLoop()
    #Storage Location
    loc1 = frm.info1()
    #Download Location
    loc2 = frm.info2()
    print(loc1, loc2)
