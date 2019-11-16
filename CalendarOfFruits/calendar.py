import random
from graphics import *






# dictionary of apple varieties

dictionaryOfApples = {
    1: "Adams Pearmain",
    2: "Admiral",
    3: "Aia LLu",
    4: "Airlie Red Flesh",
    5: "Akane",
    6: "Akero",
    7: "Alkmene",
    8: "Allington Pippin",
    9: "Ambrosia",
    10: "Anna",
    11: "Annurca",
    12: "Antonovka",
    13: "Apollo",
    14: "Ariane",
    15: "Arkansas Black",
    16: "Arthur Turner",
    17: "Ashmead's Kernel",
    18: "Aurora Golden Gala",
    19: "Autumn Glory",
    20: "Bailey",
    21: "Baldwin",
    22: "Ballyfatten",
    23: "Bardsey Island Apple",
    24: "Beacon",
    25: "Beauty of Bath",
    26: "Belle de Boskoop",
    27: "Ben Davis",
    28: "Beverly Hills",
    29: "Brigit Bonnier",
    30: "Bismark",
    31: "Blenheim Orange",
    32: "Bloody Ploughman",
    33: "Bottle Greening",
    34: "Braeburn",
    35: "Bramley",
    36: "Bravo de Esmolfe",
    37: "Breedon Pippin",
    38: "Brina" ,
    39: "Byfleet Seeding",
    40: "Calville Blanc d'hiver",
    41: "Cameo",
    42: "Campanino",
    43: "Carolina Red June",
    44: "Carroll",
    45: "Carter's Blue",
    46: "Champion",
    47: "Catshead",
    48: "Charles Ross",
    49: "Chelmsford Wonder",
    50: "Chiver's Delight",
    51: "Claygate Pearmain",
    52: "Clivia",
    53: "Cornish Gilliflower",
    54: "Cortland",
    55: "Cosmic Crisp",
    56: "Court Pendu Plat",
    57: "Cox's Orange Pippin",
    58: "Cripps Pink",
    59: "Crispin",
    60: "Crimson Delight",
    61: "Crimson Gold",
    62: "Criterion",
    63: "D'Arcy Spice",
    64: "Delblush",
    65: "Delcorf",
    66: "Delfloga",
    67: "Delfopion",
    68: "Delrouval",
    69: "Deltana",
    70: "Devonshire",
    71: "Discovery",
    72: "Dorsett Golden",
    73: "Dougherty",
    74: "Dudley Winter",
    75: "Egle",
    76: "Early Victoria",
    77: "Edward VII",
    78: "Egremont Russet",
    79: "Ein Shemer",
    80: "Ellison's Orange"
    
    
    
    }



# dictionary of bannana varieties

dictionaryOfBananas = {
    1: "Chingan",
    2: "Lacatan",
    3: "Lady Finger",
    4: "Pisang jari buaya",
    5: "Senorita",
    6: "Sinwobogi",
    7: "Dwarf Cavendish",
    8: "Giant Cavendish",
    9: "Formosana",
    10: "Grand Nain",
    11: "Masak Hijau",
    12: "Robusta",
    13: "Red Dacca",
    14: "Dwarf Red",
    15: "Flhorban 920",
    16: "Gros Michel",
    17: "East Africa Highland",
    18: "Bodles altafort",
    19: "Golden Beauty",
    20: "Atan",
    21: "Goldfinger",
    22: "maqueno",
    23: "Popoulu",
    24: "Mysore",
    25: "French plantain",
    26: "Green French",
    27: "Horn plantain",
    28: "Nedran",
    29: "Pink French",
    30: "Tiger",
    31: "Pome",
    32: "Prata-ana",
    33: "Latunda",
    34: "Pisang Seribu",
    35: "Plu",
    36: "Kalamagol",
    37: "Pisang Awak",
    38: "Ney Poovan",
    39: "Blue Java" ,
    40: "Bluggoe",
    41: "Silver Bluggoe",
    42: "Pelipita",
    43: "Saba",
    44: "Cardaba" ,
    45: "Benedetta" ,
    46: "Tiparot",
    47: "Musa azizii",
    48: "Musa barioensis",
    49: "Musa bauensis",
    50: "Musa Beccarii",
    51: "Musa boman",
    52: "Musa bormeensis",
    53: "Musa bukensis",
    54: "Musa campestris",
    55: "Musa coccinea",
    56: "Musa exotica",
    57: "Musa fitzalanii",
    58: "Musa gracilis",
    59: "Musa hirta",
    60: "Musa jackeyi",
    61: "Musa johnsii",
    62: "Musa lawitiensis",
    63: "Musa lokok",
    64: "Musa lolodensis",
    65: "Musa maclay",
    66: "Musa monticola",
    67: "Musa muluensis",
    68: "Musa paracoccinea",
    69: "Musa peekelii",
    70: "Musa salaccensis",
    71: "Musa textilis",
    72: "Musa tuberculata",
    73: "Musa violascens",
    74: "Musa viridis",
    75: "Musa voonii",
    76: "Musa ingens",
    77: "Musa acuminata",
    78: "Musa aurantiaca",
    79: "Musa balbisiana",
    80: "Musa banksii"
    
    
    
    
    
    
    
    
    }


