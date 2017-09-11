class Button:
    def __init__(self, name, left, top, width, height, background_image):
        self.name = name
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.clicked = False
        self.background_image = background_image
        import pygame
        self.pg = pygame
        self.rect = pygame.rect.Rect((left,top, width, height))
        self.buttonSurface = self.pg.Surface((self.width, self.height))


    def draw(self, surface):
        toDraw = self.pg.image.load(self.background_image).convert_alpha()
        surface.blit(toDraw, (self.left, self.top))

    def click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
