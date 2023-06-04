# zero - the Blender add-on that does absolutely nothing

This is an experimental project to test Blender add-on capabilities.

## Dirty tricks

### How to start a modal without user intervention in any context

[zero/Modal.py](https://github.com/simonecesano/blender-Zero/blob/main/zero/Modal.py) shows how to do this.

The trick is to create an "ambush function" that waits for the context to come into being, and then boom!
it registers the modal in that context.

Broken down:

1. when the modal registers it also registers a timer that runs a function
2. this function checks that the right context exists
3. and then stops checking (unregistering the timer)

In more detail:

- you create your modal operator
- _before that_ you one (or more) functions that
  1. go through the areas and regions until they find the right one
  2. when it finds the context, it calls ```INVOKE_DEFAULT``` on your modal operator 
  3. and then unregisters itself
  4. and if it doesn't find the context return the number of seconds until they should be called again
- making sure you create one for each context you need the modal operator in
- you register your functions as timers upon registering the modal operator like this:
  ```bpy.app.timers.register(delayed_startup_area_3d)```
- and unregister them upon unregistering the modal operator

Check out the docs:

- [bpy.app.timers.register](https://docs.blender.org/api/current/bpy.app.timers.html)
- [bpy.context.temp_override](https://docs.blender.org/api/current/bpy.types.Context.html#bpy.types.Context.temp_override)

And the nice writeup on context override in blender 3.2 and later [here](https://b3d.interplanety.org/en/context-overriding-in-blender-3-2-and-later)