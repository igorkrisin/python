import pygame

FRAME_COLOR = (0,255,204)
WHITE = (255,255,255)
BLUE = [204,255,255]
SIZE_BLOCK=20
COUNT_BLOKS = 20
SNAKE_COLOR = [255,6,57]
MARGIN = 1
size = [500,600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_block(color, row, column):
    pygame.draw.rect(screen,color,\
                [10+column*SIZE_BLOCK+MARGIN*(column+1),\
                20+row*SIZE_BLOCK+MARGIN*(row+1),\
                SIZE_BLOCK,SIZE_BLOCK])

snake_block = [SnakeBlock(9,9)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)

    for row in range(COUNT_BLOKS):
        for column in range(COUNT_BLOKS):
            if (row+column)%2==0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color,row,column)
        
    for block in snake_block:
        
        draw_block(SNAKE_COLOR, block.x, block.y)

    pygame.display.flip()
