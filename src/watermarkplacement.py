import pygame
import os

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
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                drag_rect.x = event.pos[0] - offset_x
                drag_rect.y = event.pos[1] - offset_y
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_e:
                export_image_requested = True # when user presses "E" image will be exported
    return True

def window_size(image_path):
    image = pygame.image.load(image_path)
    win_width, win_height = image.get_width(), image.get_height()
    return win_width, win_height

def draw(win, bg_image, bg_rect, drag_image, drag_rect, opacity):
    win.fill((0,0,0))
    win.blit(bg_image, bg_rect)
    win.blit(drag_image, drag_rect) # Draws the thumbnail image with opacity
    drag_image.set_alpha(opacity)
    pygame.display.flip()

def save_final_image(bg_image, drag_image, drag_rect, output_folder):
    final_image = pygame.Surface((bg_image.get_width(), bg_image.get_height()))
    final_image.blit(bg_image, (0, 0))

    os.makedirs(output_folder, exist_ok = True)

    output_path = os.path.join(output_folder, "final_image.png")
    
    pygame.image.save(final_image, output_path)
    print(f"Final image saved at: {output_path}")

def export_image(bg_image, drag_image, drag_rect, output_folder):
    global export_image_requested
    if export_image_requested:
        save_final_image(bg_image, drag_image, drag_rect, output_folder)
        export_image_requested = False  
def main():
    global dragging, offset_x, offset_y
    dragging = False
    offset_x, offset_y = 0, 0

    pygame.init()

    bg_image_path = "rat_birthday.jpg"
    win_width, win_height = window_size(bg_image_path)
    win = pygame.display.set_mode((win_width, win_height))
    bg_image = pygame.image.load(bg_image_path).convert_alpha()
    pygame.display.set_caption("Image Overlay")

    drag_image_path = "thumbnail.png"
    drag_image = pygame.image.load(drag_image_path).convert_alpha()
    drag_rect = drag_image.get_rect(center =(win_width // 2, win_height // 2))

    opacity = 128

    while True:
        if not drag_drop(drag_rect):
            break

        draw(win, bg_image, bg_image.get_rect(), drag_image, drag_rect, opacity)

        export_image(bg_image, drag_image, drag_rect, "final_images")

    pygame.quit()

if __name__ == "__main__":
    main()
