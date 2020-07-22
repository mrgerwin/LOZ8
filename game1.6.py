from pygame_functions6 import *

screenSize(1024,768)
setBackgroundColour('grey')
setAutoUpdate(False)
link = Player()
sword = Sword(link)



octorok1 = Octorok()
octorok2 = Octorok()
octorok3 = Octorok()
enemyList = [octorok1, octorok2, octorok3]
showSprite(link)
for enemy in enemyList:
    showSprite(enemy)

nextFrame = clock()
frame = 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        if keyPressed("down"):
            
            link.orientation =0
            link.move(frame)
        elif keyPressed("up"):
            link.orientation =1
            link.move(frame)
        elif keyPressed("right"):
            link.orientation =2
            link.move(frame)
        elif keyPressed("left"):
            link.orientation =3
            link.move(frame)
        elif keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        #Sword Swing Code
            sword.swing()
            for enemy in enemyList:
                if touching(sword, enemy):
                    enemy.hit()
        if not keyPressed("space") or keyPressed("left") or keyPressed("right") or keyPressed("up") or keyPressed("down"):
            hideSprite(sword)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        
        for enemy in enemyList:
            enemy.move(frame)            
            if touching(enemy, link):
                link.hit()
        updateDisplay()

endWait()