import random


speed = random.randint(0,100)

print("speed: ", speed)

def speed_to_mov(speed):
    # mov = "movement in meters in 0.25s:"
    return round((speed*1000)/(60*60*4),5)

print(speed_to_mov(speed))

def init_pos():
    return round(random.uniform(3,5),5)

print("init pos:", init_pos())