# dictionary of grape varieties

dictionaryOfGrapes = {
    1: "Abbuoto",
    2: "Abouriou",
    3: "Alexandroouli",
    4: "Akhasheni",
    5: "Abrusco",
    6: "Acolon",
    7: "Ada Karasi",
    8: "Affenthaler",
    9: "Agiorgitiko",
    10: "Aglianico",
    11: "Babic",
    12: "Bachet Noir",
    13: "Baco Noir",
    14: "Baga",
    15: "Barbera",
    16: "Barbera del Sannio",
    17: "Barbera Sarda",
    18: "Barsaglina",
    19: "Beaunoir",
    20: "Bekari",
    21: "Caberinta",
    22: "Cabernet Carbon",
    23: "Cabernet Colonjes",
    24: "Cabernet Cortis" ,
    25: "Cabernet Cubin",
    26: "Cabernet Dorio",
    27: "Cabernet Franc",
    28: "Cabernet Gernischt",
    29: "Cabernet Jura",
    30: "Cabernet Mitos",
    31: "Dolcetto",
    32: "Domina",
    33: "Dornfelder",
    34: "Douce",
    35: "Douce Noire grise",
    36: "Dunkelfelder",
    37: "Duras",
    38: "Dureza",
    39: "Durif",
    40: "Ederena",
    41: "Enfarine noir",
    42: "Espadeiro",
    43: "Etraire",
    44: "Fer",
    45: "Ferron",
    46: "Feteasca neagra",
    47: "forcallat tinta",
    48: "Fortana",
    49: "Frappato",
    50: "Freisa",
    51: "Fruhroter Veltiner",
    52: "Fumin",
    53: "Gaglioppo",
    54: "Gamashara",
    55: "Gamay",
    56: "Gamaret",
    57: "Garanoir",
    58: "Garnatxa",
    59: "Giro",
    60: "Gouget noir",
    61: "Graciano",
    62: "Grisa nera",
    63: "Greco nera" ,
    64: "Grignolino",
    65: "Gropello",
    66: "Grolleau",
    67: "Gros Verdot",
    68: "Gueuche noir",
    69: "Helfensteiner",
    70: "Heroldrebe",
    71: "Hondarribi Beltza",
    72: "Hron",
    73: "Humagne Rouge",
    74: "Joubertin",
    75: "Juan Garcia",
    76: "Jurancon noir",
    77: "Kadarka",
    78: "Kakhet",
    79: "Kalecik Karasi",
    80: "Kindzmarauli"
    
    
    
    
    }














monthDictionary = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
    
    
    }



# months that are displayed when selecting a month
arrayOfMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September" , "October", "November", "December"]



# fruit that is displayed when selecting a fruit
arrayOfFruit = ["Apple", "Banana", "Grape"]






# draws out the months
def drawListOfMonths(win):
     
    

    # variables to handle moving the boxes
    movingPointX = 0
    movingPointY = 0
    indexOfArrayOfMonths = 0


    titleForMonthSelection = Text(Point(500, 50), "Please select a month.")
    titleForMonthSelection.setSize(30)


    monthRectangle = Rectangle(Point(10, 250), Point(247.5, 300))
    monthRectangle.setWidth(3)


    textForMonth = Text(Point(128.75, 275), arrayOfMonths[indexOfArrayOfMonths])
    textForMonth.setSize(25)




    titleForMonthSelection.draw(win)
    textForMonth.draw(win)
    monthRectangle.draw(win)



    # displays all of the months evenly
    for monthCount in range(1, 12):
        
        indexOfArrayOfMonths += 1
        
        if monthCount == 4 or monthCount == 8:
            movingPointY += 100
            movingPointX = -247.5
        
        
        movingPointX += 247.5
        
        newMonthRectangle = monthRectangle.clone()
        newTextForMonth = textForMonth.clone()
        newTextForMonth.setText(arrayOfMonths[indexOfArrayOfMonths])
        
        newMonthRectangle.move(movingPointX, movingPointY)
        newTextForMonth.move(movingPointX, movingPointY)
        
        
        
        
        newMonthRectangle.draw(win)
        newTextForMonth.draw(win)








