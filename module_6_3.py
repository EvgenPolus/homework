import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    speed = 1


    def move(self, dx, dy, dz):
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.dz = dz * self.speed
        if dx < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [self.dx, self.dy, self.dz]

    def get_cords(self):
        # self.x = x
        # self.y = y
        # self.z = z
        print(f' X: {self.dx}, Y: {self.dy}, Z: {self.dz}')


    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.beak = True
    def lay_eggs(self):
        self.eggs = random.randint(1, 4)
        print(f'Here are(is) {self.eggs} eggs for you')

class AquaticAnimal(Animal):
    def __init__(self):
        super().__init__()
        self._DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.dz = self.dz - abs(dz)
        self.speed = self.speed / 2

class PoisonousAnimal(Animal):
    def __init__(self):
        super().__init__()
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    def __init__(self, _DEGREE_OF_DANGER):
        super().__init__()
        self._DEGREE_OF_DANGER = _DEGREE_OF_DANGER
        self.sound = "Click-click-click"



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs()