import pygame


width = 500
height = 500
WIN = pygame.display.set_mode((width, height))


pygame.display.set_caption("sudoku solver")

Background_color = (255, 255, 255)
Red = (255,0,0)
FPS = 60


def draw_window():
    WIN.fill(Background_color)
    pygame.display.update()
    pygame.draw.rect(WIN, Red,pygame.Rect(30,30,60,60),2)
    pygame.display.flip()





def main():
    clock = pygame.time.Clock()
    run = True
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()



    pygame.quit()


#zorgt ervoor dat het kan runnen 11:11
if __name__ =="__main__":
    main()