# used to clear the window
def undraw(win):
    for item in win.items[:]:
        item.undraw()
    
    
    
    
# Gets the mouse click to determine wich month was selected then returns the month
def getMouseClickForMonths(win):   
    
    currentMonth = ""
    
    didSelectMonth = False
    
    while didSelectMonth == False: 

        clickPoint = win.getMouse()


        mouseX = clickPoint.getX()
        mouseY = clickPoint.getY()


        if mouseX in range(10, 248) and mouseY in range(250, 300):
            currentMonth = "January"
            undraw(win)
            didSelectMonth = True 


        elif mouseX in range(257, 495) and mouseY in range(250, 300):
            currentMonth = "February"
            undraw(win)
            didSelectMonth = True
            

        elif mouseX in range(505, 743) and mouseY in range(250, 300):
            currentMonth = "March"
            undraw(win)
            didSelectMonth = True
            
        
        elif mouseX in range(752, 990) and mouseY in range(250, 300):
            currentMonth = "April"
            undraw(win)
            didSelectMonth = True
    # second Line 
        elif mouseX in range(10, 248) and mouseY in range(350, 400):
            currentMonth = "May"
            undraw(win)
            didSelectMonth = True 


        elif mouseX in range(257, 495) and mouseY in range(350, 400):
            currentMonth = "June"
            undraw(win)
            didSelectMonth = True
            

        elif mouseX in range(505, 743) and mouseY in range(350, 400):
            currentMonth = "July"
            undraw(win)
            didSelectMonth = True
            
        
        elif mouseX in range(752, 990) and mouseY in range(350, 400):
            currentMonth = "August"
            undraw(win)
            didSelectMonth = True

    # third Line    
        elif mouseX in range(10, 248) and mouseY in range(450, 500):
            currentMonth = "September"
            undraw(win)
            didSelectMonth = True 


        elif mouseX in range(257, 495) and mouseY in range(450, 500):
            currentMonth = "October"
            undraw(win)
            didSelectMonth = True
            

        elif mouseX in range(505, 743) and mouseY in range(450, 500):
            currentMonth = "November"
            undraw(win)
            didSelectMonth = True
            
        
        elif mouseX in range(752, 990) and mouseY in range(450, 500):
            currentMonth = "December"
            undraw(win)
            didSelectMonth = True

    return currentMonth








# consolidates all the month drawing functions then returns the month that I need
def mainForMonth(win):
    drawListOfMonths(win)
    mon = getMouseClickForMonths(win)
    return mon




#
#
#
#
#
#
#
#
#
#
#
#   Start Fruit selection here



# draws a list of fruit
def drawListOfFruit(win):
    
    moveFruitX = 0
    
    
    indexOfFruitText = 0
    
    
    titleForFruitSelection = Text(Point(500, 50), "Please select a fruit.")
    titleForFruitSelection.setSize(30)
    
    
    
    fruitRectangle = Rectangle(Point(71.875, 250), Point(309.375, 300))
    fruitRectangle.setWidth(3)
    
    
    
    textForFruit = Text(Point(190.625, 275), arrayOfFruit[indexOfFruitText])
    textForFruit.setSize(25)
    
    
    titleForFruitSelection.draw(win)
    fruitRectangle.draw(win)
    textForFruit.draw(win)
    
    
    
    for f in range(1,3):
        
        indexOfFruitText += 1
        
        moveFruitX += 309.375
        
        
        newFruitRectangle = fruitRectangle.clone()
        newTextForFruit = textForFruit.clone()
        newTextForFruit.setText(arrayOfFruit[indexOfFruitText])
        
        
        
        newFruitRectangle.move(moveFruitX, 0)
        newTextForFruit.move(moveFruitX, 0)
        
        
        
        newFruitRectangle.draw(win)
        newTextForFruit.draw(win)
        
        
        



# gets mouse click and then returns the users choice of fruit
def getMouseClickForFruit(win):
    
    fruitSelected = ""
    
    didSelectFruit = False
    
    while didSelectFruit == False:
        
        fruitClickPoint = win.getMouse()
        
        
        fruitMouseX = fruitClickPoint.getX()
        fruitMouseY = fruitClickPoint.getY()
        
        
        
        if fruitMouseX in range(71, 310) and fruitMouseY in range(250, 300):
            fruitSelected = "Apple"
            undraw(win)
            didSelectFruit = True
            
        elif fruitMouseX in range(381, 619) and fruitMouseY in range(250, 300):
            fruitSelected = "Banana"
            undraw(win)
            didSelectFruit = True
            
        elif fruitMouseX in range(690, 929) and fruitMouseY in range(250, 300):
            fruitSelected = "Grape"
            undraw(win)
            didSelectFruit = True
        
        
        
    return fruitSelected        
        
        
        
        
        
        
