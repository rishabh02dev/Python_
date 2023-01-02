class Remote():
    pass


# player ke functions player class ke andar aur remote ke functions remove class ke andar
class Player:
    def moveRight(self):
        pass 
    def moveleft(self):
        pass

    def moveTop(self):
        pass
  
remote1 = Remote()
player1 = Player()

if (remote1.isLeftpressed()):
    player1.moveLeft()

#In abstraction the implementation details and the details which are not important to the user are'nt show.