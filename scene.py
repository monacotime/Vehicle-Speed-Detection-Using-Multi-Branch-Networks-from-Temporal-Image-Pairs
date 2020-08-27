import bpy

#------------------------------------------------
#print("hi")
# bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
#bpy.ops.mesh.primitive_cube_add( size=1, location=(0,0,0))

#print(dir(bpy.data.objects["Car"]))

# print(dir(bpy.data.textures.get("body")))

# bpy.data.materials["Body"].diffuse_color[0, 0.00289276, 1, 1]
#------------------------------------------------

active_object = bpy.context.view_layer.objects.active 
Car = bpy.data.objects["Car"]

def select_car():
    bpy.ops.object.select_all(action='DESELECT')

    active_object = Car
    Car.select_set(True)

bpy.ops.transform.translate(value = (0,1,0))