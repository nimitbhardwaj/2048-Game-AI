from constant import *
import pygame
from color import colors
import copy


class Box(object):
    boxColors = {
                0: colors['antiquewhite3'],
                2: colors['banana'],
                4: colors['brick'],
                8: colors['brown2'],
                16: colors['cadmiumorange'],
                32: colors['goldenrod4'],
                64: colors['blueviolet'],
                128: colors['chartreuse4'],
                256: colors['deeppink4'],
                512: colors['manganeseblue'],
                1024: colors['red1'],
                2048: colors['yellow4'],
                4096: colors['sgibeet']
            }
    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.coorX = WINMARGIN + BOXSIZE * self.x + GAPSIZE * self.x
        self.coorY = WINMARGIN + BOXSIZE * self.y + GAPSIZE * self.y;
        self.val = int(value)
        self.rect = pygame.Rect(self.coorX, self.coorY, BOXSIZE, BOXSIZE)
    def delta(self, dx, dy):
        self.rect.left += dx
        self.rect.top += dy

    def draw(self, surface,radius=0.4):

        """
        AAfilledRoundedRect(surface,rect,color,radius=0.4)

        surface : destination
        rect    : rectangle
        color   : rgb or rgba
        radius  : 0 <= radius <= 1
        """
        color = pygame.Color(*Box.boxColors[self.val])
        rect = copy.deepcopy(self.rect)
        alpha        = color.a
        color.a      = 0
        pos          = rect.topleft
        rect.topleft = 0,0
        rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

        circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
        pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

        radius              = rectangle.blit(circle,(0,0))
        radius.bottomright  = rect.bottomright
        rectangle.blit(circle,radius)
        radius.topright     = rect.topright
        rectangle.blit(circle,radius)
        radius.bottomleft   = rect.bottomleft
        rectangle.blit(circle,radius)

        rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
        rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

        rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
        rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)
        if self.val != 0:
            txtSrf = FONT.render(str(self.val), True, (0, 0, 0))
            txtRect = txtSrf.get_rect()
            txtRect.center = rect.center
            rectangle.blit(txtSrf, txtRect.topleft)

        return surface.blit(rectangle,pos)
