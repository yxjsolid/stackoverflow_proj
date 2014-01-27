import cStringIO, base64
import pygame
from pygame.locals import *
from math import pi
from PIL import Image
# from MyMiddleWare import *
#from MyGlobal import *
#import MyMiddleWare
#from MiddleWare_Widget_Setting import *


rescoure_dir = r".\image\\"

btn_red_off = rescoure_dir + r"red_up.png"
btn_red_on = rescoure_dir + "red_down.png"

btn_green_off = rescoure_dir + "green_up.png"
btn_green_on = rescoure_dir + "green_down.png"

btn_on = rescoure_dir + "btn_on.png"
btn_off = rescoure_dir + "btn_off.png"

circle_btn_on = rescoure_dir + "circle_btn_on.png"
circle_btn_off = rescoure_dir + "circle_btn_off.png"

image_fish = rescoure_dir + "fugu.png"

image_bg = rescoure_dir + "bg.jpg"


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
 

#help( SMALL_FONT)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)




class Ball(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)
        ball_file = cStringIO.StringIO(base64.decodestring(
"""iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJ
bWFnZVJlYWR5ccllPAAABBJJREFUeNqsVj2PG1UUvfPp8XictXfHa+9mlyJCNEQRWiToqACJAgGC
LqJNlQZR0IFEj8RPSJkGGooUpEWJkGhR0tAAElI2tsfjjxnPjIdz7oyDF2wSUK72yN43793z7rkf
Y8N2HFmbbVliGIYiyzIpy1Isy3oHeMswzLOyXJ2tVit9VhTFAxz5Cfge+A7IZIcZmySObQudwIE0
veanraB1w/O8l5x6D9eXy6UkSaJYLBa6BvsNuAV8uY3sCQlvX4LANM0Xw/Dgdhj2Xm02m+K6LqPR
PXmeS5qmMp/PZTabyXQ6lclkosS1/QJcB+5vkthrAkoAuc4uHx//0B8MvCAIxG/5jEg0kpIkmcwX
icTxBIhlHWEURXoedgW4B3wIfHuBJM9yMQ3j5PTk5N7g6MjtdrrS3e9Ku90GUUvc2hkdMYJx5Ivn
NRC19UReRlRLR/sGeB34UUkMJBcJlcHg6K4SdDvS7/el1+tJp7MnQdCWRqMhDGWZLmWCCFog9rBm
GBYc50rOKON4uqkSC+IQSC3moeX7N09PX/i4AwLkAoQDxeFhHziU8CCUzt6e+EFLc2QaJi4mFQHy
kQLZMpME+WJF1sabdYA7Nq4jQbv9OZPs+75cgkSMYH9/X6PhJ9dpTLjruFLkBRyjACBd1BoLzzY8
T3O0IRntJvCZDXsTTnq262CzrzmgRHu4+QEIQhAxNzRWU1mTxfjOwvBIAOlIYNnWtja5bqM33mN/
sBEdx9bNPOQ1PWlqZJdAFKoMrEI6R+9gj6t7cUl1zjKnjFvsfaybr1Uqlv94ypXSKCud+aefpezs
7O3LL9s4c5U65gCrhGDDpUkqyWIuU1STweNlJRe7nAlmA+ZaVbnmiD4KFNEWC+3VqjB5YImDdMA+
YKONx2OVgxefojRL8CzmCxkOhxLhWYy+mGIvz6RKmv096X91PErP4Byazapbs3vZB45bVQqTzBzQ
kjQBQSTnjx7JcDTCRSLkKNY9SbKACsttHKZdrIqHILnGCNhoDU0qG83U5mNUVTOKShRPYo3m8fAc
nT/S/3mWFy2KrXKNOFbuI+Rr1FvLsB731Ho2m2pU7I1Sx8pSHTLaESIZjob6nfso2w77mSR3IMsN
zh4mmLOIBAkO6fjAgESdV1MYiV4kiUZHRDjD3E0Qza580D+rjsUdAQEj4fRl8wUkqBttPeo5RlJI
uB71jIASc8D+i4W8IoX8CviC5cuI+JlgpLsgcF1ng6RQyaoX1oWX1i67DTxe9w+9/EHW9VOrngCW
ZfNFpmvVWOfUzZ/mfG0HwHBz4ZV1kz8nvLuL+YPnRPDJ00J8A/j9fzrnW+sjeUbjbP8amDyj86z+
tXL5PwzOC4njj4K3gavA8cazczYacLd+p/+6y8mfAgwAsRuLfp/zVLMAAAAASUVORK5CYII="""))

