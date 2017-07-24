# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit


class Utils:
    def __init__(self):
        self.color_yellow = (255, 255, 0)
        self.color_red = (255, 0, 0)
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)
        self.color_green = (0, 255, 0)
        self.width = 640
        self.height = 480
        self.rect1_pos = (160, 290, 100, 60)
        self.rect2_pos = (400, 290, 100, 60)
        self.font_type = r'C:\Users\zhouxin\Downloads\hanyi147\hanyi.ttf'
        self.big_font_size = 32
        self.small_font_size = 16


class Game(Utils):
    def __init__(self):
        Utils.__init__(self)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        pygame.display.set_caption('Brick&Blocks')
        self.clock = pygame.time.Clock()
        self.ball_pos = [220, 220]
        self.panel_surface = pygame.Surface((50, 10))
        self.panel_pos = [300, 250]
        self.running = False
        self.wining = False
        self.font = None
        self.rect1 = None
        self.rect2 = None
        self.tiled_map = [['@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
                          ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
                          ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
                          ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@']]
        self.brick_list = []
        self.is_hit_edge = False
        self.is_hit_panel = False
        self.speed_x = 1
        self.speed_y = 1
        self.score = 0

    def draw_text(self, text, size, font_color, pos):
        self.font = pygame.font.Font(self.font_type, size)
        text_surface = self.font.render(text, False, font_color)
        text_rect = pos
        self.screen.blit(text_surface, text_rect)

    def new(self):
        tiled_x = 0
        tiled_y = 0
        for bricks in self.tiled_map:
            for per_brick in bricks:
                brick = bricks[bricks.index(per_brick)] = pygame.Rect(tiled_x, tiled_y, 60, 20)
                self.brick_list.append(brick)
                tiled_x += 65
            tiled_x = 0
            tiled_y += 25
        return self.brick_list

    def game_start_screen(self):
        self.draw_text(u"打砖块", self.big_font_size, self.color_white, (280, 200))
        self.rect1 = pygame.draw.rect(self.screen, self.color_green, self.rect1_pos)
        self.rect2 = pygame.draw.rect(self.screen, self.color_green, self.rect2_pos)
        self.draw_text(u"开始", self.small_font_size, self.color_white, self.rect1.center)
        self.draw_text(u"结束", self.small_font_size, self.color_white, self.rect2.center)
        mouse = pygame.mouse.get_pos()
        if self.rect1_pos[2] >= mouse[0] - self.rect1_pos[0] >= 0 \
                >= mouse[1] - (self.rect1_pos[1] + self.rect1_pos[3]) >= -self.rect1_pos[3]:
            self.rect1 = pygame.draw.rect(self.screen, (255, 255, 255), self.rect1_pos)
            if pygame.mouse.get_pressed()[0]:
                self.running = True
        elif self.rect2_pos[2] >= mouse[0] - self.rect2_pos[0] >= 0 \
                >= mouse[1] - (self.rect2_pos[1] + self.rect2_pos[3]) >= -self.rect2_pos[3]:
            self.rect2 = pygame.draw.rect(self.screen, (255, 255, 255), self.rect2_pos)
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            self.color_green = (0, 255, 0)
        pygame.display.update()
        return self.running

    def game_over_screen(self):
        self.draw_text(u'游戏结束', self.big_font_size, self.color_white, (280, 200))
        self.rect1 = pygame.draw.rect(self.screen, self.color_green, self.rect1_pos)
        self.rect2 = pygame.draw.rect(self.screen, self.color_green, self.rect2_pos)
        self.draw_text(u"继续游戏", self.small_font_size, self.color_white, self.rect1.center)
        self.draw_text(u"结束", self.small_font_size, self.color_white, self.rect2.center)
        self.draw_text(u'当前记录：%d' % self.score, self.small_font_size, self.color_green, (250, 300))
        mouse = pygame.mouse.get_pos()
        if self.rect1_pos[2] >= mouse[0] - self.rect1_pos[0] >= 0 \
                >= mouse[1] - (self.rect1_pos[1] + self.rect1_pos[3]) >= -self.rect1_pos[3]:
            self.rect1 = pygame.draw.rect(self.screen, (255, 255, 255), self.rect1_pos)
            if pygame.mouse.get_pressed()[0]:
                self.running = True
        elif self.rect2_pos[2] >= mouse[0] - self.rect2_pos[0] >= 0 \
                >= mouse[1] - (self.rect2_pos[1] + self.rect2_pos[3]) >= -self.rect2_pos[3]:
            self.rect2 = pygame.draw.rect(self.screen, (255, 255, 255), self.rect2_pos)
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            self.color_green = (0, 255, 0)
        pygame.display.update()
        return self.running

    def ball(self):
        ball = pygame.draw.circle(self.screen, self.color_red, self.ball_pos, 5)
        key = pygame.key.get_pressed()
        self.ball_pos[0] += self.speed_x
        self.ball_pos[1] += self.speed_y
        if key[K_w]:
            self.ball_pos[1] -= 1
        if key[K_s]:
            self.ball_pos[1] += 1
        if key[K_a]:
            self.ball_pos[0] -= 1
        if key[K_d]:
            self.ball_pos[0] += 1
        if self.ball_pos[1] > self.height - 5:
            self.running = False
        elif self.ball_pos[1] < 5:
            self.ball_pos[1] += self.speed_y
            if self.speed_y < 0:
                self.speed_y *= -1
            self.speed_y *= 1
        if self.ball_pos[0] > self.width - 5:
            self.ball_pos[0] -= self.speed_x
            if self.speed_x > 0:
                self.speed_x *= 1
            self.speed_x *= -1
        elif self.ball_pos[0] < 5:
            self.ball_pos[0] += self.speed_x
            if self.speed_x < 0:
                self.speed_x *= -1
            self.speed_x *= 1
        return ball

    def panel(self):
        panel = pygame.draw.rect(self.screen, self.color_yellow, (self.panel_pos[0], self.panel_pos[1], 50, 10))
        key = pygame.key.get_pressed()
        if key[K_UP]:
            self.panel_pos[1] -= 3
            if self.panel_pos[1] <= 0:
                self.panel_pos[1] = 0
        if key[K_DOWN]:
            self.panel_pos[1] += 3
            if self.panel_pos[1] > self.height - 10:
                self.panel_pos[1] = self.height - 10
        if key[K_LEFT]:
            self.panel_pos[0] -= 3
            if self.panel_pos[0] <= 0:
                self.panel_pos[0] = 0
        if key[K_RIGHT]:
            self.panel_pos[0] += 3
            if self.panel_pos[0] >= self.width - 50:
                self.panel_pos[0] = self.width - 50
        self.clock.tick(100)
        return panel

    def bricks(self):
        for brick in self.brick_list:
            pygame.draw.rect(self.screen, self.color_green, brick)
        if self.ball().collidelist(self.brick_list) != -1:
            self.brick_list.pop(self.ball().collidelist(self.brick_list))
            self.score += 10
            self.ball_pos[1] += self.speed_y
            if self.speed_y < 0:
                self.speed_y = -self.speed_y
        if self.panel().collidelist(self.brick_list) != -1:
            self.panel_pos[1] = self.brick_list[self.panel().collidelist(self.brick_list)].bottom

    def ball_hit_panel(self):
        if self.ball().colliderect(self.panel()):
            self.ball_pos[1] -= self.speed_y
            if self.speed_y > 0:
                self.speed_y = -self.speed_y

    def update(self):
        self.screen.fill(self.color_black)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        self.ball()
        self.panel()
        self.ball_hit_panel()
        self.bricks()
        pygame.display.update()

    def wait_for_mouse(self):
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    waiting = False
                    self.running = False
            if self.game_start_screen():
                return self.game_start_screen()

    def win(self):
        if len(self.brick_list) == 0:
            self.running = False
        return self.running

    def run(self):
        self.wait_for_mouse()
        self.new()
        while self.running:
            self.win()
            self.update()
            while not self.running:
                self.screen.fill(self.color_black)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                if self.game_over_screen():
                    self.running = self.game_over_screen()
                    self.new().clear()
                    self.new()
                    self.ball_pos = [220, 220]
                    self.panel_pos = [300, 250]
                    self.speed_y = 1
                    self.speed_x = 1
                    self.score = 0

if __name__ in '__main__':
    Game().run()
