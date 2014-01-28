
import pygame

from res import *
from pygame.locals import *
from wx.lib.embeddedimage import PyEmbeddedImage
from math import pi
from PIL import Image



pygame.font.init()
try:
    regular_font_file = os.path.join(os.path.dirname(__file__), "Vera.ttf")
    bold_font_file = os.path.join(os.path.dirname(__file__), "VeraBd.ttf")

    # Check for cx_Freeze
    #
    if "frozen" in sys.__dict__.keys() and sys.frozen:

        regular_font_file = os.path.join(sys.path[1], "Vera.ttf")
        bold_font_file = os.path.join(sys.path[1], "VeraBd.ttf")

    BIG_FONT = pygame.font.Font(regular_font_file, 30)
    SMALL_FONT = pygame.font.Font(regular_font_file, 12)
    BOLD_FONT = pygame.font.Font(bold_font_file, 12)

except:
    # TODO: log used font: pygame.font.get_default_font()
    #print("Could not load {0}".format(os.path.join(os.path.dirname(__file__), "Vera.ttf")))
    BIG_FONT = pygame.font.Font(None, 40)
    SMALL_FONT = BOLD_FONT = pygame.font.Font(None, 20)
 





class PyGamePseudoImage():
    def __init__(self, size, color):
        self.screen = pygame.Surface(size, 0, 32)
        self.screen.fill(color)

    def getImage(self):
        return self.screen



class __MouseMixin:

    def onLeftUp(self, event):
        #print "onLeftUp"
        pass

    def onLeftDown(self, event):
        #print "onLeftDown"
        pass

    def onLeftDClick(self, event):
        #print "onLeftDClick"
        pass

    def onRightUp(self, event):
        #print "onRightUp"
        pass

    def onRightDown(self, event):
        #print "onRightDown"
        pass

    def onDragging(self, event):
        #print "onDragging"
        pass

    def onMouseEnter(self, event):
        #print "onMouseEnter"
        pass

    def OnMouseHandler(self, event):
        #print "OnMouseHandler"
        event.Skip()

        if event.LeftUp():
            self.onLeftUp(event)
        elif event.LeftDown():
            self.onLeftDown(event)
        elif event.LeftDClick():
            self.onLeftDClick(event)
        elif event.RightUp():
            self.onRightUp(event)
        elif event.RightDown():
            self.onRightDown(event)
        elif event.Dragging() and event.LeftIsDown():
            self.onDragging(event)

        pass


class DragSprite(__MouseMixin, pygame.sprite.Sprite):
    SPRITE_BUTTON, SPRITE_TRANSPORTER = range(2)

    def __init__(self, parent=None):
        pygame.sprite.Sprite.__init__(self)
        self.is_select = 0
        self.lastPos = 0
        self.lastUpdate = 0
        self.parent = parent

    def setLastPos(self, pos):
        self.lastPos = pos

    def move(self, pos):
        dx = pos[0] - self.lastPos[0]
        dy = pos[1] - self.lastPos[1]
        self.lastPos = pos
        center = (self.rect.center[0] + dx, self.rect.center[1] + dy)
        self.rect.center = center

        return

    def isSelected(self):
        return self.is_select

    def setSelect(self, is_select):

        self.is_select = is_select
        return
         
        pad = 8
        center = self.rect.center

        if is_select:
            if not self.is_select:
                self.is_select = 1
                W,H = (self.rect.width, self.rect.height)
                W += pad
                H += pad
                self.image = pygame.Surface((W,H), pygame.SRCALPHA, 32)
                yellow = (255, 255, 0)
                
                pygame.draw.rect(self.image, yellow, (0,0,W-1,H-1), 2)
                pygame.Surface.blit(self.image, self.imageOrig, (pad/2,pad/2,W-pad,H-pad))

                self.rect = pygame.Rect(0,0,W,H)
                self.rect.center = center
        else:
            self.is_select = 0
            self.recovery()
           
    def recovery(self):
        self.image = self.imageOrig.copy()
        center = self.rect.center
        self.rect = self.rectOrig.copy()

    def update(self, current_time):
        return


def drawBoader(image, rect):
    W,H = (rect.width, rect.height)
    yellow = (255, 255, 0)
    pygame.draw.rect(image, yellow, (0,0,W-2,H-2), 2)


class ButtonSprite(DragSprite):
        def __init__(self, parent=None, initPos=(0,0), width=50, height=50, dicts=None):
            DragSprite.__init__(self, parent)
            self.type = DragSprite.SPRITE_BUTTON
            self.resourceCfgDict = dicts
            self.imageResource = {}
            self.status = 0
            self.index = 0

            self.parent = parent
            self.initPos = (initPos[0], initPos[1])
            self.width = width
            self.height = height
            self.rectOnLoad = pygame.Rect(initPos, (width, height))
            self.rect = self.rectOnLoad.copy()

            self.operationOn = None
            self.operationOff = None

            self.operationDic = {"on": self.getOperationOnItem, "off": self.getOperationOffItem}
            self.guiCfg = None


            for dic in dicts:
                self.loadImgResource(dic)

            self.setCurrentResource("off")

        def getOperationOnItem(self):
            return self.operationOn

        def getOperationOffItem(self):
            return self.operationOff


        def loadImgResource(self, dict):
            """
                load image with pygame lib
            """
            key = dict[0]
            file_name = dict[1]


            #image_file = pygame.image.load(file_name) #use this to load real image
            image_file = PyGamePseudoImage((500,500), file_name).getImage()
            imagedata = pygame.image.tostring(image_file, "RGBA")
            imagesize = image_file.get_size()
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")

            self.imageResource[key] = (file_name, imageSurface)

        def resizeResource(self, src, size):
            return pygame.transform.smoothscale(src, size)

        def setCurrentResource(self, status):
            self.currentStatus = status
            self.imageOnLoad = self.resizeResource(self.imageResource[status][1], (self.width, self.height))
            self.image = pygame.transform.scale(self.imageOnLoad, (self.rect.width, self.rect.height))

        def switchResource(self, index):
            self.setCurrentResource(index)

        def onZoomUpdate(self, zoomRatio):
            parentRect = pygame.Rect(self.parent.GetRect())
            dx = self.rectOnLoad.centerx - parentRect.centerx
            dy = self.rectOnLoad.centery - parentRect.centery

            self.rect.centerx = parentRect.centerx + dx*zoomRatio
            self.rect.centery = parentRect.centery + dy*zoomRatio

            self.rect.height = self.imageOnLoad.get_rect().height * zoomRatio
            self.rect.width = self.imageOnLoad.get_rect().width * zoomRatio

            self.image = pygame.transform.scale(self.imageOnLoad, (self.rect.width, self.rect.height))

        def update(self, current_time, ratio):
            if self.isSelected():
                drawBoader(self.image, self.image.get_rect())
            else:
                pass
                #self.image = self.imageOnLoad.copy()

        def onRightUp(self, event):
            print "onRightUp"
            event.Skip(False)
            pass

        def onLeftDClick(self, event):
            if self.currentStatus == "on":
                self.setCurrentResource("off")
            elif self.currentStatus == "off":
                self.setCurrentResource("on")

            return

        def move(self, pos):
            DragSprite.move(self, pos)

            parentRect = pygame.Rect(self.parent.GetRect())
            centerDx = self.rect.centerx - parentRect.centerx
            centerDy = self.rect.centery - parentRect.centery

            self.rectOnLoad.centerx = parentRect.centerx + centerDx/self.parent.zoomRatio
            self.rectOnLoad.centery = parentRect.centery + centerDy/self.parent.zoomRatio
