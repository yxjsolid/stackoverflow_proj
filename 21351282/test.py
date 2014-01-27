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

        #self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )


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
        self.bReset.Bind( wx.EVT_BUTTON, self.onReset )
        self.bZoomOut.Bind( wx.EVT_BUTTON, self.onZoomOut )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onZoomIn( self, event ):
        self.panelMain.onZoomIn()
        event.Skip()

    def onReset( self, event ):
        self.panelMain.onReset()
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
        #self.timer.Start(5000, False)

        self.linespacing = 5
        # self.addTestSprite()

        self.zoomRatio = 1

        self.previous_time = 0
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)


        self.selectedSprite = None
        #self.SetDoubleBuffered(True)
        #testRSizedWidget(self)

        print self.size



        self.addTestSprite()

    def loadBG(self, screen):
        parentRect = pygame.Rect(self.GetRect())
        background = pygame.image.load(image_bg)
        bgRect = background.get_rect()
        #pygame.transform.scale(background, (1200,800))  #or some size x,y here.

        size = width, height = bgRect.width, bgRect.height

        #bgRect.center = parentRect.center
        bgRect.width *= self.zoomRatio
        bgRect.height *= self.zoomRatio
        bgRect.center = screen.get_rect().center

        bd = pygame.transform.scale(background, (bgRect.width,bgRect.height))
        screen.blit(bd, bgRect)


    def addSpriteToPanel(self, sprite):
        sprite.parent = self
        self.rootSpriteGroup.add(sprite, layer=12)

    def addTestSprite(self):

        """
        for color, location, speed in [([255, 0, 0], [50, 50], [2,3]),
                                       ([0, 255, 0], [100, 100], [3,2]),
                                       ([0, 0, 255], [150, 150], [4,3])]:
            self.rootSpriteGroup.add(MoveBall(color, location, speed, (350, 350)))
"""
        #self.rootSpriteGroup.add(test_Drag_Sprite([100, 100, 100], [200, 200], [5,6], (350, 350)))
        #self.rootSpriteGroup.add(Sprite_Button([200, 200, 200], [300, 400], [5,6], (350, 350)))
        #self.rootSpriteGroup.add(AnimateTansporterSprite([200, 200, 200], (150,150), 150,40,500,1))
        self.rootSpriteGroup.add(ButtonSprite(initPos=(100, 100), width=50, height=50, dicts= [('on', btn_green_on), ('off', btn_green_off)]))
        self.rootSpriteGroup.add(ButtonSprite(initPos=(200, 200), width=50, height=50, dicts= [('on', btn_red_on), ('off', btn_red_off)]))



        #ButtonSprite(initPos=(0, 0), width=x, height=y, dicts= [('on', on), ('off', off)])

        #self.rootSpriteGroup.add(specialSprite_transport([200, 200, 200], (100,100), 500,50,1,1))
        #self.addTestSprite()

    def addSpritePerformanceTest(self):
        rowMax = 10
        colMax = 10
        x_i = 100
        y_i = 100

        width = 150
        height = 50

        for i in range(0,rowMax):
            for j in range(colMax):
                updateInterval = random.randint(300,2000)
                trans1 = AnimateTansporterSprite([200, 200, 200], (x_i + i*width +20, y_i + j*width), width,height,updateInterval,1)
                self.rootSpriteGroup.add(trans1)

    def Update(self, event):
        # Any update tasks would go here (moving sprites, advancing animation frames etc.)
        self.Redraw()

        if hasattr(self, 'testBtn'):
                #self.testBtn.Update()
            #self.testBtn.OnPaint(event)
            #self.testBtn.Update()
            #self.testBtn.Refresh()
            pass
        return




    def Redraw(self):
        #print "select page is HIM", self.GetParent().GetCurrentPage() is self
        #print "isEnabled", self.IsEnabled()
        #print "MyHmiPanel, Redraw"
        # return

        if  self.size[0] == 0  or  self.size[1] == 0:
            print "MyHmiPanel.Redraw", self.size
            return

        if self.size_dirty:
            self.screen = pygame.Surface(self.size, 0, 32)
            self.size_dirty = False

        self.screen.fill((0,0,0))

        self.loadBG(self.screen)

        cur = 0
        w, h = self.screen.get_size()

        # while cur <= h:
        #     pygame.draw.aaline(self.screen, (255, 255, 255), (0, h - cur), (cur, 0))
        #     cur += self.linespacing

        current_time = pygame.time.get_ticks()
        #print current_time
        #print "current_time - previous_time = ", current_time - self.previous_time

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

        if hasattr(self, 'testBtn'):
            #dddc = self.testBtn.OnDrawBtn()
            pass

            # (width, height) = self.GetClientSizeTuple()
            # (x,y) = self.testBtn.GetPositionTuple()
            #
            # dc.Blit(x,y,width,height, dddc, 0,0, useMask=True)

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
        mousePos = (event.GetX(),event.GetY())
        onMouseObj = self.checkCollide(event)
        #print "MyHmiPanel Mouse Event:", event
        event.Skip()

        if onMouseObj:
            onMouseObj.OnMouseHandler(event)


        #print "event.GetSkipped()", event.GetSkipped()

        if not event.GetSkipped():

            print "event dropped "
            return

        if event.LeftDown():
            #print "LeftDown",(event.GetX(),event.GetY())
            self.onSelectSprite(event, onMouseObj)
        elif event.LeftUp():
            #print "left up"
            pass

        elif event.RightUp():
            #print "RightUp"
            self.onSelectSprite(event, onMouseObj)
        elif event.RightDown():
            #print "RightDown",(event.GetX(),event.GetY())
            self.onSelectSprite(event, onMouseObj)

        elif event.Dragging() and event.LeftIsDown():
            #print "left Dragging", (event.GetX(),event.GetY())

            if self.selectedSprite:
                self.selectedSprite.move((event.GetX(),event.GetY()))

    def OnPaint(self, event):
        self.Redraw()
        event.Skip()  # Make sure the parent frame gets told to redraw as well

    def OnSize(self, event):
        self.size = self.GetSizeTuple()
        self.size_dirty = True

    def Kill(self, event):
        # Make sure Pygame can't be asked to redraw /before/ quitting by unbinding all methods which
        # call the Redraw() method
        # (Otherwise wx seems to call Draw between quitting Pygame and destroying the frame)
        # This may or may not be necessary now that Pygame is just drawing to surfaces
        self.Unbind(event=wx.EVT_PAINT, handler=self.OnPaint)
        self.Unbind(event=wx.EVT_TIMER, handler=self.Update, source=self.timer)



    def onZoomIn(self):
        self.zoomRatio += 0.2
        self.onZoomUpdate()



    def onReset(self):
        self.zoomRatio = 1
        self.onZoomUpdate()


    def onZoomOut(self):
        if self.zoomRatio > 0.2:
            self.zoomRatio -= 0.2

        self.onZoomUpdate()


    def onZoomUpdate(self):
        for s in self.rootSpriteGroup.sprites():
            s.onZoomUpdate(self, self.zoomRatio)


if __name__=='__main__':
        app = wx.App(redirect=False)
        # frame = wx.Frame(None, size=(1024,768))
        #
        # panel = MyHmiPanel(frame, -1)


        frame = MyFrame1(None, (1024, 768))
        
        frame.Show()
        app.MainLoop()