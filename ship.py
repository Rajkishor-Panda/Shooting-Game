import pygame
from pygame.sprite import Sprite
class Ship(Sprite):


    def __init__(self,ai_settings,screen):
        """initializing ship and it's starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('.vscode/Project/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)



        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        

        








    def update(self):
        """ Update the ship position based on the movement flag."""
        ## Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor          

        # Update rect object from self.center.
        # movement in two direction.
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx    
       


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)    

    


