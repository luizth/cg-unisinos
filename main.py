import pygame as pg
import moderngl as mgl
import sys

from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene


class GraphicsEngine:
    def __init__(self, win_size=(1200, 720)) -> None:
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(True)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create an object to track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)
        # scene
        self.scene = Scene(self)

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.scene.shoot_projectile()
            elif event.type == pg.KEYDOWN and event.key == pg.K_l:
                self.camera.editMode = not self.camera.editMode
                if(self.camera.editMode):
                    self.camera.perspective_position = self.camera.position
                    self.camera.perspective_yaw = self.camera.yaw
                    self.camera.perspective_pitch = self.camera.pitch
                else:
                    self.camera.position =  self.camera.perspective_position
                    self.camera.yaw = self.camera.perspective_yaw
                    self.camera.pitch = self.camera.perspective_pitch

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))

        self.scene.render()

        # swap buffers
        pg.display.flip()

    def run(self):
        while True:
            self.get_time()
            self.check_event()
            if(len(self.scene.objects) > 4):
                self.camera.update(self.scene.objects[4])
            self.render()
            self.delta_time = self.clock.tick(60)


if __name__ == "__main__":
    app = GraphicsEngine()
    app.run()
