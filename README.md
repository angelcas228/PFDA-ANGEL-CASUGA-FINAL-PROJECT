# Watermark Drag and Drop

## Demo
Demo Video: https://youtu.be/57LdgpXeXw0

## GitHub Repository
GitHub Repo: https://github.com/angelcas228/PFDA-ANGEL-CASUGA-FINAL-PROJECT.git

## Description
This program will let the user drag and drop their images to wherever they desire on any photo or drawing uploaded! The program will also open the window to the set dimensions of the desired image. I have a final images folder set up so when the image exports it will automatically go there, and have 2 test images "Value Breakdown" and "Rat Birthday" along with the thumbnail in my folder.

The program is straight forward you place your desired images and thumbnail within the correct folders, modify the code to open your specific images, and then the program will open a window the size of your drawing and allow you to drag and drop your thumbnail wherever you desire! Once you're done you can export and close the window by pressing 'E'

If someone else wants to put other images in the generator all they have to do is to change the name of the file within the code, and they can also rename the exported image name other than "final image".

The main function I wanted to show off in this project was mainly the drag and drop feature. I was able to do this by using pygame and through an event loop to help with the drag and drop feature. When the user presses down on the mouse to move the image it will set the event pygame.MOUSEBUTTONDOWN to true and allow the user to start dragging the image around the screen until they stop pressing. however the drag and drop event will only happen if the mouse is within the area of the thumbnail image, which is where drag_rect.collidepoint(event.pos) comes in. I learned that I had to use offset_x and offset_y to calculate the offset of where the mouse was and the top left corner of the rectangle image of the thumbnail so I could drag it around. pygame.MOUSEMOTION is the event that occured once the user has moved the mouse and when dragging is set to true, it updates the position of the draggable image. The event loops will continue to execute until the export and exit key are pressed.

The other main function of this program was setting it up to where the window would be the size of the image. One of the images I used (rat birthday) was 1000 by 1000, so the program made a window the size of the image. I did this by also using pygame and image.getwidth() and image.getheight(). So when the program is going to generate a window it will just use the information from the image and create the window based off of that size. However I did not realize the drawback of using an image that was larger than my current laptop's display dimensions. In the future I could figure out a way to downscale the image when opening the window but stil export it at the same size, however for this project currently I am satisfied with keeping it the way it is, as long as the user is able to drag and drop a thumbnail around the window. 
