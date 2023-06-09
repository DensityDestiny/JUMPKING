# MAIN PROGRAM
import pygame
from player import Player
from background import Background
from world_information import World_information

# variables
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Arial", 20)
size = (900, 675)
screen = pygame.display.set_mode(size)
player_image = pygame.image.load("Jump_king.webp")
player_x = 450 - player_image.get_width() * 0.4 / 2
player_y = 575 - player_image.get_height() * 0.4 / 2
player = Player(player_x, player_y)
image1 = Background("1.png")
image2 = Background("2.png")
image3 = Background("3.png")
image4 = Background("4.png")
image5 = Background("5.png")
image6 = Background("6.png")
image7 = Background("7.png")  # work on this
image8 = Background("8.png")
image9 = Background("9.png")
image10 = Background("10.png")
image11 = Background("11.png")
image12 = Background("12.png")
image13 = Background("13.png")
image14 = Background("14.png")
image15 = Background("15.png")
image16 = Background("16.png")
image17 = Background("17.png")
image18 = Background("18.png")
image19 = Background("19.png")
image20 = Background("20.png")
image21 = Background("21.png")
image22 = Background("22.png")
image23 = Background("23.png")
image24 = Background("24.png")
image25 = Background("41.png")
image26 = Background("42.png")
image27 = Background("43.png")

world_information = World_information()


# class for generating world
class World:
    def __init__(self, data):
        self.tile_list = []
        tile_size = 15
        block_img = pygame.image.load("grass_block.png").convert_alpha()
        right_img = pygame.image.load("slope_right.png").convert_alpha()
        left_img = pygame.image.load("slope_left.png").convert_alpha()
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    types = "block"
                    img = pygame.transform.scale(block_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, types)
                    self.tile_list.append(tile)
                if tile == 2:
                    types = "right"
                    img = pygame.transform.scale(right_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, types)
                    self.tile_list.append(tile)
                if tile == 3:
                    types = "left"
                    img = pygame.transform.scale(left_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, types)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


def playing(current_level):
    play = True
    while play:
        fps = 300
        clock = pygame.time.Clock()
        clock.tick(fps)
        if current_level == 1:
            world_data = world_information.world1
            current_bg = image1.image
        if current_level == 2:
            world_data = world_information.world2
            current_bg = image2.image
        if current_level == 3:
            world_data = world_information.world3
            current_bg = image3.image
        if current_level == 4:
            world_data = world_information.world4
            current_bg = image4.image
        if current_level == 5:
            world_data = world_information.world5
            current_bg = image5.image
        if current_level == 6:
            world_data = world_information.world6
            current_bg = image6.image
        if current_level == 7:
            world_data = world_information.world7
            current_bg = image7.image
        if current_level == 8:
            world_data = world_information.world8
            current_bg = image8.image
        if current_level == 9:
            world_data = world_information.world9
            current_bg = image9.image
        if current_level == 10:
            world_data = world_information.world10
            current_bg = image10.image
        if current_level == 11:
            world_data = world_information.world11
            current_bg = image11.image
        if current_level == 12:
            world_data = world_information.world12
            current_bg = image12.image
        if current_level == 13:
            world_data = world_information.world13
            current_bg = image13.image
        if current_level == 14:
            world_data = world_information.world14
            current_bg = image14.image
        if current_level == 15:
            world_data = world_information.world15
            current_bg = image15.image
        if current_level == 16:
            world_data = world_information.world16
            current_bg = image16.image
        if current_level == 17:
            world_data = world_information.world17
            current_bg = image17.image
        if current_level == 18:
            world_data = world_information.world18
            current_bg = image18.image
        if current_level == 19:
            world_data = world_information.world19
            current_bg = image19.image
        if current_level == 20:
            world_data = world_information.world20
            current_bg = image20.image
        if current_level == 21:
            world_data = world_information.world21
            current_bg = image21.image
        if current_level == 22:
            world_data = world_information.world22
            current_bg = image22.image
        if current_level == 23:
            world_data = world_information.world23
            current_bg = image23.image
        if current_level == 24:
            world_data = world_information.world24
            current_bg = image24.image
        if current_level == 25:
            world_data = world_information.world25
            current_bg = image25.image
        if current_level == 26:
            world_data = world_information.world26
            current_bg = image26.image
        if current_level == 27:
            world_data = world_information.world27
            current_bg = image27.image

        world = World(world_data)
        # DOING THE STUFF IN GAME
        events = pygame.event.get()
        # mouse = pygame.mouse.get_pos()
        # testing_list = world_information.world9
        for event in events:
            if event.type == pygame.QUIT:
                # print(testing_list)
                play = False
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    current_level += 1
                # FOR LEVEL BUILDING NOT FOR PRESENTATION
                # if event.key == pygame.K_1:
                #     x_pos = mouse[0] // 15
                #     y_pos = mouse[1] // 15
                #     testing_list[y_pos][x_pos] = 1
                # if event.key == pygame.K_2:
                #     x_pos = mouse[0] // 15
                #     y_pos = mouse[1] // 15
                #     testing_list[y_pos][x_pos] = 2
                # if event.key == pygame.K_3:
                #     x_pos = mouse[0] // 15
                #     y_pos = mouse[1] // 15
                #     testing_list[y_pos][x_pos] = 3
                # if event.key == pygame.K_4:
                #     x_pos = mouse[0] // 15
                #     y_pos = mouse[1] // 15
                #     testing_list[y_pos][x_pos] = 0


        # MOVEMENT
        player.update(world, events)

        # SWITCHING LEVELS AND CHECKING IF ON SCREEN
        if player.rect.y < 0:
            player.rect.y += size[1] - 1
            current_level += 1
        if player.rect.y > size[1] - 20 and current_level != 1:
            player.rect.y -= size[1] - 1
            current_level -= 1

        # SHOWING STUFF ON THE SCREEN
        screen.fill((255, 255, 255))
        world.draw()
        screen.blit(current_bg, (0, 0))
        if player.direction:
            screen.blit(player.image, (player.rect.x - 15, player.rect.y - 25))
        else:
            screen.blit(player.face_left, (player.rect.x - 15, player.rect.y - 25))
        pygame.display.update()


playing(1)

