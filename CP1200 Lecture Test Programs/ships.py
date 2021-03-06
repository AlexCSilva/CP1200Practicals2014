__author__ = 'Smoo'

from spacechip import Spaceship


def main():
    serenity = Spaceship("Serenity", 4, 3, 300)
    print(serenity)
    nexus = Spaceship("Nexus", 8, 8, 400)
    tieFighter = Spaceship("Tie", 1, 0, 290)

    ships = [serenity, nexus, tieFighter]

    chosenShip = chooseShip(ships)
    if chosenShip:
        print("I'm flying on", chosenShip.getName())
    else:
        print("I'm walkin'")

def inspectShip(ship):
    print("Inspecting", ship._name)
    ship._name = "Hacked xx"

def chooseShip(ships):
    for ship in ships:
        if ship.hasSpareCapacity():
            return ship
    return None


main()