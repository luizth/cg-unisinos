from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        self.add_object(Pyramid(self.app, pos=(0, 2, 0), scale=(1, 2, 1)))
        self.add_object(Cube(self.app))
        # add(Cube(app, pos=(0, 0,-2.5), rot=(45, 0, 0), scale=(1, 2, 1)))
        # add(Cube(app, pos=(0, 0, 2.5), rot=(0, 0, 45), scale=(1, 1, 2)))

    def render(self):
        [obj.render() for obj in self.objects]
