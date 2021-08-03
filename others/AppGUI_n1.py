import wx

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="Hy Python")
        panel = wx.Panel(self)

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)

        my_btn = wx.Button(panel, label="Press here")
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
