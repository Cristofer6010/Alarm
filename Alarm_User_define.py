import time
time2 = "J"
num = 1.0
num2 = 2.0
num3 = 3.0

def datetime1():
    import datetime
    return datetime.datetime.now()

def alarm1():
    while True:
        a = 100
        if a == 100:
            from pygame import mixer
            mixer.init()
            mixer.music.load("drink_water.py.mp3")
            mixer.music.play()
            time.sleep(10)

        from pygame import mixer
        print("Please enter the valid code to stop the Water alarm :")
        b = input()
        if b == "Water":
            mixer.music.stop()
        if b == "Water":
            with open("harry_exrcice.txt", 'a') as f:
                f.write((' This time i drank Water -->> ') + str(datetime1()) + ('\n'))

        if num == 1.0:
            prog2()

def alarm2():
    while True:
        c = 10
        if c == 10:
            from pygame import mixer

            mixer.init()
            mixer.music.load("eye_exercise.py.mp3")
            mixer.music.play()
            time.sleep(10)

        from pygame import mixer
        print("Please enter the valid code to stop the Eye alarm :")
        d = input()
        if d == "Eye":
            mixer.music.stop()
        if d == "Eye":
            with open("hammad_exrcice.txt", 'a') as f:
                f.write((' This time i do eye exercise -->> ') + str(datetime1()) + ('\n'))

        if num2 == 2.0:
            prog3()

def alarm3():
    while True:
        e = 1
        if e == 1:
            from pygame import mixer

            mixer.init()
            mixer.music.load("physical_exercice.py.mp3")
            mixer.music.play()
            time.sleep(10)

        from pygame import mixer
        print("Please enter the valid code to stop the Physical Exercise alarm :")
        fgh = input()
        if fgh == "Physical":
            mixer.music.stop()
        if fgh == "Physical":
            with open("rohan_exrcice.txt", 'a') as f:
                f.write((' This time i do physical exercice -->> ') + str(datetime1()) + ('\n'))

        if num3 == 3.0:
            prog1()

def prog1():
    print("'S' for Second\n'H' for Hour\n'M' for Minutes")
    print("In which dimension you whould like to choose for time :")
    time2 = input()
    print("In how many time we remind your Water alarm :")
    reminder = int(input())
    time1 = time2
    if time1 == "H":
        a007 = 60 * 60 * reminder
    if time1 == "M":
        a007 = 60 * reminder
    if time1 == "S":
        a007 = reminder
    sleep = time.sleep(a007)
    if reminder == reminder:
        alarm1()

def prog2():
    print("'S' for Second\n'H' for Hour\n'M' for Minutes")
    print("In which dimension you whould like to choose for time :")
    time2 = input()
    print("In how many time we remind your Eye alarm :")
    reminder2 = int(input())
    time1 = time2
    if time1 == "H":
        a007 = 60 * 60 * reminder2
    if time1 == "M":
        a007 = 60 * reminder2
    if time1 == "S":
        a007 = reminder2
    sleep = time.sleep(a007)
    if reminder2 == reminder2:
        alarm2()

def prog3():
    print("'S' for Second\n'H' for Hour\n'M' for Minutes")
    print("In which dimension you whould like to choose for time :")
    time2 = input()
    print("In how many time we remind your Physical Exercise alarm :")
    reminder3 = int(input())
    time1 = time2
    if time1 == "H":
        a007 = 60 * 60 * reminder3
    if time1 == "M":
        a007 = 60 * reminder3
    if time1 == "S":
        a007 = reminder3
    sleep = time.sleep(a007)
    if reminder3 == reminder3:
        alarm3()

prog1()
