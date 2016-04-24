import time
import subprocess

beep = "resources/beep.wav"
tick = "resources/tick.wav"
success = "resources/success.wav"

def play(n):
    return_code = subprocess.call(["afplay", n])

def init():
    print(chr(27) + "[2J")
    print("###############################")
    print("# C a N i H a z W o R k O u T #")
    print("###############################")
    print("   ")
    print("(1) Jumping Jacks - 40 Seconds")
    print("(2) Wall Sit - 30 Seconds")
    print("(3) Push-up - 30 Seconds")
    print("(4) Abdominal Crunch - 70 Seconds")
    print("(5) Squat - 60 Seconds")
    print("(6) Plank - 30 Seconds")
    print("(7) Barefoot Run - 90 Seconds")
    print("(8) Lunge - 40 Seconds")
    print("(9) Push-up and Rotation - 30 Seconds")
    print("(10) Side Plank LEFT - 20 Seconds")
    print("(11) Side Plank RIGHT - 20 Seconds")
    print("(12) Leg Lift LEFT - 60 Seconds")
    print("(13) Leg Lift RIGHT - 60 Seconds")
    print("(14) Parachuter - 60 Seconds")
    print("   ")
    raw_input("Press Enter to continue...")

def countdown(n):
    print('Get ready (10 seconds)...')
    time.sleep(10)
    play(beep)
    print('GO!!!')
    print("   ")
    while n:
        print(n)
        play(tick)
        time.sleep(5)
        n = n - 5
        if n == 5:
            while n >= 1:
                time.sleep(1)
                n = n - 1
                print(n)
                play(tick)
        if n == 0:
            print("   ")
            print('Timed out!')
            play(success)

def printworkout(n):
    print(chr(27) + "[2J")
    print("##################################")
    print(n)
    print("##################################")
    print("   ")

init()
printworkout("(1) Jumping Jacks - 40 Seconds")
countdown(40)
printworkout("(2) Wall Sit - 30 Seconds")
countdown(30)
printworkout("(3) Push-up - 30 Seconds")
countdown(30)
printworkout("(4) Abdominal Crunch - 70 Seconds")
countdown(70)
printworkout("(5) Squat - 60 Seconds")
countdown(60)
printworkout("(6) Plank - 30 Seconds")
countdown(30)
printworkout("(7) Barefoot Run - 90 Seconds")
countdown(90)
printworkout("(8) Lunge - 40 Seconds")
countdown(40)
printworkout("(9) Push-up and Rotation - 30 Seconds")
countdown(30)
printworkout("(10) Side Plank LEFT - 20 Seconds")
countdown(20)
printworkout("(11) Side Plank RIGHT - 20 Seconds")
countdown(20)
printworkout("(12) Leg Lift LEFT - 60 Seconds")
countdown(40)
printworkout("(13) Leg Lift RIGHT - 60 Seconds")
countdown(40)
printworkout("(14) Parachuter - 60 Seconds")
countdown(60)

print(chr(27) + "[2J")
print("CONGRATULATIONS YOU ARE DONE, 620 SECONDS!")
raw_input("Press Enter to end...")
