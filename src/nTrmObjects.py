import bpy
import bpy_extras
import mathutils


class NeoTrmEdge(bpy.types.Operator, bpy_extras.object_utils.AddObjectHelper):
    bl_idname = "mesh.neo_trm_edge"
    bl_label = "TRM Edge"
    bl_options = {'REGISTER', 'UNDO'}

    left_wall_bottom: bpy.props.FloatVectorProperty(
        name="Left Wall Bottom",
        subtype='TRANSLATION',
        size=2,
        precision=6,
        default=(-2.0, 0.0),
    )

    left_wall_top: bpy.props.FloatVectorProperty(
        name="Left Wall Top",
        subtype='TRANSLATION',
        size=2,
        precision=6,
        default=(-2.574, 0.571),
    )

    right_wall_bottom: bpy.props.FloatVectorProperty(
        name="Right Wall Bottom",
        subtype='TRANSLATION',
        size=2,
        precision=6,
        default=(2.0, 0.0),
    )

    right_wall_top: bpy.props.FloatVectorProperty(
        name="Right Wall Top",
        subtype='TRANSLATION',
        size=2,
        precision=6,
        default=(2.574, 0.571),
    )

    def execute(self, context):
        self.add(context)

        return {'FINISHED'}

    def add(self, context):
        verts = [
            mathutils.Vector((self.left_wall_top.x, 0.0, self.left_wall_top.y)),
            mathutils.Vector((self.left_wall_bottom.x, 0.0, self.left_wall_bottom.y)),
            mathutils.Vector((0.0, 0.0, 0.0)),
            mathutils.Vector((self.right_wall_bottom.x, 0.0, self.right_wall_bottom.y)),
            mathutils.Vector((self.right_wall_top.x, 0.0, self.right_wall_top.y)),
        ]

        edges = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 4]
        ]

        faces = []

        mesh = bpy.data.meshes.new(name="Trm Edge")
        mesh.from_pydata(verts, edges, faces)
        bpy_extras.object_utils.object_data_add(context, mesh, operator=self)


def add_trm_edge_ui(self, context):
    self.layout.operator(
        NeoTrmEdge.bl_idname,
        text="Trm Edge",
        icon="PLUGIN"
    )


classes = (
    NeoTrmEdge,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.VIEW3D_MT_mesh_add.append(add_trm_edge_ui)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    bpy.types.VIEW3D_MT_mesh_add.remove(add_trm_edge_ui)