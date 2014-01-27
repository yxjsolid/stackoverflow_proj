# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.panelMain, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomIn = wx.Button( self.m_panel4, wx.ID_ANY, u"Zoom In", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.bZoomIn, 0, wx.ALL, 5 )
		
		self.bReset = wx.Button( self.m_panel4, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.bReset, 0, wx.ALL, 5 )
		
		self.bZoomOut = wx.Button( self.m_panel4, wx.ID_ANY, u"Zoom Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.bZoomOut, 0, wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( bSizer3 )
		self.m_panel4.Layout()
		bSizer3.Fit( self.m_panel4 )
		fgSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bZoomIn.Bind( wx.EVT_BUTTON, self.onZoomIn )
		self.bReset.Bind( wx.EVT_BUTTON, self.onReset )
		self.bZoomOut.Bind( wx.EVT_BUTTON, self.onZoomOut )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onZoomIn( self, event ):
		event.Skip()
	
	def onReset( self, event ):
		event.Skip()
	
	def onZoomOut( self, event ):
		event.Skip()
	

