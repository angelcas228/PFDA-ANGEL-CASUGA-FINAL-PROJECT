import pygame
import os

def window_size(image):
    win_width = image.get_width()
    win_height = image.get_height
    return win_width, win_height

bg_image_path = "rat_birthday.jpg"
bg_image = pygame.image.load(bg_image_path).convert_alpha()

win_width, win_height = set_window_size(bg_image)
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Image Overlay")
