import sys
import pygame
from pygame.sprite import Group
from setting import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_function as gf

def rungame():
    #initialize pygame and screen_object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")



    # Create an instances to stroe game statitics.
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship,a group of bullets,group of aliens
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()


    #set the background color
    bg_color = (0,0,255)

    # Make an alien.
    alien = Alien(ai_settings, screen)

    #Create the fleet for the aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    #start the main loop for the game

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


        

rungame()         