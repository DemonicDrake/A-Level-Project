import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((160, 32, 240))
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.world_direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -4

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_c]:
            self.jump()

#######################
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.world_direction.y += self.gravity
        self.rect.y += self.direction.y
        print(self.direction[1])

    def jump(self):
        self.direction.y = self.jump_speed
        self.world_direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.rect.y += self.direction.y * self.speed
        self.apply_gravity()
#######################