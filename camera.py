import glm
import pygame as pg
import math


FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05

class Camera:
    editMode = False
    def __init__(self, app, position=(0, 25, 0), yaw=0, pitch=-90) -> None:
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        if self.editMode:
            return
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self, objectToFollow):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

        if self.editMode:
            self.position = objectToFollow.pos + glm.vec3(0, 1, 0)
            self.yaw = glm.atan(-objectToFollow.m_model[0][1], objectToFollow.m_model[1][1]) * 180./math.pi
            self.pitch = glm.atan(-objectToFollow.m_model[2][0], objectToFollow.m_model[2][2]) * 180./math.pi

    def move(self):
        self.velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if self.editMode:
            return
        if keys[pg.K_w]:
            self.position += self.velocity * self.forward
        if keys[pg.K_s]:
            self.position -= self.velocity * self.forward
        if keys[pg.K_a]:
            self.position -= self.velocity * self.right
        if keys[pg.K_d]:
            self.position += self.velocity * self.right
        if keys[pg.K_q]:
            self.position += self.velocity * self.up
        if keys[pg.K_e]:
            self.position -= self.velocity * self.up
        self.position = glm.vec3(self.position[0], max(15, min(80, self.position[1])), self.position[2])

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
