# import random


# speed = random.randint(0,100)

# print("speed: ", speed)

# def speed_to_mov(speed):
#     # mov = "movement in meters in 0.25s:"
#     return round((speed*1000)/(60*60*4),5)

# print(speed_to_mov(speed))

# def init_pos():
#     return round(random.uniform(3,5),5)

# print("init pos:", init_pos())

#Fns
# def select_car():
#     bpy.ops.object.select_all(action='DESELECT')
#     active_object = Car
#     Car.select_set(True)

# def move_car(dist = 1):
#     select_car()
#     # bpy.ops.transform.translate(value = (0, dist, 0))
#     bpy.context.object.location[1] = 3

#------------------------------------------------
#print("hi")
# bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
# bpy.ops.mesh.primitive_cube_add( size=1, location=(0,0,0))
# print(dir(bpy.data.objects["Car"]))
# print(dir(bpy.data.textures.get("body")))
# bpy.data.materials["Body"].diffuse_color = [0, 0.00289276, 1, 1]
#------------------------------------------------

# import pickle

# with open(r".\Dataset\Train\speed.txt", "rb") as fp:   # Unpickling
#     b = pickle.load(fp)

# print(b)

# x = [1,3,4,5,6]
# print(x[1,2])
okay