import random
Rabbit = False
Loop = 0
RandomNumOfLoops = 4

while Loop < RandomNumOfLoops:
    if Rabbit == True:
        print("Captured a rabbit")
        Loop = Loop + 1
    else:
        print("No rabbits found, running again")
        PlusOrMinus = random.randint(-1,2)
        Loop = Loop + PlusOrMinus
        if Loop >= RandomNumOfLoops:
            print("No rabbits found, ending operation")
        if Loop >= RandomNumOfLoops - 1:
                Rabbit = True