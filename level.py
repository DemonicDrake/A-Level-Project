import pygame
from tiles import Tile
from settings import tile_size, screen_height
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if tile == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if tile == 'p':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < screen_height / 4 and direction_y < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_y > screen_height - (screen_height / 4) and direction_y > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_y()

        self.player.update()
        self.horizontal_movement_collision()
        self.player.draw(self.display_surface)

