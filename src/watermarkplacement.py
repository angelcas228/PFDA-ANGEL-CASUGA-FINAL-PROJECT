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

def drag_drop(drag_rect):
    global dragging, offset_x, offset_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if drag_rect.collidepoint(event.pos):
                dragging = True
                offset_x = event.pos[0] - drag_rect.x
                offset_y = event.pos[1] - drag_rect.y
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION
            if dragging:
                drag_rect.x = event.pos[0] - offset_x
                drag_rect.y = event.pos[1] - offset_y
return True
