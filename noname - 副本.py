# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 430,386 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        fgSizer5 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid1 = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelSize( 30 )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelSize( 80 )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        self.m_grid1.EnableScrolling(1,1)
        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer29.Add( self.m_grid1, 0, 0, 0 )


        self.m_panel12.SetSizer( bSizer29 )
        self.m_panel12.Layout()
        bSizer29.Fit( self.m_panel12 )
        fgSizer5.Add( self.m_panel12, 1, wx.ALL|wx.EXPAND, 0 )

        self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer18 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid2 = wx.grid.Grid( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid2.CreateGrid( 10, 5 )
        self.m_grid2.EnableEditing( True )
        self.m_grid2.EnableGridLines( True )
        self.m_grid2.EnableDragGridSize( False )
        self.m_grid2.SetMargins( 0, 0 )

        # Columns
        self.m_grid2.EnableDragColMove( False )
        self.m_grid2.EnableDragColSize( True )
        self.m_grid2.SetColLabelSize( 0 )
        self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.m_grid2.EnableDragRowSize( True )
        self.m_grid2.SetRowLabelSize( 80 )
        self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer18.Add( self.m_grid2, 0, wx.EXPAND, 0 )


        self.m_panel10.SetSizer( bSizer18 )
        self.m_panel10.Layout()
        bSizer18.Fit( self.m_panel10 )
        fgSizer5.Add( self.m_panel10, 1, wx.ALL|wx.EXPAND, 0 )


        self.m_grid2.Bind(wx.EVT_SCROLLWIN, self.OnScroll_2)
        self.m_grid1.Bind(wx.EVT_SCROLLWIN, self.OnScroll_1)

        self.SetSizer( fgSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    def OnScroll_1(self,evt):
        print "11111"
        print self.m_grid2.Scroll(10, 10)
        print self.m_grid1.Scroll(10,10)
        evt.Skip()

    def OnScroll_2(self,evt):
        print "2222"
        self.m_grid1.EnableScrolling(1,1)
        print self.m_grid2.Scroll(10, 10)
        print self.m_grid1.Scroll(-1,5)


        self.m_grid1.GetEventHandler().ProcessEvent(evt)
        self.m_grid1.Layout()
        self.m_grid1.ForceRefresh()
        self.m_grid1.Refresh()
        evt.Skip()

