import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures[1] = self.get_texture(path='textures/triangle.png')
        self.textures[2] = self.get_texture(path='textures/img_1.png')
        self.textures['table'] = self.get_texture(path='objects/mesa/table01.bmp')
        self.textures['trout'] = self.get_texture(path='objects/trout/trout03-3a-wav1.jpg')
        # self.textures['teapot'] = self.get_texture(path='objects/teapot/Blank.mtl')
        self.textures['terrain'] = self.get_texture(path='textures/terrain_01.png')
        self.textures['skull'] = self.get_texture(path='objects/skull/Skull.jpg')

    def get_texture(self, path, flip_x=False, flip_y=True):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=flip_x, flip_y=flip_y)
        texture = self.ctx.texture(size=texture.get_size(), components=3, data=pg.image.tostring(texture, 'RGB'))
        # mipmap
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture. build_mipmaps()
        # AF
        texture.ansiotropic_filter = 32.0
        return texture

    def destroy(self):
        [texture.release() for texture in self.textures.values()]
