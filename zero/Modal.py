import bpy

def delayed_startup_area_3d():
    area_3d = next(iter([area for area in bpy.context.screen.areas if area.type == "VIEW_3D"]))
    if area_3d:
        region = next(iter([region for region in area_3d.regions if region.type == 'WINDOW']))
        print("found 3d view")
        with bpy.context.temp_override(area=area_3d, region=region):
            bpy.ops.object.minimal_modal_operator('INVOKE_DEFAULT')
        bpy.app.timers.unregister(delayed_startup_area_3d)
    return 0.1

def delayed_startup_asset_browser():
    area_types = [ area.type for area in bpy.context.screen.areas ]
    # dont try to make this work like the one above
    # strange things happen - "StopIteration"
    if "FILE_BROWSER" in area_types:
        asset_browser = next(iter([area for area in bpy.context.screen.areas if area.type == "FILE_BROWSER"]))
        if asset_browser.ui_type == "ASSETS":
            print("found asset browser")
            with bpy.context.temp_override(area=asset_browser):
                bpy.ops.object.minimal_modal_operator('INVOKE_DEFAULT')
            bpy.app.timers.unregister(delayed_startup_asset_browser)
    else:
        pass
    return 0.1
    
class MinimalModalOperator(bpy.types.Operator):
    """A minimal modal operator example"""

    bl_idname = "object.minimal_modal_operator"
    bl_label = "Minimal Modal Operator"

    letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    numbers = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]
    arrows =  [ 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW' ]

    
    def modal(self, context, event):
        if event.type == 'ESC':
            return {'PASS_THROUGH'}
        elif event.type in self.letters and event.value == "PRESS":        
            print(event.type, event.ctrl, event.shift, event.alt, event.oskey)
        elif event.type in self.numbers and event.value == "PRESS":        
            print(event.type, event.ctrl, event.shift, event.alt, event.oskey)
        elif event.type in self.arrows and event.value == "PRESS":        
            print(event.type, event.ctrl, event.shift, event.alt, event.oskey)

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        print("invoking from " + __file__)
        print("current area is " + context.area.type)

        if context.area.type in [ 'VIEW_3D', 'FILE_BROWSER' ]:
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "This might not be the right window to call this in")
            return {'CANCELLED'}
        
    def register():
        bpy.app.timers.register(delayed_startup_area_3d)
        bpy.app.timers.register(delayed_startup_asset_browser)
        print("registering from " + __file__)

    def unregister():
        bpy.app.timers.unregister(delayed_startup_area_3d)
        bpy.app.timers.unregister(delayed_startup_asset_browser)
        print("unregistering from " + __file__)

if __name__ == "__main__":
    register()
