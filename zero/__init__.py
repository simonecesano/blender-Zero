import bpy
import os
import sys

from importlib import reload

print("name is " + __name__)

bl_info = {
    "name": "Zero",
    "author": "simone cesano",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Zero",
    "description": "Tools that do nothing",
    "warning": "",
    "category": "Material",
}


from . Panel import *
from . Modal import *

addon_modules =  [ m for m in sys.modules if str(m).startswith(__name__) ]
print(" ".join(addon_modules))
      
class_list = (
    MinimalModalOperator,
)

def register():
    print('registering inside ' + __file__)
    for cls in class_list:
        bpy.utils.register_class(cls)

def unregister():
    for cls in class_list:
        bpy.utils.unregister_class(cls)



    
