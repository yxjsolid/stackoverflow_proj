import wx
import pygame
from MySprite import *
from pygame.locals import *

#from import noname.py *

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent, fSize ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = fSize, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.AddGrowableRow( 0 )
        fgSizer1.SetFlexibleDirection( wx.VERTICAL )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )


        self.panelMain = MyHmiPanel(self, -1)

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
        self.bReset.Bind( wx.EVT_BUTTON, self.onZoomReset )
        self.bZoomOut.Bind( wx.EVT_BUTTON, self.onZoomOut )

    def __del__( self ):
        pass

    def onZoomIn( self, event ):
        self.panelMain.onZoomIn()
        event.Skip()

    def onZoomReset( self, event ):
        self.panelMain.onZoomReset()
        event.Skip()

    def onZoomOut( self, event ):
        self.panelMain.onZoomOut()
        event.Skip()


class MyHmiPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.parent = parent
        self.hwnd = self.GetHandle()
        self.size = self.GetSizeTuple()
        self.size_dirty = True
        self.rootSpriteGroup = pygame.sprite.LayeredUpdates()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.fps = 60.0
        self.timespacing = 1000.0 / self.fps
        self.timer.Start(self.timespacing, False)
        self.previous_time = 0
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

        self.selectedSprite = None

        self.zoomRatio = 1
        self.background = None
        self.bgRect = None
        self.backgroundOnUpdate = None
        self.bgRetOnUpdate = None

        self.loadBackground()
        self.addTestSprite()

    def loadBackground(self):
        self.background = pygame.image.load(image_bg)
        self.bgRect = self.background.get_rect()

        self.backgroundOnUpdate = self.background.copy()
        self.bgRetOnUpdate = self.bgRect.copy()

    def resizeUpdateBackground(self):
        self.bgRect.center = self.screen.get_rect().center
        self.bgRetOnUpdate = self.bgRect.copy()

    def zoomUpdateBackground(self, zoomRatio):
        self.bgRetOnUpdate.width = self.bgRect.width * zoomRatio
        self.bgRetOnUpdate.height = self.bgRect.height * zoomRatio
        self.bgRetOnUpdate.width = self.bgRect.width * zoomRatio
        self.bgRetOnUpdate.center = self.screen.get_rect().center
        self.backgroundOnUpdate = pygame.transform.scale(self.background, (self.bgRetOnUpdate.width, self.bgRetOnUpdate.height))

    def drawBackground(self, screen):
        screen.blit(self.backgroundOnUpdate, self.bgRetOnUpdate)

    def addTestSprite(self):
        self.rootSpriteGroup.add(ButtonSprite(self, initPos=(100, 100), width=100, height=100, dicts= [('on', btn_green_on), ('off', btn_green_off)]))
        self.rootSpriteGroup.add(ButtonSprite(self, initPos=(200, 200), width=100, height=100, dicts= [('on', btn_red_on), ('off', btn_red_off)]))

    def Update(self, event):
        self.Redraw()
        return

    def Redraw(self):
        if  self.size[0] == 0  or  self.size[1] == 0:
            print "MyHmiPanel.Redraw", self.size
            return

        if self.size_dirty:
            self.screen = pygame.Surface(self.size, 0, 32)
            self.resizeUpdateBackground()
            self.size_dirty = False

        self.screen.fill((0,0,0))
        self.drawBackground(self.screen)

        w, h = self.screen.get_size()
        current_time = pygame.time.get_ticks()

        self.previous_time = current_time
        self.rootSpriteGroup.update(current_time, self.zoomRatio)
        self.rootSpriteGroup.draw(self.screen)

        s = pygame.image.tostring(self.screen, 'RGB')  # Convert the surface to an RGB string
        #img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image
        img = wx.ImageFromData(w, h, s)  # Load this string into a wx image

        #if img.IsOk() is not True:
           # return
        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        dc = wx.BufferedDC( dc)
        dc.DrawBitmap(bmp, 0, 0, 1)  # Blit the bitmap image to the display


    def checkCollide(self, event):
        x , y = (event.GetX(),event.GetY())

        mousePoint = pygame.sprite.Sprite()
        mousePoint.rect = pygame.Rect(x, y, 1, 1)
        #copoint = pygame.sprite.spritecollideany(mousePoint, self.rootSpriteGroup)
        copoint = pygame.sprite.spritecollide(mousePoint, self.rootSpriteGroup, None)

        if copoint:
            copoint = copoint[-1]

        return copoint

    def removeSelectedSprite(self):
        if self.selectedSprite:
            self.selectedSprite.setSelect(0)
            self.selectedSprite = None

    def setNewSelectedSprite(self, sprite):
        self.removeSelectedSprite()
        sprite.setSelect(1)
        self.selectedSprite = sprite

    def onSelectSprite(self, event, onMouseObj):
        if onMouseObj:
            if self.selectedSprite:
                if onMouseObj != self.selectedSprite:
                    self.setNewSelectedSprite(onMouseObj)
            else:
                self.setNewSelectedSprite(onMouseObj)

            self.selectedSprite.setLastPos((event.GetX(),event.GetY()))
        else:
            self.removeSelectedSprite()


    def OnMouse(self, event):
        onMouseObj = self.checkCollide(event)
        event.Skip()

        if onMouseObj:
            onMouseObj.OnMouseHandler(event)

        if not event.GetSkipped():
            print "event dropped "
            return

        if event.LeftDown():
            self.onSelectSprite(event, onMouseObj)
        elif event.LeftUp():
            pass
        elif event.RightUp():
            self.onSelectSprite(event, onMouseObj)
        elif event.RightDown():
            self.onSelectSprite(event, onMouseObj)
        elif event.Dragging() and event.LeftIsDown():
            if self.selectedSprite:
                self.selectedSprite.move((event.GetX(),event.GetY()))

    def OnPaint(self, event):
        self.Redraw()
        event.Skip()  # Make sure the parent frame gets told to redraw as well

    def OnSize(self, event):
        self.size = self.GetSizeTuple()
        self.size_dirty = True

    def Kill(self, event):
        self.Unbind(event=wx.EVT_PAINT, handler=self.OnPaint)
        self.Unbind(event=wx.EVT_TIMER, handler=self.Update, source=self.timer)

    def onZoomIn(self):
        self.zoomRatio += 0.2
        self.onZoomUpdate()

    def onZoomReset(self):
        self.zoomRatio = 1
        self.onZoomUpdate()

    def onZoomOut(self):
        if self.zoomRatio > 0.2:
            self.zoomRatio -= 0.2
        self.onZoomUpdate()

    def onZoomUpdate(self):
        self.zoomUpdateBackground(self.zoomRatio)
        for s in self.rootSpriteGroup.sprites():
            s.onZoomUpdate(self.zoomRatio)


if __name__=='__main__':
        app = wx.App(redirect=False)
        frame = MyFrame1(None, (800, 600))
        frame.SetPosition((100, 100))
        frame.Show()
        app.MainLoop()