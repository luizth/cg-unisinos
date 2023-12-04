import glm
import math

class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.vao_name = vao_name
        self.shader_program = self.vao.program
        self.camera = self.app.camera

    def get_minX(self):
        self.minX= self.pos[0] - self.scale[0]/2
        return self.minX
    def get_maxX(self):
        self.maxX = self.pos[0] + self.scale[0]/2
        return self.maxX
    def get_minY(self):
        self.minY = self.pos[1] - self.scale[1]/2
        return self.minY
    def get_maxY(self):
        self.maxY = self.pos[1] + self.scale[1]/2
        return self.maxY
    def get_minZ(self):
        self.minZ = self.pos[2] - self.scale[2]/2
        return self.minZ
    def get_maxZ(self):
        self.maxZ = self.pos[2] + self.scale[2]/2
        return self.maxZ


    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()

    def destroy(self):
        print("destroyed")


class Pista(BaseModel):
    def __init__(self, app, vao_name='pista', tex_id='road', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Pyramid(BaseModel):
    def __init__(self, app, vao_name='pyramid', tex_id=1, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # light
        self.shader_program['light.position'].write(self.app.light.position)
        self.shader_program['light.Ia'].write(self.app.light.Ia)
        self.shader_program['light.Id'].write(self.app.light.Id)
        self.shader_program['light.Is'].write(self.app.light.Is)

        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Table(BaseModel):
    def __init__(self, app, vao_name='table', tex_id='table', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Trout(BaseModel):
    def __init__(self, app, vao_name='trout', tex_id='trout', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Teapot(BaseModel):
    def __init__(self, app, vao_name='teapot', tex_id='teapot', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Terrain(BaseModel):
    def __init__(self, app, vao_name='terrain', tex_id='terrain', pos=(0, 0, 0), rot=(0, 0, 0), scale=(5, 1, 5)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Skull(BaseModel):
    def __init__(self, app, vao_name='skull', tex_id='skull', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)

        self.pos = glm.vec3(self.m_model[3][0], self.m_model[3][1], self.m_model[3][2])
        self.m_model = glm.translate(self.m_model, glm.vec3(1,1,1) * 0.2)
        self.m_model = glm.rotate(self.m_model, 0.02, glm.vec3(0, 0, -1))
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # light
        self.shader_program['light.position'].write(self.app.light.position)
        self.shader_program['light.Ia'].write(self.app.light.Ia)
        self.shader_program['light.Id'].write(self.app.light.Id)
        self.shader_program['light.Is'].write(self.app.light.Is)
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)


class Projectile(BaseModel):
    def __init__(self, app, objectToFollow, vao_name='projectile', tex_id=2,
    pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1), speed = 0.3):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        self.objectToFollow = objectToFollow
        self.speed = speed

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.pos = glm.vec3(self.m_model[3][0], self.m_model[3][1], self.m_model[3][2])

        self.translationVector = (self.objectToFollow.pos - self.pos)
        self.distance = math.sqrt((self.translationVector[0])*(self.translationVector[0])
            + (self.translationVector[1])*(self.translationVector[1])
            + (self.translationVector[2])*(self.translationVector[2]))
        #print("Distance:", self.distance)

        if self.isColliding():
            print("COLLIDE")
            self.app.scene.targetDestroyed = True
            self.app.scene.objects.remove(self.objectToFollow)
            self.app.scene.objects.remove(self)
        else:
            self.m_model = glm.translate(self.m_model, self.translationVector * 1./self.distance * self.speed)
        self.shader_program['m_model'].write(self.m_model)

    def isColliding(self):
        x_in = False
        y_in = False
        z_in = False

        if self.get_minX() >= self.objectToFollow.get_minX():
            if self.get_minX() <= self.objectToFollow.get_maxX():
                x_in = True
                #print("x in")
        if self.get_maxX() >= self.objectToFollow.get_minX():
            if self.get_maxX() <= self.objectToFollow.get_maxX():
                x_in = True
                #print("x in")
        if self.get_minX() <= self.objectToFollow.get_minX():
            if self.get_maxX() >= self.objectToFollow.get_maxX():
                x_in = True
                #print("x in")

        if self.get_minY() >= self.objectToFollow.get_minY():
            if self.get_minY() <= self.objectToFollow.get_maxY():
                y_in = True
                #print("y in")
        if self.get_maxY() >= self.objectToFollow.get_minY():
            if self.get_maxY() <= self.objectToFollow.get_maxY():
                y_in = True
                #print("y in")
        if self.get_minY() <= self.objectToFollow.get_minY():
            if self.get_maxY() >= self.objectToFollow.get_maxY():
                y_in = True
                #print("y in")

        if self.get_minZ() >= self.objectToFollow.get_minZ():
            if self.get_minZ() <= self.objectToFollow.get_maxZ():
                z_in = True
                #print("z in")
        if self.get_maxZ() >= self.objectToFollow.get_minZ():
            if self.get_maxZ() <= self.objectToFollow.get_maxZ():
                z_in = True
                #print("z in")
        if self.get_minZ() <= self.objectToFollow.get_minZ():
            if self.get_maxZ() >= self.objectToFollow.get_maxZ():
                z_in = True
                #print("z in")

        return (x_in and y_in and z_in)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

class Car(BaseModel):
    def __init__(self, app, vao_name='car', tex_id='car', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        #self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)

        self.m_model = glm.rotate(self.m_model, self.app.time * 0.002, glm.vec3(0, 0, -1))
        self.shader_program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.shader_program['u_texture_0'] = 0
        #self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
