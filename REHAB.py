import pygame
from os import path
from random import randrange, randint
pygame.init()

# Peli-ikkunan asetukset
scWidth = 400
scHight = 400


sc=pygame.display.set_mode((scWidth, scHight))
sc.fill([169,203,102])
pygame.display.set_caption("Rehab")


# Pelin nopeus / Sanken nopeus
tick = pygame.time.Clock()


# sanken asetukset
sBlock = 20
sColor = (64, 64, 64)


def Snake(sBlock, sList):
    for _ in sList:
        pygame.draw.rect(sc, sColor, [_[0], _[1], sBlock, sBlock])


def drawGrid(): #idk mut se toimii
    for z in range(0, scWidth, sBlock):
        for c in range(0, scHight, sBlock):
            rect = pygame.Rect(z, c, sBlock, sBlock)
            pygame.draw.rect(sc, [0,0,0], rect, 1)

def horsEndPic():

    ohors = "\ohors.png"
    z1 = "\Z.png"
    juan = "\juan.png"
    hors1 = "\hors1.png"

    if a == 0:
        imgPath = path.dirname(__file__) + hors1

    if a == 1:
        imgPath = path.dirname(__file__) + juan

    if a == 2:
        imgPath = path.dirname(__file__) + z1

    if a == 3:
        imgPath = path.dirname(__file__) + ohors

    imp = pygame.image.load(rf"{imgPath}")
    sc.blit(imp, (0,0))

# Kirjoittaminen peli-ikkunalle + asetukset
fontStyle = pygame.font.SysFont(None, 30)

def message(MSG, color):
    msg = fontStyle.render(MSG, True, color)
    sc.blit(msg, [3, scHight /3])

def Score(pisteet):
    value = fontStyle.render("Pisteet: " + str(pisteet), True, [255, 255, 255])
    sc.blit(value, [0, 0])

# Main gameloop
def gameLoop():
    global a
    a = randint(0,3)

    running=True
    gameOver = False


    # Sanken aloitus sijainti + muut Sanken pelin sisäiset asetukset
    x1 = scWidth/2
    y1 = scHight/2

    xChange = 0
    yChange = 0

    sList = []
    sLength = 2


    # Omenan random sijainti kartalla + sen koordinaatien pyöristäminen toimiviksi luvuiksi 
    oX = round(randrange(0, scWidth-20)/20)*20
    oY = round(randrange(0, scHight-20)/20)*20


    while running:

        while gameOver == True:
            sc.fill([0,0,0])    
            horsEndPic()
            message("ESC To give up  SPACE For A Fresh Start", [255,255,255])
            Score(sLength - 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        gameOver = False
                    
                    if event.key == pygame.K_SPACE:
                        gameLoop()


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print("AAAAAAAA")
                running = False

            # Lopeta peli painamalla esc
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Nuoli + wasd näppäin liikkeet
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    xChange = -sBlock
                    yChange = 0

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xChange = sBlock
                    yChange = 0

                elif event.key == pygame.K_UP or  event.key == pygame.K_w:
                    xChange = 0
                    yChange = -sBlock

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    xChange = 0
                    yChange = sBlock

                elif event.key == pygame.K_SPACE:

                    print(":3")



        # Jos sanken x tai y arvo on yli tai alle peli-ikkunan rajojen arvot -> häviät pelin
        if x1 >= scWidth or x1 < 0 or y1 >= scHight or y1 < 0:
            gameOver = True
        

        # Madon liikeet
        x1 += xChange
        y1 += yChange


        # Taustan päivittäminen
        sc.fill([169,203,102])
        drawGrid()


        # Piirrä omena
        pygame.draw.rect(sc, [255,0,0], [oX, oY, 20, 20])


        # Sanken pituuden lisääminen ja piirtäminen
        sHead = []
        sHead.append(x1)
        sHead.append(y1)
        sList.append(sHead)

        if len(sList) >= sLength:
            del sList[0]

        for x in sList[:-1]:
            if x == sHead:
                gameOver = True

        Snake(sBlock, sList)
        

        # Sanken x ja y coordinaatien rikkominen xy listoihin
        x_list = [x4 for x4, _ in sList] 
        y_list = [y4 for _, y4 in sList]


        # Piirrä pisteet
        Score(sLength - 2)
        pygame.display.update()


        # Omenan syönti
        if x1 == oX and y1 == oY:
            sLength += 1
            print("Yums!!")
            oX = round(randrange(0, scWidth-20)/20)*20
            oY = round(randrange(0, scHight-20)/20)*20
            
            # Tarkista että omeanan pos ei ole sanken sisällä
            while oX in x_list and oY in y_list:
                oX = round(randrange(0, scWidth-20)/20)*20
                oY = round(randrange(0, scHight-20)/20)*20
            

        tick.tick(16)

    pygame.quit()
    quit()

gameLoop()