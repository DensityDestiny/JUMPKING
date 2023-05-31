# PLAYER
import pygame


class Player:
    def __init__(self, x, y):
        self.dx = 0
        self.y_vel_gravity = 0.36
        self.ground_check = False
        self.direction = True
        self.x = x
        self.y = y
        self.image_list = ["idle.png", "squat.png", "fall.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.idle = pygame.image.load(self.image_list[0])
        self.squat = pygame.image.load(self.image_list[1])
        self.fall = pygame.image.load(self.image_list[2])
        self.image_list = [self.idle, self.squat]
        self.image = self.rescale_image(self.image)
        self.face_left = pygame.transform.flip(self.image, True, False)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, 50 - 10, 53)
        self.delta = 2
        self.image_idx = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.grounded = False
        self.y_velocity = 0
        self.jump_power = 0

    def rescale_image(self, image):
        self.image_size = image.get_size()
        scale_size = (self.image_size[0] * 0.75, self.image_size[1] * 0.75)
        self.image = pygame.transform.scale(self.image, scale_size)
        return self.image

    def update(self, world, events):
        dy = 0

        keys = pygame.key.get_pressed()
        if self.grounded:
            if not keys[pygame.K_SPACE]:
                self.image = self.idle
                self.image = self.rescale_image(self.idle)
                self.face_left = pygame.transform.flip(self.image, True, False)
                if keys[pygame.K_LEFT]:
                    self.dx = -3
                    self.direction = False
                elif keys[pygame.K_RIGHT]:
                    self.dx = 3
                    self.direction = True
                else:
                    self.dx = 0
            else:
                self.image = self.squat
                self.image = self.rescale_image(self.squat)
                self.face_left = pygame.transform.flip(self.image, True, False)
                self.dx = 0
                if self.jump_power > -12.5:
                    self.jump_power -= 0.5
            for event in events:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if keys[pygame.K_RIGHT]:
                            self.dx = 6
                        if keys[pygame.K_LEFT]:
                            self.dx = -6
                        self.jump_power -= 2.5
                        self.y_velocity = self.jump_power
                        self.jump_power = 0

        if not self.grounded:
            if self.y_vel_gravity < 0.5:
                self.y_vel_gravity += 0.0030
            self.y_velocity += self.y_vel_gravity
        dy += self.y_velocity

        self.ground_check = False
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width, self.rect.height) and tile[2] == "block":
                if self.grounded:
                    self.dx = 0
                else:
                    self.dx *= -0.5
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height) and tile[2] == "block":
                if self.y_velocity < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.y_velocity *= -0.5
                elif self.y_velocity > 0:
                    dy = tile[1].top - self.rect.bottom
                    self.y_velocity = 3
                    self.ground_check = True
            if tile[2] == "right":
                x_distance = self.rect.left - tile[1].left
                y_distance = tile[1].bottom - self.rect.bottom
                y_expected = 20 - x_distance
                if 0 < x_distance < 20 and y_distance < y_expected:
                    self.dx = (self.dx + dy) / 2
                    dy = (self.dx + dy) / 2
            if tile[2] == "left":
                x_distance = tile[1].right - self.rect.right
                y_distance = tile[1].bottom - self.rect.bottom
                y_expected = 20 - x_distance
                if 0 < x_distance < 20 and y_distance < y_expected:
                    self.dx = (self.dx - dy) / 2
                    dy = (-self.dx + dy) / 2

        if not self.ground_check:
            self.grounded = False
        else:
            self.grounded = True
            self.y_vel_gravity = 0.36
        if dy < -3:
            self.image = self.fall
            self.image = self.rescale_image(self.fall)
            self.face_left = pygame.transform.flip(self.image, True, False)
        self.rect.x += self.dx
        self.rect.y += dy
