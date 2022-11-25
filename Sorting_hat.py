print("The Sorting Hat")

#The Hogwats Houses
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

#First Question by the soring hat
print('Q1. Do you Like Dawn or Dusk?')
print(' 1) Dawn')
print(' 2) Dusk')

answer =int(input('Enter answer 1 or 2: ')) #input answer

if answer == 1 :
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2 :
    Hufflepuff += 1
    Slytherin += 1
else :
    print('Wrong Input')

#Second Question by the sorting hat
print('Q2. When I am dead, I want people to remember me as?')
print(' 1) The Good')
print(' 2) The Great')
print(' 3) The Wise')
print(' 4) The Bold')

answer = int(input('Enter your answer 1-4:  ')) #input answer

if answer == 1 :
    Hufflepuff += 1
elif answer == 2 :
    Slytherin += 1
elif answer == 3 :
    Ravenclaw += 1
elif answer == 4 :
    Gryffindor += 1
else :
    print("Wrong Input")

#Third Question by the sorting hat
print('Q3) Which kind of instrument most pleases your ear?')
print('1) The Violin')
print('2) The Trumpet')
print('3) The Piano')
print('4) The Drum')

answer = int(input('Enter your answer 1-4: ')) #input answer

if answer == 1 :
    Slytherin += 1
elif answer == 2 :
    Hufflepuff += 1
elif answer == 3 :
    Ravenclaw += 1
elif answer == 4 :
    Gryffindor += 1
else :
    print('Wrong Input')

#Print out House with most Points
if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')