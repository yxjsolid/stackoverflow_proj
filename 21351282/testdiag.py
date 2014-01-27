import wx

class TestDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title='Test Dialog')

        sizer = wx.BoxSizer(wx.VERTICAL)

        message = wx.StaticText(self, wx.NewId(), 'This is some dummy text')
        sizer.Add(message)

        ok_button = wx.Button(self, wx.ID_OK, 'OK')
        cancel_button = wx.Button(self, wx.ID_CANCEL, 'Cancel')

        btn_sizer = self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL)
        btn_sizer.Add(cancel_button)
        btn_sizer.Add(ok_button)
        sizer.Add(btn_sizer)

        self.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestory)

    def OnClose(self, event):
        print 'In OnClose'
        event.Skip()

    def OnDestory(self, event):
        print 'In OnDestory'
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None)
    frame.Show()
    dialog = TestDialog(frame)

    dialog.Show()

    #result = dialog.ShowModal()
    #dialog.Close(True)
    #print 'Result: {}'.format(result)
    app.MainLoop()