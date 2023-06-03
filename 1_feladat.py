class SpaceShip:

    def __init__(self):
        self.fuel = 400
        self.passengers = ['John', 'Steve', 'Sam', 'Danielle']
        self.shields = True
        self.speedometer = 0

    def list_passengers(self):
        for name in self.passengers:
            print(f'Passenger: {name}')

    def add_passenger(self,new_passenger):
        self.passengers.append(new_passenger)
        print(f'{new_passenger} was added to the ship')

    def travel(self, distance):
        print(f'trying to travel: {distance}')
        if self.fuel == 0:
            print('cant go further, tank is empty')
        else:
            new_fuel = self.fuel - (distance/2)
            if new_fuel < 0:
                distance = (self.fuel*2)
                print(f'can only travel: {int(distance)}')
                self.fuel = 0
            else:
                self.fuel = new_fuel
            self.speedometer = self.speedometer + distance
            if self.fuel < 30 and self.shields:
                self.shields = False
                print('fuel is low, turning off shields...')
            print(f'the SpaceShip is at: {int(self.speedometer)}')
            print(f'the spaceship has: {int(self.fuel)} fuel')


#TEST
mySpaceShip = SpaceShip()
mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)