# handles everything for the selection of fruit
def mainForFruit(win):
    drawListOfFruit(win)
    fru = getMouseClickForFruit(win)
    
    return fru
        
    







#
#
#
#
#
#
#   This is where the random calender starts
#
#
#
#
#
#



# fills up randomNumberArray with random numbers

def ranNumber(): 
    
    full = False
    randomNumber = 0
    randomNumberArray = []
    
    while full == False : 
        
        randomNumber = random.randint(1,80)

        
        if randomNumber not in randomNumberArray:
            randomNumberArray.append(randomNumber)
            
        
        if len(randomNumberArray) == 31:
            full = True
            
    return randomNumberArray





# returns list of  random apples using the random numbers in the array as it's indexes

def ranFruitArrays(ranNumbers):
    randomAppleArray = []
    randomBananaArray = [] 
    randomGrapeArray = []

    for ranNum in ranNumbers:
        randomAppleArray.append(dictionaryOfApples[ranNum])
        randomBananaArray.append(dictionaryOfBananas[ranNum])
        randomGrapeArray.append(dictionaryOfGrapes[ranNum])
    
    return randomAppleArray, randomBananaArray, randomGrapeArray
    

  



# function that takes in fruit and returns a new array that can be added to fruitArray

def fruit(fruitType, randomApple, randomBanana, randomGrape): 
    
    fruitArray = []
    
    if fruitType == "Banana":
        fruitArray = randomBanana
        
    elif fruitType == "Apple":
        fruitArray = randomApple
        
    else:
        fruitArray = randomGrape

    return fruitArray


    
    
    
    
    
    
    
# Handles drawing the calender that will display the list of fruits

def drawCalender(win, month, fruitForCalender, arrayOfFruit):
    
    


    # depend on what month. set this to a variable 
    textAtTop = month


    textDisplay = Text(Point(500,50), textAtTop)

    textDisplay.setSize(30)

    textDisplay.draw(win)


    #values 
    indexForRandomArray = 0
    numberOfDays = monthDictionary[month]





    number = 1





    fruit = fruitForCalender




    calenderBox = Rectangle(Point(5, 100), Point(146, 200))
    numberInBox = Text(Point(15,110), number)
    circleAroundNumber = Circle(Point(15, 110), 9)

    headerInBox = Text(Point(71, 130), "{} of the day:".format(fruit))
    appleOfTheDay = Text(Point(71, 170), arrayOfFruit[indexForRandomArray]) 
    appleOfTheDay.setStyle("bold")

    calenderBox.draw(win)
    numberInBox.draw(win)
    circleAroundNumber.draw(win)
    headerInBox.draw(win)
    appleOfTheDay.draw(win)




    moveX = 0
    moveY = 0




    for i in range(1,numberOfDays):
        
        if i % 7 == 0:
            moveY += 100
            moveX = -141
        
        
        moveX += 141
        number += 1
        indexForRandomArray += 1
        
        newBox = calenderBox.clone()
        newNumber = numberInBox.clone()
        newNumber.setText(number)
        newCircle = circleAroundNumber.clone()
        clonedHeader = headerInBox.clone()
        newFruit = appleOfTheDay.clone()
        newFruit.setText(arrayOfFruit[indexForRandomArray])
        
        
        newBox.move(moveX, moveY)
        newNumber.move(moveX, moveY)
        newCircle.move(moveX, moveY)
        clonedHeader.move(moveX, moveY)
        newFruit.move(moveX, moveY)
        
        newBox.draw(win)
        newNumber.draw(win)
        newCircle.draw(win)
        clonedHeader.draw(win)
        newFruit.draw(win)
        
        
    
    
    
    
    
    
    
    
    
    
    
# the main func that is called that will run the program    
def main():
    win = GraphWin("Food Suggestions", 1000, 700)
    
    
    
    # displays months and then gets the current month based on the users selection
    monthForCallender = mainForMonth(win)
    
    
    
    # get the fruit selection
    
    fruitInCallender = mainForFruit(win)
    
    
    
    
    
    
    
    # displays a calender of random fruits 
    random = ranNumber()
    
    apple, banana, grape = ranFruitArrays(random)
    
    arrFruit = fruit(fruitInCallender, apple, banana, grape)
    
    drawCalender(win, monthForCallender, fruitInCallender, arrFruit)
    
    
    
    
    win.getMouse()
    win.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()
    

   
    
    
    