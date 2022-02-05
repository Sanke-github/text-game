import sys
import time



def rickroll():
    import webbrowser
    webbrowser.open('https://rb.gy/vzybgk')




def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.45/10)

def keyboard_art():    
      
    ime = input("Enter your good name: \n ")
    for c in ime :
            c = c.upper()
            if (c == "A"):
                print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n")
            elif (c == "B"):
                print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n")
            elif (c == "C"):
                print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n")
            elif (c == "D"): 
                print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n")
            elif (c == "E"): 
                print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n")
            elif (c == "F"):
                print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n")    
            elif (c == "G"):
                print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n")
            elif (c == "H"):
                print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n")
            elif (c == "I"):
                print("..######..\n....##....\n....##....\n....##....\n..######..\n")
            elif (c == "J"):
                print("..######..\n....##....\n....##....\n..#.##....\n..####....\n")
            elif (c == "K"):
                print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n") 
            elif (c == "L"):
                print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n")
            elif (c == "M"):
                print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n")   
            elif (c == "N"):   
                print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n")
            elif (c == "O"):
                print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n")
            elif (c == "P"):
                print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
            elif (c == "Q"):
                print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n")
            elif (c == "R"):
                print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n")
            elif (c == "S"):
                print("..######..\n..#.......\n..######..\n.......#..\n..######..\n")  
            elif (c == "T"):
                print("..######..\n....##....\n....##....\n....##....\n....##....\n")
            elif (c == "U"):
                print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n")
            elif (c == "V"):
                print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n")
            elif (c == "W"):
                print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n")
            elif (c == "X"):
                print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n")
            elif (c == "Y"):
                print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n")
            elif (c == "Z"):    
                print("..######..\n......#...\n.....#....\n....#.....\n..######..\n")   
            elif (c == " "):
                print("..........\n..........\n..........\n..........\n")
            elif (c == "."):
                print("----..----\n")

def castle():
    slowprint("now that you have the arrows to kill the ghost\nYou go and kill them with the ghost killing arrows,The ghosts mourn and turn to ashes.\nBehind them you see a treasure")
    slowprint("you open the treasure and find gold,the gold can imprint your name.")
    slowprint("type yor name and recieve your reward")
    slowprint("YOU WON THE GAME CONGRATS!!")
    keyboard_art()
    
    


def continuation_2():
    slowprint("after the fierce battle with the goblins you are now tired.\nYou see a castle along the mountains but this castle is haunted by ghosts.\nThe castle has a treasure which is being guarded by ghosts.\nIn order to kill the ghosts,you need the ghost killing arrows.")
    slowprint("You see a cottage nearby.You go into the cottage,there is a bed and since you are tired you take  rest.")
    slowprint("its time you sleep now, the clock is ticking and the time goes:\n11PM\n12PM\n1AM\n2AM\n3AM\n4AM\n5AM\n6AM\n7AM. And you wake up")
    slowprint("You go towards the castle,passing through the mountains.\nWhen you finally reach it,You are welcomed by a guard.\nHe is no ordinary guard\nIn order to enter the castle, you have to answer this riddle given by the guard.")
    riddle=input("poor people have it,rich people need it and if you eat it you die. what is it? : ")
    if riddle=="nothing":
        slowprint("CORRECT.The guard gives you the ghost killing arrows as a reward")
        castle()
    
    else:
        slowprint("You are wrong.Try again")
        retry1=input("poor people have it,rich people need it and if you eat it you die. what is it? : ") 
        if retry1=="nothing":
            slowprint("CORRECT.The guard gives you the ghost killing arrows as a reward")   
        else:
            ("you have failed again.YOU LOSE.")
            rickroll()



def continuation():
    slowprint('The exit is right in front of you but to go through it you have to answer this riddle')
    answer=input('I have seas without water,forests without wood,deserts without sand and houses with no brick.What am I ? :')
    if answer=="map":
        slowprint("Now a door opens and you are rewarded with a sword and a bow. You are now in a jungle")
        slowprint("You stroll along the jungle and \n SUDDENLY YOU ARE BEING AMBUSHED BY A GROUP OF GOBLINS. \n FYI these creatures are really fast.Now you are left with two options:")
        escape=input('do you wish to run or attack ?')
        if escape=="attack":
            slowprint("Good choice!")
            weapon=input("Now that you have 2 weapons:sword and bow,which one would you wield considering its a close combat(sword/bow) : ")
            if weapon=="sword":
                slowprint('you kill the goblins as the sword is best for close combat')
                continuation_2()
            else:
                slowprint('bow cannot be a feasable option as there is a bunch of goblins and impossible to fight them with a single yielding weapon.\n YOU LOSE')
                rickroll()    
        elif escape=="run":
            slowprint('wrong choice.As mentioned earlier the goblins are pretty fast creatures and can chase you in seconds')
            rickroll() 
    else:
        print('wrong answer,pls use brein')
        exit()



def main():          
    answer=input("do you wanna play a game? (yes/no):\n ")
    if answer=="yes":
            answer=input("so you're in a dark alley where you have no clue about what exists.There are two passsageways; left and right.Where would you choose to go? :\n ")
            if answer=="left":
                answer=input("there's a monster running towards you,do you wish to attack or run? : \n ")
                if answer=="attack":
                    slowprint('WRONG CHOICE-THE MONSTER KILLS YOU \n')
                    rickroll()
            
                if answer=="run":
                    slowprint('great choice,as the monster is too big to pass into the alley in which you are in.  \n ')
                    slowprint('Now there are 3 doors in front of you :')
                    slowprint('in door1 there is a 1860°C fire')
                    slowprint('in door2 there is liquid nitrogen that could freeze you to death')
                    slowprint('in door3 there is a serial killer from 1890s')
                    answer=input("which door do you want to go into : door1,door2,door3 ? : ")
                    if answer=="door3":
                        print('Great choice! as the serial killer must be dead by now.')
                        continuation()
                       
                
                
                else:
                    print('wrong option as you got yourself killed')  
                    rickroll()
            
            
            elif answer=="right":
                slowprint("There are 3 doors in front of you : ") 
                slowprint("1. a room in which a lion has been hungry for 3yrs")
                slowprint("2. a door that leads you into a room full of lava")
                slowprint("3. a door that leads you into a room full of alligators")
                answer=input("which door do you want to go into : door1,door2 or door3 ? : ")
                if answer=="door1":
                    slowprint("Great Choice!,as the lion must be dead by not eating from 3 years.")
                    continuation()

                else:
                    slowprint('wrong option as you got yourself killed')
                    rickroll()

            restart=input('do you wanna play the game again? (yes/no) : ')
            if restart=="yes":
               main()
            else:
               exit()
    
    else:
         slowprint("aight m8 that's cool by me")
main()
