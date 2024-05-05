import pygame
import os

pygame.init()

def window_size(image_path):
    image = pygame.image.load(image_path)
    win_width, win_height = image.get_width(), image.get_height()
    return win_width, win_height


bg_image_path = "rat_birthday.jpg"
win_width, win_height = window_size(bg_image_path)
win = pygame.display.set_mode((win_width, win_height))
bg_image = pygame.image.load(bg_image_path).convert_alpha()
pygame.display.set_caption("Image Overlay")
