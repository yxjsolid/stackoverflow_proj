import wx
import wx.lib.scrolledpanel
from noname import *




class FrameTest(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

        self.m_grid1.SetRowLabelValue(0, "test")
        self.m_grid1.SetRowLabelValue(1, "test")
        self.m_grid1.SetRowLabelValue(2, "test")
        self.m_grid1.SetRowLabelValue(3, "test")
        self.m_grid1.SetRowLabelValue(4, "test")


       # self.m_grid2.SetScrollLineX(10)


        #SetScrollbars(self, int pixelsPerUnitX, int pixelsPerUnitY, int noUnitsX,
                                                                        #int noUnitsY, int xPos=0, int yPos=0, bool noRefresh=False)

        self.m_grid1.Scroll(2,2)
        self.m_grid2.Scroll(10,10)

        #self.m_grid1.SetupScrolling()
        self.m_grid1.SetAutoLayout(1)

        self.m_grid2.SetScrollbars(0,0,0,0,0,0,0)
        self.m_grid1.SetScrollbars(0,0,0,0,0,0,0)

        self.m_grid3.Bind(wx.EVT_SCROLLWIN, self.onScroll)


        #self.m_scrolledWindow1.ShowScrollbars(wx.SHOW_SB_NEVER,wx.SHOW_SB_DEFAUL)

        self.m_scrolledWindow1.SetScrollbars(0,0,0,0, noRefresh = True)
        self.m_scrolledWindow1.SetScrollRate( 0, 5 )
        #self.m_scrolledWindow1.EnableScrolling(0, 0)


    def onScroll(self, evt):
        print "onScroll"
        self.m_scrolledWindow1.GetEventHandler().ProcessEvent(evt)
        self.m_scrolledWindow1.Scroll(5,5)
        evt.Skip()

if __name__=='__main__':
        app = wx.App(redirect=False)
        frame = FrameTest(None)
        frame.Show()
        app.MainLoop()