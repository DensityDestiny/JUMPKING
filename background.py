import pygame


class Background:
    def __init__(self, image1):
        self.image_list = [image1]
        self.returned_image = []
        # for i in range(len(self.image_list)):
        self.image = pygame.image.load(self.image_list[0]).convert_alpha()
        self.image.set_alpha(150)
        self.rescale_image()
        self.image_size = self.image.get_size()
        self.returned_image.append(self.image)

    # self.mask = pygame.mask.from_surface(self.image)

    def rescale_image(self):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.75, self.image_size[1] * 0.75)
        self.image = pygame.transform.scale(self.image, scale_size)
