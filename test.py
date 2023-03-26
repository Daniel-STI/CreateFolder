# import Pygame

import pygame

# defined the RGB color code for the background

background_colour = (139,0,0)

# defined the size of the screen (width, height)

screen = pygame.display.set_mode((600, 300))



# set caption

pygame.display.set_caption('GuidingCode.com')



# fill the screen with the above-defined background color

screen.fill(background_colour)

# update the display using flip

pygame.display.flip()



# keep the game looping

running = True


# game loop

while running:

   pygame.event.get()



# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False
# import pygame
# pygame.init()

# game = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Test")
# pygame.display.update()
# pygame.time.delay(5000)
# x=100
# y=100
# height=50
# width=50
# movement=5

# run=True
# while run:
#     pygame.time.delay(10)
#     for event in pygame.event.get():
#         if event.type == pygame.quit():
#             run==False