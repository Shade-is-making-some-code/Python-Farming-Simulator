
# Copyright (c) Shaded-Leaf-Development

# game active variable

gameActive = True

# current version

curVer = "0.0.5 Pre-Alpha"

# player crop variables

hasturnips = 0
hascarrots = 0
haspotatoes = 0
hasonions = 0
hastomatoes = 0
haswheat = 0
hascorn = 0

# player inventory variables

hasTurnipSeed = 0
hasCarrotSeed = 0
hasPotatoPlant = 0
hasOnionSeed = 0
hasTomatoSeed = 0
hasWheatSeed = 0
hasCornSeed = 0
hasWateringCan = False
hasFertilizer = 0

# crop watering variables

turnipsNeedWater = False
carrotsNeedWater = False
potatoesNeedWater = False
onionsNeedWater = False
tomatoesNeedWater = False
wheatNeedsWater = False
cornNeedsWater = False

# shop price variables

turnipSeedSatchelPrice = 50
carrotSeedSatchelPrice = 70
potatoPlantSatchelPrice = 90
onionSeedSatchelPrice = 110
tomatoSeedSatchelPrice = 130
wheatSeedSatchelPrice = 150
cornSeedSatchelPrice = 200
fertilizerBagPrice = 45
wateringCanPrice = 10

# crop sell value variables

turnipSellvalue = 100
carrotSellValue = 140
potatoSellValue = 180
onionSellvalue = 220
tomatoSellValue = 260
wheatSellValue = 300
cornSellValue = 400

# player currency variable

playerMoney = 60

# sunlight level variable

sunLVL = 0

# dampness variable

airDampness = 0

# Functions

def shopFunc():

    global hasTurnipSeed
    global hasCarrotSeed
    global hasPotatoPlant
    global hasOnionSeed
    global hasTomatoSeed
    global hasWheatSeed
    global hasCornSeed
    global hasWateringCan
    global playerMoney

    print("greetings, welcome to the shop! we've got many seeds for you to choose from!")
    print("")
    print("here's what we got, all seed satchels have 3 seeds/units in em'")
    print("Turnip Seed Satchel: " + str(turnipSeedSatchelPrice) + " Dolans")
    print("Carrot Seed Satchel: " + str(carrotSeedSatchelPrice) + " Dolans")
    print("Potato Plant Satchel: " + str(potatoPlantSatchelPrice) + " Dolans")
    print("Onion Seed Satchel: " + str(onionSeedSatchelPrice) + " Dolans")
    print("Tomato Seed Satchel: " + str(tomatoSeedSatchelPrice) + " Dolans")
    print("Wheat Seed Satchel: " + str(wheatSeedSatchelPrice) + " Dolans")
    print("Corn Seed Satchel: " + str(cornSeedSatchelPrice) + " Dolans")
    print("Watering Can: " + str(wateringCanPrice) + " Dolans")
    print("")
    print("So, buyin' something?")
    shopQuery = input("Purchase: ")
    if (shopQuery == "Turnip" or "Turnip Seed Satchel" or "Turnip Satchel" and playerMoney == turnipSeedSatchelPrice):
        print("alrighty! here ya go! one Satchel o' turnip seeds.")
        print("(you got a Satchel of turnip seeds!)")
        print("(Dolans - " + str(turnipSeedSatchelPrice) + ")")
        hasTurnipSeed = hasTurnipSeed +3
        playerMoney = playerMoney - turnipSeedSatchelPrice
    elif (shopQuery == "Turnip" or "Turnip Seed Satchel" or "Turnip Satchel" and playerMoney < turnipSeedSatchelPrice):
        print("Oh... you don't got enough Dolans im afraid, come back when you have enough Dolans to purchase this item")

    if (shopQuery == "Carrot" or "Carrot Seed Satchel" or "Carrot Satchel" and playerMoney == carrotSeedSatchelPrice):
        print("alrighty! here ya go! one satchel o' carrot seeds.")
        print("(You got a Satchel of carrot seeds!)")
        print("(Dolans -" + str(carrotSeedSatchelPrice) + ")")
        hasCarrotSeed = hasCarrotSeed +3
        playerMoney = playerMoney - carrotSeedSatchelPrice
    elif (shopQuery == "Carrot" or "Carrot Seed Satchel" or "Carrot Satchel" and playerMoney < carrotSeedSatchelPrice):
        print("Oh... you don't got enough Dolans im afraid, come back when you have enough Dolans to purchase this item")

