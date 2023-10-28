point= 0
gryffindor=0
hufflepuff=0
slytherin=0
ravenclaw=0
q1= int(input (" Q1. Do you like Dawn or Dusk? 1. Dawn  2. Dusk \n" "answer: "))
if q1 == 1:
  gryffindor= point +5
  ravenclaw= point+5
elif q1== 2:
  hufflepuff= point +5
  slytherin= point +5
else:
  print("wrong input")

q2= int(input("Q2 When i am dead, I want people to remember me as: 1 The Good  2 The Great  3 The Wise  4 The Bold\n" "answer: "))
if q2==1:
  hufflepuff = hufflepuff+5
elif q2 == 2:
  slytherin= slytherin+5
elif q2 == 3:
  ravenclaw= ravenclaw+5
elif q2 == 4:
  gryffindor= gryffindor+5
else:
  print("wrong input")

q3 = int(input("Q3) Which kind of instrument most pleases your ear? 1) The violin 2)The trumpet 3)The piano 4)The drum\n" "answer: "))
if q3==2:
  slytherin = slytherin+5
elif q3 == 4:
  hufflepuff= hufflepuff+5
elif q3 == 1:
  ravenclaw= ravenclaw+5
elif q3 == 3:
  gryffindor= gryffindor+5
else:
  print("wrong input")

q4 = int(input("Q4) Which of these qualities do you value most: 1) bravery 2) intelligence 3)loyalty 4) ambition?\n" "answer: "))
if q4==4:
  slytherin = slytherin+5
elif q4 == 3:
  hufflepuff= hufflepuff+5
elif q4 == 2:
  ravenclaw= ravenclaw+5
elif q4 == 1:
  gryffindor= gryffindor+5
else:
  print("wrong input")
  
  
q5= int(input("Q5) What kind of magical creature would you most like to be: 1)a phoenix 2)a dragon 3)a centaur 4) a mermaid/merman?\n""answer: "))
if q5==4:
  hufflepuff = hufflepuff+5
elif q5 == 3:
  slytherin= slytherin+5
elif q5 == 1:
  ravenclaw= ravenclaw+5
elif q5 == 2:
  gryffindor= gryffindor+5
else:
  print("wrong input")
  
  
q6 = int(input("Q6) In a challenging situation, what do you tend to rely on the most: 1)your courage, 2)your wits, 3)your friends, 4) your determination?\n" "answer: "))
if q6 == 3:
  hufflepuff = hufflepuff+5
elif q6 == 2:
  slytherin= slytherin+5
elif q6 == 4:
  ravenclaw= ravenclaw+5
elif q6 == 1:
  gryffindor= gryffindor+5
else:
  print("wrong input")
  
  
if ravenclaw>hufflepuff:
    print("\nRAVANCLAW")
elif ravenclaw>slytherin:
    print("\nRAVANCLAW")
elif ravenclaw>gryffindor:
    print("\nRAVANCLAW")

elif hufflepuff>slytherin:
    print("\nHUFFLEPUFF")
elif hufflepuff>gryffindor:
    print("\nHUFFLEPUFF")
elif hufflepuff>ravenclaw:
    print("\nHUFFLEPUFF")

elif gryffindor>slytherin:
    print("\nGRYFFINDOR")
elif gryffindor>hufflepuff:
    print("\nGRYFFINDOR")
elif gryffindor>ravenclaw:
    print("\nGRYFFINDOR")

elif slytherin>gryffindor:
    print("\nSLYTHERIN")
elif slytherin>hufflepuffr:
    print("\nSLYTHERIN")
elif slytherin>ravenclawr:
    print("\nSLYTHERIN")

  
  
