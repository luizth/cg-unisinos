import numpy as np
import pywavefront


def get_data(vertices, indices):
    data = [vertices[ind] for triangle in indices for ind in triangle]
    return np.array(data, dtype=np.float32)


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['pyramid'] = PyramidVBO(ctx)
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['table'] = TableVBO(ctx)
        self.vbos['trout'] = TroutVBO(ctx)
        # self.vbos['teapot'] = TeapotVBO(ctx)
        self.vbos['terrain'] = TerrainVBO(ctx)
        self.vbos['skull'] = SkullVBO(ctx)
        self.vbos['projectile'] = ProjectileVBO(ctx)
        #self.vbos['car'] = CarVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx, objects_path='objects/'):
        self.ctx = ctx
        self.objects_path = objects_path
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attrib: str = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class PyramidVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f'
        self.attrib = ['in_texcoord_0', 'in_position']

    def get_vertex_data(self):

        vertices = [(-1,-1, 1), (1,-1, 1),
                    ( 0, 1, 0), (-1,-1,-1),
                    (1,-1,-1)]
        indices = [(0, 1, 2), (1, 4, 2),
                   (4, 3, 2), (3, 0, 2),
                   (0, 4, 1), (0, 3, 4)]
        vertex_data = get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (0.5, 1)]
        tex_coord_indices = [(0, 1, 2), (1, 2, 0), (2, 0, 1),
                             (0, 1, 2), (1, 2, 0), (0, 1, 2)]
        tex_coord_data = get_data(tex_coord, tex_coord_indices)

        vertex_data = np.hstack((tex_coord_data, vertex_data))
        return vertex_data


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):

        vertices = [(-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1),
                    (-1, 1,-1), (-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]
        tex_coord_data = get_data(tex_coord, tex_coord_indices)

        normals = [ ( 0, 0, 1) * 6,
                    ( 1, 0, 0) * 6,
                    ( 0, 0,-1) * 6,
                    (-1, 0, 0) * 6,
                    ( 0, 1, 0) * 6,
                    ( 0,-1, 0) * 6]
        normals = np.array(normals, dtype=np.float32).reshape(36, 3)

        vertex_data = np.hstack((normals, vertex_data))
        vertex_data = np.hstack((tex_coord_data, vertex_data))
        return vertex_data


class TableVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(self.objects_path + '/mesa/table01.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype=np.float32)
        return vertex_data


class TroutVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(self.objects_path + '/trout/trout.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype=np.float32)
        return vertex_data


# class TeapotVBO(BaseVBO):
#     def __init__(self, ctx):
#         super().__init__(ctx)
#         self.format = '2f 3f 3f'
#         self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']
#
#     def get_vertex_data(self):
#         objs = pywavefront.Wavefront(self.objects_path + '/teapot/20900_Brown_Betty_Teapot_v1.obj', cache=True, parse=True)
#         obj = objs.materials.popitem()[1]
#         vertex_data = obj.vertices
#         vertex_data = np.array(vertex_data, dtype=np.float32)
#         return vertex_data


class TerrainVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(self.objects_path + '/terrain/terrain.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype=np.float32)
        return vertex_data


class SkullVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(self.objects_path + '/skull/12140_Skull_v3_L2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype=np.float32)
        return vertex_data


class ProjectileVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):

        vertices = [(-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1),
                    (-1, 1,-1), (-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]
        tex_coord_data = get_data(tex_coord, tex_coord_indices)

        normals = [ ( 0, 0, 1) * 6,
                    ( 1, 0, 0) * 6,
                    ( 0, 0,-1) * 6,
                    (-1, 0, 0) * 6,
                    ( 0, 1, 0) * 6,
                    ( 0,-1, 0) * 6]
        normals = np.array(normals, dtype=np.float32).reshape(36, 3)

        vertex_data = np.hstack((normals, vertex_data))
        vertex_data = np.hstack((tex_coord_data, vertex_data))
        return vertex_data
    
class CarVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attrib = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(self.objects_path + '/bugatti/bugatti.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype=np.float32)
        return vertex_data
