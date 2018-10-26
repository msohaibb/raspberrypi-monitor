import pygame
from UsageStats import UsageStats

pygame.init()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
LIGHTBLUE = (30, 178, 252)

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 36, True, False)

# Set the width and height of the screen [width, height]
size = (960, 540)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Usage Monitor")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    textCPU = font.render("CPU Usage: " + str(UsageStats.find_cpu_usage() + "%"), True, WHITE)
    textRAM = font.render("RAM Usage: " + str(UsageStats.find_ram_usage() + "%"), True, WHITE)
    # --- Drawing code should go here
    pygame.draw.rect(screen, LIGHTBLUE, (0, 0, size[0]/2, size[1]))
    pygame.draw.rect(screen, RED, (size[0]/2, 0, size[0]/2, size[1]))

    screen.blit(textCPU, [120, 230])
    screen.blit(textRAM, [570, 230])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
