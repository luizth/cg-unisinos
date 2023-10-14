from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        # load locally for better performance
        app = self.app
        add = self.add_object

        add(Terrain(app, pos=(0, 0, 0)))
        add(Table(app, pos=(0, 0, 0), scale=(0.5, 0.5, 0.5)))
        add(Cube(app, pos=(-1.4, 5.3, -1.2), rot=(0, -26, 0), scale=(0.8, 0.8, 0.8)))
        add(Cube(app, pos=(0.26, 5.05, -1.2), rot=(0, -38, 0), scale=(0.55, 0.55, 0.55)))
        add(Trout(app, pos=(-2.2, 6.1, 0), rot=(-90, 0, 46), scale=(0.4, 0.4, 0.4)))
        add(Skull(app, pos=(1.3, 4.5, 0.8), rot=(-90, 0, -45), scale=(0.05, 0.05, 0.05)))

    def shoot_projectile(self):
        self.add_object(Projectile(self.app, pos=self.app.camera.position, rot=self.app.camera.forward))

    def render(self):
        [obj.render() for obj in self.objects]
