import bpy
import random
import pickle
random.seed(100)


#---------------------------------------------------------------------------
TRAINING_IMAGE_MAKING_MODE = False #TRUE # IF YOU ARE MAKING TRAINIng IMGS
#---------------------------------------------------------------------------


#Global vars
active_object = bpy.context.view_layer.objects.active 
Car = bpy.data.objects["Car"]
Plate_text = bpy.data.objects["plate_text"]
Car_body_mat = bpy.data.materials["Body"]
train_before = r"C:\Users\monac\Documents\GitHub\DeepForSpeed\Dataset\train\Before"
train_after = r"C:\Users\monac\Documents\GitHub\DeepForSpeed\Dataset\train\After"
test_before = r"C:\Users\monac\Documents\GitHub\DeepForSpeed\Dataset\test\Before"
test_after = r"C:\Users\monac\Documents\GitHub\DeepForSpeed\Dataset\test\After"
train_speed_txt = r".\Dataset\train\speed.txt"
train_licence_txt = r".\Dataset\train\license.txt"
test_speed_txt = r".\Dataset\test\speed.txt"
test_licence_txt = r".\Dataset\test\license.txt"
license_plate_list = ["MH 1010", "BX 2050", "KP 3001", "PX 8029", "GM 8980"]
car_colour_list = [
    [1, 0, 0, 1], 
    [1, 1, 1, 1], 
    [1, 1, 0, 1], 
    [0, 0.5, 1, 1], 
    [0, 1, 0, 1]] #RED, White, Yellow, blue, green
count = 0
speed_list = []
plate_list = []

def speed_to_dist(speed):
    # mov = "movement in meters in 0.25s:"
    return round((speed*1000)/(60*60*4),5)

#Execs

for i in range(100):
    Car_body_mat.diffuse_color = random.choice(car_colour_list)
    
    plate = random.choice(license_plate_list)
    plate_list.append(plate)
    Plate_text.data.body = plate

    speed = random.randint(0,150)
    speed_list.append(speed)

    Car.location.y = round(random.uniform(3,5),5)
    bpy.context.scene.render.filepath = f"{test_before}\{count}.jpg"
    bpy.ops.render.render(write_still = True)

    Car.location.y += speed_to_dist(speed)
    bpy.context.scene.render.filepath = f"{test_after}\{count}.jpg"
    bpy.ops.render.render(write_still = True)

    count += 1
    print("no of pics:", count)

with open(test_speed_txt, "wb") as fp:
    pickle.dump(speed_list, fp)

with open(test_licence_txt, "wb") as fp:
    pickle.dump(plate_list, fp)