def helpFunc():
    print("")
    print("==================== HELP DIALOGUE ====================")
    print("")
    print("Commands:")
    print("Help: Displays this help dialogue")
    print("Shop: activates the shop menu, go to the shop to buy and sell crops, as well as fertilizer!")
    print("Exit: enter the shutdown dialogue, *warning, at it's current state, you CANNOT save your progress!*")
    print("Water: use this to water a plant, if you have none, and if you don't have a watering can, this won't")
    print("do anything")
    print("Harvest: use this to harvest your crops after they've grown, similarily to water, if none of your crops")
    print("have matured, this does nothing.")
    print("Plant: use this to plant seeds you may have")
    print("")
    print("=======================================================")
    print("")

def plantFunc():
    print("")
    seedQuery = input("Plant what seed?: ")
    if (seedQuery == "Turnip" and hasTurnipSeed == 0):
        print("you don't have any Turnip seeds to plant...")
        print("")
    elif (seedQuery == "Turnip" and hasTurnipSeed >= 1):
        print("you planted the turnip seed into the soft soil")
        print("")

    if (seedQuery == "Carrot" and hasCarrotSeed == 0):
        print("you don't have any Carrot seeds to plant...")
        print("")
    elif (seedQuery == "Carrot" and hasCarrotSeed >= 1):
        print("you planted the Carrot seed into the soft soil")
        print("")

    if (seedQuery == "Potato" and hasPotatoPlant == 0):
        print("you don't have any Potato plants to plant...")
        print("")
    elif (seedQuery == "Potato" and hasPotatoPlant >= 1):
        print("you planted the Potato plant in the soft soil")
        print("")

def exitFunc():
    print("thank you for playing this farming simulation game!")
    exitConfirm = input("TYPE 'OK' TO QUIT: ")
    if (exitConfirm == "OK"):
      exit()
    elif(exitConfirm != "OK"):
      print("please type 'OK' to exit, it is case sensitive")


def buglistFunc():
    print("")
    print("---------------------------BUGLIST---------------------------")
    print("")
    print("KNOWN BUGS:")
    print("")
    print("In Pre-Alpha 0.0.5, when in the shop dialogue, if you purchased anything at all, you would for some reason")
    print("purchase everything in the store, despite only having 60 Dolans to start")
    print("")
    print("FIXED BUGS:")
    print("In pre-alpha 0.0.1, during the exit dialogue, if you typed in anything")
    print("but OK, you'd get endlessly spammed with the same message due to an error")
    print("in the code structure")
    print("")
    print("-------------------------------------------------------------")
    print("")

def checkFunc():
    checkQuery = input("Check What?: ")
    if (checkQuery == "Money"):
        print("You currently have " + str(playerMoney) + " Dolans")
        print("")
    elif (checkQuery == "Inventory"):
        print("You have " + str(hasTurnipSeed) + " Turnip seeds")
        print("You have " + str(hasCarrotSeed) + " Carrot seeds")
        print("You have " + str(hasPotatoPlant) + " Potato plants")
        print("You have " + str(hasOnionSeed) + " Onion seeds")
        print("You have " + str(hasTomatoSeed) + " Tomato seeds")
        print("You have " + str(hasWheatSeed) + " Wheat seeds")
        print("You have " + str(hasCornSeed) + " Corn seeds")

def main():

  print("Welcome to Python Farming Simulator!")
  print("")
  print("the current version is: " + curVer)
  print("")
  print("type 'Help' in the command input to display the help dialogue box")
  print("anyways, have fun!")

  while (gameActive == True):
    print("")
    playerInp = input(">>> ")

    if (playerInp == "Help"):
        helpFunc()

    elif(playerInp == "Shop"):
        shopFunc()

    elif(playerInp == "Plant"):
        plantFunc()

    elif(playerInp == "Buglist"):
        buglistFunc()

    elif(playerInp == "Exit"):
        exitFunc()

    elif(playerInp == "Check"):
        checkFunc()

































if __name__ == "__main__":
  main()