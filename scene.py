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

        n, s = 5, 3
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
                add(Pyramid(app, pos=(x, -s+2, z)))

    def render(self):
        [obj.render() for obj in self.objects]
