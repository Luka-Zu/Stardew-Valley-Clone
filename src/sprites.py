import pygame
from settings import *
from random import randint, choice

from src.timer import Timer


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group, z=LAYERS['main']):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.2, -self.rect.height*0.75)


class Water(Generic):
    def __init__(self, pos, frames, group):
        # Animation setup
        self.frames = frames
        self.frame_index = 0

        # Sprite setup
        super().__init__(pos=pos,
                         surf=self.frames[self.frame_index],
                         group=group,
                         z=LAYERS['water'])

    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class WildFlower(Generic):
    def __init__(self, pos, surf, group):
        super().__init__(pos, surf, group)
        self.hitbox = self.rect.copy().inflate(-20, -self.rect.height * 0.9)


class Tree(Generic):
    def __init__(self, pos, surf, group, name):
        super().__init__(pos, surf, group)

        # Tree attributes
        self.health = 5
        self.alive = True
        stump_path = f'graphics/stumps/{"small" if name=="Small" else "large"}.png'
        self.stump_surf = pygame.image.load(stump_path).convert_alpha()
        self.invul_timer = Timer(200)

        # Apples
        self.apple_surf = pygame.image.load('graphics/fruit/apple.png')
        self.apple_pos = APPLE_POS[name]
        self.apple_sprites = pygame.sprite.Group()
        self.create_fruit()

    def damage(self):
        # Damaging the tree
        self.health -= 1

        # Remove an apple
        if len(self.apple_sprites.sprites()) > 0:
            random_apple = choice(self.apple_sprites.sprites())
            random_apple.kill()


    def create_fruit(self):
        for pos in self.apple_pos:
            if randint(0, 10) <= 2:
                x = pos[0] + self.rect.left
                y = pos[1] + self.rect.top

                Generic(pos=(x, y),
                        surf=self.apple_surf,
                        group=[self.apple_sprites, self.groups()[0]],
                        z=LAYERS['fruit'])

