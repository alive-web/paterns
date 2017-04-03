__author__ = 'plevytskyi'


# The abstract product 1
class Obstacle:
    def action(self):
        raise NotImplementedError


# The abstract product 2
class Character:
    def interactWith(self, obstacle):
        raise NotImplementedError


# The product 2
class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a {}".format(obstacle.action()))


# The product 2
class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a {}".format(obstacle.action()))


# The product 1
class Puzzle(Obstacle):
    def action(self):
        return "Puzzle"


# The product 1
class NastyWeapon(Obstacle):
    def action(self):
        return "NastyWeapon"


# The Abstract Factory:
class GameElementFactory:
    def makeCharacter(self):
        raise NotImplementedError

    def makeObstacle(self):
        raise NotImplementedError


# Concrete factories:
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self):
        return Kitty()

    def makeObstacle(self):
        return Puzzle()


# Concrete factories:
class KillAndDismember(GameElementFactory):
    def makeCharacter(self):
        return KungFuGuy()

    def makeObstacle(self):
        return NastyWeapon()


# run
class GameEnvironment:
    def __init__(self, factory):
        # self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)

g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()