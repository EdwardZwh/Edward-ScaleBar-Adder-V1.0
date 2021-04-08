'''
Edward's ScaleBar Adder V1.0.py
Author: Weiheng(Edward) Zhang. 2021/4/7

Add 600 nm and 1000 nm scale bars to selected spine for classification.
See README.md for usage.
'''

import bpy
import math

class TestPanel(bpy.types.Panel):
    bl_label = "Edward's ScaleBar Adder"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ScaleBar Adder'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add a ScaleBar on selected spine")
        
        Objs = bpy.context.selected_objects
        
        if(len(Objs) != 2):
            return
        else:
            obj1 = Objs[0].location.copy()
            obj2 = Objs[1].location.copy()
            
            locTotal = (obj1 + obj2)/2
            
            rela = obj1 - obj2
            x = rela[0]
            y = rela[1]
            z = rela[2]
            
            yaw = math.atan2(x, z) *180.0/math.pi
            
            padj = math.sqrt(pow(x, 2) + pow(z, 2))
            pitch = math.atan2(padj, y) *180.0/math.pi
            
            yaw = math.radians(yaw)
            pitch = math.radians(pitch)
            
            rot = (pitch, yaw, 0)
            
        
        row = layout.row()
        b1 = row.operator("mesh.primitive_cube_add", icon = 'MESH_CUBE', text = "600 nm")
        b1.size = 0.6
             
        loc = Objs[1].location
        b1.location = loc
        b1.rotation = rot
        

        row = layout.row()
        b2 = row.operator("mesh.primitive_cube_add", icon = 'LIGHTPROBE_CUBEMAP', text = "1000 nm")
        b2.size = 1.0
        
        b2.location = locTotal
        b2.rotation = rot
        
        
    
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    
if __name__ == "__main__":
    register()
