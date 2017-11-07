import pygame
import sys
from pygame.locals import *
import math

class Pong:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.font.init()
        self.font = pygame.font.Font("pongFont.TTF", 50)
        self.ball = pygame.Rect(400, 300, 5, 5)
        self.ballAngle = math.radians(0)
        self.ballSpeed = 10
        self.playerScore = 0
        self.opponentScore = 0
        self.direction = -1
        self.playerRects = {
            -60:pygame.Rect(50, 380, 10, 20), # Bottom of paddle
            -45:pygame.Rect(50, 360, 10, 20),
            -30:pygame.Rect(50, 340, 10, 20),
            -0:pygame.Rect(50, 320, 10, 20),
            30:pygame.Rect(50, 300, 10, 20),
            45:pygame.Rect(50, 280, 10, 20),
            60:pygame.Rect(50, 260, 10, 20), # Top of paddle
        }

        self.player2rects = {
            -60:pygame.Rect(750, 380, 10, 20), # Bottom of paddle
            -45:pygame.Rect(750, 360, 10, 20),
            -30:pygame.Rect(750, 340, 10, 20),
            -0:pygame.Rect(750, 320, 10, 20),
            30:pygame.Rect(750, 300, 10, 20),
            45:pygame.Rect(750, 280, 10, 20),
            60:pygame.Rect(750, 260, 10, 20), # Top of paddle
        }

        self.pause = 10

    def drawPlayers(self):
        for pRect in self.playerRects:
            pygame.draw.rect(self.screen, (255,0,0), self.playerRects[pRect])
        for oRect in self.player2rects:
            pygame.draw.rect(self.screen, (0,0,255), self.player2rects[oRect])

    def updatePlayer(self): #controls the paddle on the left
        key = pygame.key.get_pressed()
        if self.ball.y <= 0 or self.ball.y > 595:
            self.ballAngle *= -1

        if key[K_w]:
            if self.playerRects[60].y > 0:
                for pRect in self.playerRects:
                    self.playerRects[pRect].y -= 5

        elif key[K_s]:
            if self.playerRects[-60].y < 590:
                for pRect in self.playerRects:
                    self.playerRects[pRect].y += 5

    def updateBall(self):
        self.ball.x += self.direction * self.ballSpeed * math.cos(self.ballAngle)
        self.ball.y += self.direction * self.ballSpeed * -math.sin(self.ballAngle)
        if self.ball.x > 800 or self.ball.x < 0:
            if self.ball.x > 800:
                self.playerScore += 1

            elif self.ball.x < 0:
                self.opponentScore += 1
            self.ball.x = 400
            self.ball.y = 300
            self.ballAngle = math.radians(0)
            self.pause = 10
            if self.opponentScore >= 11 or self.playerScore >= 11:
                self.opponentScore = 0
                self.playerScore = 0
            return

        if self.direction < 0:
            for pRect in self.playerRects:
                if self.playerRects[pRect].colliderect(self.ball):
                    self.ballAngle = math.radians(pRect)
                    self.direction = 1
                    break

        else:
            for oRect in self.player2rects:
                if self.player2rects[oRect].colliderect(self.ball):
                    self.ballAngle = math.radians(oRect)
                    self.direction = -1

    def updatePlayer2(self): #controls the paddle on the right
        key = pygame.key.get_pressed()
        if self.ball.y <= 595 or self.ball.y > 0:
            self.ballAngle *= 1

        if key[K_UP]:
            if self.player2rects[-60].y > 0:
                for pRect in self.player2rects:
                    self.player2rects[pRect].y -= 5

        elif key[K_DOWN]:
            if self.player2rects[60].y < 590:
                for pRect in self.player2rects:
                    self.player2rects[pRect].y += 5
    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.fill((0,0,0))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

            pygame.draw.rect(self.screen, (255,255,255), self.ball)
            self.screen.blit(self.font.render(str(self.playerScore), -1, (255,255,255)), (200, 25))
            self.screen.blit(self.font.render(str(self.opponentScore), -1, (255,255,255)), (600, 25))
            self.drawPlayers()
            self.updatePlayer()
            self.updatePlayer2()
            if self.pause:
                self.pause -= 1
            else:
                self.updateBall()
            pygame.display.flip()

Pong().run()
'''
Credits:
*    Title: Pong created in 30 mins
*    Author: Max00355
*    Date: 2015
*    Code version: Source Code
*    Availability: https://github.com/Max00355/Pong
'''
