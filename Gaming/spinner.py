import random, time, sys

options = ['🍒','🍀','🔔','🥠','🍋']

machine = []

def spin(reels=3, spins=15):
    global machine
    for i in range(spins):
        machine = [random.choice(options) for _ in range(reels)]
        sys.stdout.write("\r" + " | ".join(machine))
        sys.stdout.flush()
        time.sleep(0.1 + i * 0.02)
    print()
    return machine
