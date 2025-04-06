import pygame
import time

# Constants
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_SIZE = 40
ERASER_SIZE = 20

# Initialize Pygame
pygame.init()

# Set up the canvas (window)
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Eraser on Canvas")

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)

# Create a grid to track the cells (True = blue, False = erased)
grid = [[True for _ in range(CANVAS_WIDTH // CELL_SIZE)] for _ in range(CANVAS_HEIGHT // CELL_SIZE)]

# Function to draw the grid of blue cells
def draw_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            color = BLUE if grid[row][col] else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to erase cells under the eraser
def erase_cells(eraser_rect):
    left = max(eraser_rect.left // CELL_SIZE, 0)
    top = max(eraser_rect.top // CELL_SIZE, 0)
    right = min((eraser_rect.right + CELL_SIZE - 1) // CELL_SIZE, len(grid[0]))
    bottom = min((eraser_rect.bottom + CELL_SIZE - 1) // CELL_SIZE, len(grid))

    for row in range(top, bottom):
        for col in range(left, right):
            grid[row][col] = False  # Mark as erased

def main():
    clock = pygame.time.Clock()

    # Define the initial position of the eraser
    eraser_rect = pygame.Rect(100, 100, ERASER_SIZE, ERASER_SIZE)

    # Main loop
    running = True
    while running:
        screen.fill(WHITE)  # Fill the screen with white (clearing the screen)
        
        draw_grid()  # Redraw the grid after clearing

        # Draw the eraser
        pygame.draw.rect(screen, PINK, eraser_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get mouse position and move the eraser
        mouse_x, mouse_y = pygame.mouse.get_pos()
        eraser_rect.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)

        # Erase cells under the eraser
        erase_cells(eraser_rect)

        pygame.display.update()  # Update the display
        clock.tick(60)  # Frame rate

    pygame.quit()

if __name__ == '__main__':
    main()
