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
image5 = Background("4.png")
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
        fps = 150
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

        world = World(world_data)

        # DOING THE STUFF IN GAME
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play = False

        # MOVEMENT
        player.update(world, events)

        # SWITCHING LEVELS AND CHECKING IF ON SCREEN
        if player.rect.y < 0:
            player.rect.y += size[1] - 10
            current_level += 1
        if player.rect.y > size[1] - 20 and current_level != 1:
            player.rect.y -= size[1] - 10
            current_level -= 1

        # SHOWING STUFF ON THE SCREEN
        screen.fill((0, 0, 0))
        world.draw()
        screen.blit(current_bg, (0, 0))
        if player.direction:
            screen.blit(player.image, (player.rect.x - 15, player.rect.y - 25))
        else:
            screen.blit(player.face_left, (player.rect.x - 15, player.rect.y - 25))
        pygame.display.update()


playing(4)