#        screen = pygame.display.set_mode([350, 350])
        
        image = pygame.image.load(ball_file, 'file')



        print "aaaaaaaaaaaaaaa", image
        
        print image.get_size()


        self.imagestr = pygame.image.tostring(image, "RGBA")
        

        self.image = pygame.image.fromstring(self.imagestr, (25, 25), "RGBA")


        #self.image = pygame.image.load(ball_file, 'file').convert_alpha()
       # 
        #print self.image

        self.rect = self.image.fill(color, None, BLEND_ADD)
        self.rect.topleft = initial_position

        print "self.rect", self.rect
       


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

                self.rect =  pygame.Rect(0,0,W,H)
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


def drawBoader1(image, rect):
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

            self.initPos = (initPos[0], initPos[1])
            self.width = width
            self.height = height
            self.rectOrig = pygame.Rect(initPos, (width, height))
            self.rect = self.rectOrig.copy()

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

        def loadImgResource1(self, file):
            """
                load image with PIL lib
            """
            im = Image.open(file)
            im = im.resize((self.width, self.height))
            imagedata = im.convert('RGBA').tostring()
            imagesize = im.size
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")

        def loadImgResource2(self, dicKey, file):
            """
                load image with pygame lib
            """
            image_file = pygame.image.load(file)
            imagedata = pygame.image.tostring(image_file, "RGBA")
            imagesize = image_file.get_size()
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")
            #imageS1.fill(color, None, BLEND_ADD)
            #imageSurface = pygame.transform.smoothscale(imageSurface,(self.width, self.height))
            #self.imageResource.append(imageSurface)
            self.imageResource[dicKey] = imageSurface

        def loadImgResource(self, dict):
            """
                load image with pygame lib
            """
            key = dict[0]
            file_name = dict[1]

            image_file = pygame.image.load(file_name)
            imagedata = pygame.image.tostring(image_file, "RGBA")
            imagesize = image_file.get_size()
            imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")

            #x = max(imagesize[0], imagesize[1])
            #newImg = pygame.Rect((0,0), (x, x))
            #imageS1.fill(color, None, BLEND_ADD)
            #imageSurface = pygame.transform.smoothscale(imageSurface,(self.width, self.height))
            #self.imageResource.append(imageSurface)
            self.imageResource[key] = (file_name, imageSurface)

        def resizeResource(self, src, size):
            return pygame.transform.smoothscale(src, size)

        def setCurrentResource(self, status):
            self.currentStatus = status

            self.imageOrig = self.resizeResource(self.imageResource[status][1], (self.width, self.height))
            self.image = self.imageOrig.copy()
           # self.rect = self.image.get_rect().copy()

        def switchResource(self, index):
            self.setCurrentResource(index)


        def onZoomUpdate(self, parent, ratio):
            #self.rect.x *= ratio
           #self.rect.y *= ratio

            parentRect = pygame.Rect(parent.GetRect())


            dx = self.rectOrig.centerx - parentRect.centerx
            dy = self.rectOrig.centery - parentRect.centery

            self.rect.centerx = parentRect.centerx + dx*ratio
            self.rect.centery = parentRect.centery + dy*ratio

            #self.rect.centery *= ratio
            print "onZoomUpdate"
            #pygame.Rect

        def update(self, current_time, ratio):
            # return
            # if current_time - self.lastUpdate > 500:
            #     self.lastUpdate = current_time
            #     self.status = ~(self.status)
            #     self.switchResource(self.status)

            rectTmp = self.rectOrig

           #pygame.Rect

            #print self.rect, self.rect.center

            if self.isSelected():
                # print "buttonSprite selected"
                drawBoader1(self.image, self.image.get_rect())
            else:
                self.image = self.imageOrig.copy()


                #self.image = pygame.transform.scale(self.imageOrig, (int(self.width*ratio), int(self.height*ratio)))



                #self.rect

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
            dx = pos[0] - self.lastPos[0]
            dy = pos[1] - self.lastPos[1]
            DragSprite.move(self, pos)



