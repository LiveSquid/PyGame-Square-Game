import pygame

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

deathFont = pygame.font.SysFont("Impact", 100)

gravity = 2
speed = 2

up = (0, -60)
down = (0, gravity)
left = (-speed - gravity, 0)
right = (speed + gravity, 0)

directions = {"up": up, "down": down, "left": left, "right": right}
direction = right

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.fill((255, 255, 255))
pygame.display.set_caption("Test Caption")

# This class is responsible for the creation of all the rectangles in my game. It's attributes control the
# rectangles appearance and location on the screen. The first method "draw" physically prints the rectangles on the
# screen using all the attributes of the class. The second method "move" uses the locationX and Y attributes to
# control the movement of rectangles. This method allows me to control the rectangles in the game loop after
# originally printing them. The last method "collision" restricts the playerRect from going through obstacles.
# It does this by moving the player back 2 from whichever direction it came.


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, d, locationX, locationY, sizeX, sizeY, color):
        super().__init__()
        self.display = d
        self.locationX = locationX
        self.locationY = locationY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.rect = pygame.draw.rect(self.display, self.color,
                                     pygame.Rect(self.locationX, self.locationY, self.sizeX, self.sizeY))

    def draw(self):
        self.rect = pygame.draw.rect(self.display, self.color,
                                     pygame.Rect(self.locationX, self.locationY, self.sizeX, self.sizeY))

    def move(self, *args):
        if len(args) == 2:
            self.locationX = (self.locationX + args[0])
            self.locationY = (self.locationY + args[1])
        elif len(args) == 1:
            self.locationX = (self.locationX + args[0][0])
            self.locationY = (self.locationY + args[0][1])

    def collision(self, sprite1, sprite2, direction2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            return sprite1.move(-direction2[0], -direction2[1])

# This class is almost identical to the Rectangle class as it inherits all of its attributes and methods. The only
# difference it has a health attribute which is used in the game loop to control whether the player is alive or not.


class Player(Rectangle):
    def __init__(self, d, locationX, locationY, sizeX, sizeY, color, health):
        super().__init__(d, locationX, locationY, sizeX, sizeY, color)
        self.health = health


floorRect = Rectangle(display, 0, 800, 15000, 100, BLUE)
playerRect = Player(display, 50, 750, 50, 50, BLACK, 1)

firstObstacleRectLeft = Rectangle(display, 350, 750, 10, 50, BLUE)
firstObstacleRectTop = Rectangle(display, 354, 749, 151, 10, BLUE)
firstObstacleRectRight = Rectangle(display, 496, 750, 10, 50, BLUE)

secondObstacleRectLeft = Rectangle(display, 650, 750, 10, 50, BLUE)
secondObstacleRectTop = Rectangle(display, 654, 749, 150, 10, BLUE)
secondObstacleRectRight = Rectangle(display, 794, 750, 10, 50, BLUE)

thirdObstacleRectLeft = Rectangle(display, 950, 750, 10, 50, BLUE)
thirdObstacleRectTop = Rectangle(display, 954, 749, 151, 10, BLUE)
thirdObstacleRectRight = Rectangle(display, 1096, 750, 10, 50, BLUE)

fourthObstacleRectLeft = Rectangle(display, 1170, 660, 10, 170, BLUE)
fourthObstacleRectTop = Rectangle(display, 1172, 659, 112, 10, BLUE)
fourthObstacleRectRight = Rectangle(display, 1274, 660, 10, 170, BLUE)

fifthObstacleRectLeft2 = Rectangle(display, 1350, 570, 10, 300, BLUE)
fifthObstacleRectTop = Rectangle(display, 1351, 569, 154, 10, BLUE)
fifthObstacleRectLeft3 = Rectangle(display, 1495, 490, 10, 80, BLUE)
fifthObstacleRectTop2 = Rectangle(display, 1499, 488, 130, 10, BLUE)
fifthObstacleRectLeft4 = Rectangle(display, 1619, 409, 10, 80, BLUE)
fifthObstacleRectTop3 = Rectangle(display, 1623, 407, 127, 10, BLUE)
fifthObstacleRectLeft5 = Rectangle(display, 1740, 329, 10, 80, BLUE)
fifthObstacleRectTop4 = Rectangle(display, 1744, 327, 127, 10, BLUE)
fifthObstacleRectLeft6 = Rectangle(display, 1861, 248, 10, 80, BLUE)
fifthObstacleRectTop5 = Rectangle(display, 1865, 246, 127, 10, BLUE)
fifthObstacleRectLeft7 = Rectangle(display, 1982, 167, 10, 80, BLUE)

sixthObstacleRectTop = Rectangle(display, 1986, 165.5, 497, 10, BLUE)
sixthObstacleRectLeft = Rectangle(display, 2473, 167, 10, 800, BLUE)
sixthObstacleRectRight = Rectangle(display, 2550, 166, 10, 550, BLUE)
sixthObstacleRectTop2 = Rectangle(display, 2554, 166, 998, 10, BLUE)

finishLineRect = Rectangle(display, 2850, 750, 3000, 50, GREEN)

bouncePad = Rectangle(display, 2474, 50, 77, 10, YELLOW)

deathBarrier1 = Rectangle(display, 498, 790, 153, 10, RED)
deathBarrier2 = Rectangle(display, 800, 790, 153, 10, RED)
deathBarrier4 = Rectangle(display, 1350, 0, 10, 500, RED)
movingDeath1 = Rectangle(display, 2250, 0, 10, 75, RED)
deathBarrier5 = Rectangle(display, 3540, 0, 10, 166, RED)

obstacleGroup1 = pygame.sprite.Group()
obstacleGroup2 = pygame.sprite.Group()
obstacleGroup3 = pygame.sprite.Group()
obstacleGroup4 = pygame.sprite.Group()
obstacleGroup5 = pygame.sprite.Group()
obstacleGroup6 = pygame.sprite.Group()
bounceGroup = pygame.sprite.Group()
finishGroup = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()
deathBarrierGroup = pygame.sprite.Group()

floorGroup.add(floorRect)
floorGroup.add(firstObstacleRectTop)
floorGroup.add(secondObstacleRectTop)
floorGroup.add(thirdObstacleRectTop)
floorGroup.add(fourthObstacleRectTop)
floorGroup.add(fifthObstacleRectTop)
floorGroup.add(fifthObstacleRectTop2)
floorGroup.add(fifthObstacleRectTop3)
floorGroup.add(fifthObstacleRectTop4)
floorGroup.add(fifthObstacleRectTop5)
floorGroup.add(sixthObstacleRectTop)
floorGroup.add(sixthObstacleRectTop2)

deathBarrierGroup.add(deathBarrier1)
deathBarrierGroup.add(deathBarrier2)
deathBarrierGroup.add(deathBarrier4)
deathBarrierGroup.add(movingDeath1)
deathBarrierGroup.add(deathBarrier5)

obstacleGroup1.add(firstObstacleRectLeft)
obstacleGroup1.add(firstObstacleRectRight)

obstacleGroup2.add(secondObstacleRectLeft)
obstacleGroup2.add(secondObstacleRectRight)

obstacleGroup3.add(thirdObstacleRectLeft)
obstacleGroup3.add(thirdObstacleRectRight)

obstacleGroup4.add(fourthObstacleRectLeft)
obstacleGroup4.add(fourthObstacleRectRight)

obstacleGroup5.add(fifthObstacleRectLeft2)
obstacleGroup5.add(fifthObstacleRectLeft3)
obstacleGroup5.add(fifthObstacleRectLeft4)
obstacleGroup5.add(fifthObstacleRectLeft5)
obstacleGroup5.add(fifthObstacleRectLeft6)
obstacleGroup5.add(fifthObstacleRectLeft7)

obstacleGroup6.add(sixthObstacleRectLeft)
obstacleGroup6.add(sixthObstacleRectRight)

bounceGroup.add(bouncePad)

finishGroup.add(finishLineRect)

goUp = 1
canJump = True
time = 0

while True:
    time += 1

    pygame.display.update()
    display.fill(WHITE)

    clock = pygame.time.Clock()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    collisionsFloor = pygame.sprite.spritecollide(playerRect, floorGroup, False)
    collisionsDeath = pygame.sprite.spritecollide(playerRect, deathBarrierGroup, False)
    collisionsBounce = pygame.sprite.spritecollide(playerRect, bounceGroup, False)
    collisionsFinish = pygame.sprite.spritecollide(playerRect, finishGroup, False)

    bouncePad.draw()

    for f in floorGroup:
        f.draw()

    for o in obstacleGroup1:
        o.draw()

    for o in obstacleGroup2:
        o.draw()

    for o in obstacleGroup3:
        o.draw()

    for o in obstacleGroup4:
        o.draw()

    for o in obstacleGroup5:
        o.draw()

    for o in obstacleGroup6:
        o.draw()

    for d in deathBarrierGroup:
        d.draw()

    for b in bounceGroup:
        b.draw()

    for f in finishGroup:
        f.draw()

    if movingDeath1.locationY <= 0:
        goUp = 1

    if goUp == 1:
        movingDeath1.move(0, 0.13)

    if movingDeath1.locationY >= 180:
        goUp = 2

    if goUp == 2:
        movingDeath1.move(0, 0.13)

    keys = pygame.key.get_pressed()

    if canJump and keys[pygame.K_SPACE]:
        playerRect.move(up)
        direction = up
        canJump = False
    else:
        direction = down

    if playerRect.health > 0:
        playerRect.move(gravity, gravity)

    if len(collisionsFloor):
        canJump = True

    if len(collisionsBounce):
        playerRect.move(0, 630)

    floorRectColl = floorRect.collision(playerRect, floorRect, down)

    firstObstacleRectLeftColl = firstObstacleRectLeft.collision(playerRect, firstObstacleRectLeft, right)
    firstObstacleRectTopColl = firstObstacleRectTop.collision(playerRect, firstObstacleRectTop, down)
    firstObstacleRectRightColl = firstObstacleRectRight.collision(playerRect, firstObstacleRectRight, left)

    secondObstacleRectLeftColl = secondObstacleRectLeft.collision(playerRect, secondObstacleRectLeft, right)
    secondObstacleRectTopColl = secondObstacleRectTop.collision(playerRect, secondObstacleRectTop, down)
    secondObstacleRectRightColl = secondObstacleRectRight.collision(playerRect, secondObstacleRectRight, left)

    thirdObstacleRectLeftColl = thirdObstacleRectLeft.collision(playerRect, thirdObstacleRectLeft, right)
    thirdObstacleRectTopColl = thirdObstacleRectTop.collision(playerRect, thirdObstacleRectTop, down)
    thirdObstacleRectRightColl = thirdObstacleRectRight.collision(playerRect, thirdObstacleRectRight, left)

    fourthObstacleRectLeftColl = fourthObstacleRectLeft.collision(playerRect, fourthObstacleRectLeft, right)
    fourthObstacleRectTopColl = fourthObstacleRectTop.collision(playerRect, fourthObstacleRectTop, down)
    fourthObstacleRectRightColl = fourthObstacleRectRight.collision(playerRect, fourthObstacleRectRight, left)

    fifthObstacleRectLeft2Coll = fifthObstacleRectLeft2.collision(playerRect, fifthObstacleRectLeft2, right)
    fifthObstacleRectTopColl = fifthObstacleRectTop.collision(playerRect, fifthObstacleRectTop, down)
    fifthObstacleRectLeft3Coll = fifthObstacleRectLeft3.collision(playerRect, fifthObstacleRectLeft3, right)
    fifthObstacleRectTop2Coll = fifthObstacleRectTop2.collision(playerRect, fifthObstacleRectTop2, down)
    fifthObstacleRectLeft4Coll = fifthObstacleRectLeft4.collision(playerRect, fifthObstacleRectLeft4, right)
    fifthObstacleRectTop3Coll = fifthObstacleRectTop3.collision(playerRect, fifthObstacleRectTop3, down)
    fifthObstacleRectLeft5Coll = fifthObstacleRectLeft5.collision(playerRect, fifthObstacleRectLeft5, right)
    fifthObstacleRectTop4Coll = fifthObstacleRectTop4.collision(playerRect, fifthObstacleRectTop4, down)
    fifthObstacleRectLeft6Coll = fifthObstacleRectLeft6.collision(playerRect, fifthObstacleRectLeft6, right)
    fifthObstacleRectTop5Coll = fifthObstacleRectTop5.collision(playerRect, fifthObstacleRectTop5, down)
    fifthObstacleRectLeft7Coll = fifthObstacleRectLeft7.collision(playerRect, fifthObstacleRectLeft7, right)

    sixthObstacleRectTopColl = sixthObstacleRectTop.collision(playerRect, sixthObstacleRectTop, down)
    sixthObstacleRectLeftColl = sixthObstacleRectLeft.collision(playerRect, sixthObstacleRectLeft, left)
    sixthObstacleRectRightColl = sixthObstacleRectRight.collision(playerRect, sixthObstacleRectRight, right)
    sixthObstacleRectTop2Coll = sixthObstacleRectTop2.collision(playerRect, sixthObstacleRectTop2, down)

    deathBarrier1Coll = deathBarrier1.collision(playerRect, deathBarrier1, down)
    deathBarrier2Coll = deathBarrier2.collision(playerRect, deathBarrier2, down)
    deathBarrier4Coll = deathBarrier4.collision(playerRect, deathBarrier4, right)
    # movingDeath1Coll = movingDeath1.collision(playerRect, movingDeath1, right)
    deathBarrier5Coll = deathBarrier5.collision(playerRect, deathBarrier5, right)

    bouncePadColl = bouncePad.collision(playerRect, bouncePad, up)
    # finishLineRectColl = finishLineRect.collision(playerRect, finishLineRect, right)

    if playerRect.health >= 1:
        for f in floorGroup:
            f.locationX -= speed

        for o in obstacleGroup1:
            o.locationX -= speed

        for o in obstacleGroup2:
            o.locationX -= speed

        for o in obstacleGroup3:
            o.locationX -= speed

        for o in obstacleGroup4:
            o.locationX -= speed

        for o in obstacleGroup5:
            o.locationX -= speed

        for o in obstacleGroup6:
            o.locationX -= speed

        for d in deathBarrierGroup:
            d.locationX -= speed

        for b in bounceGroup:
            b.locationX -= speed

        for f in finishGroup:
            f.locationX -= speed

    playerRect.draw()

    if playerRect.locationX <= 0:
        deathMessage = deathFont.render("YOU HAVE DIED", True, BLACK)
        display.blit(deathMessage, (470, 250))
        playerRect.health -= 1
        if time % 360 == 0:
            exit()

    if len(collisionsDeath):
        playerRect.health -= 1
    if playerRect.health <= 0:
        deathMessage = deathFont.render("YOU HAVE DIED", True, BLACK)
        display.blit(deathMessage, (470, 250))
        if time % 360 == 0:
            exit()

    if len(collisionsFinish):
        if playerRect.health >= 1:
            victoryMessage = deathFont.render("YOU HAVE WON, CONGRATULATIONS", True, BLACK)
            display.blit(victoryMessage, (170, 250))
            if time % 360 == 0:
                exit()