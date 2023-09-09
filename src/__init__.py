import bpy
from importlib import reload
from . import nTrmObjects

bl_info = {
    "name" : "Neognosis Objects",
    "author" : "Adam Chivers",
    "description" : "",
    "blender" : (2, 90, 0),
    "version" : (1, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

classes = (

)

modules = (
    nTrmObjects,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)

    for m in modules:
        reload(m)
        m.register()


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    for m in modules:
        reload(m)
        m.unregister()


if __name__ == '__main__':
    register()

