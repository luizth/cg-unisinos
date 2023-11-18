import glm


class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.shader_program = self.vao.program
        self.camera = self.app.camera

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


class Table(BaseModel):
    def __init__(self, app, vao_name='table', tex_id='table', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
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
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)

        self.m_model = glm.rotate(self.m_model, self.app.time * 0.002, glm.vec3(0, 0, -1))
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


class Projectile(BaseModel):
    def __init__(self, app, vao_name='projectile', tex_id=2, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.speed = 0.8
        self.on_init()

    def update(self):
        self.texture.use()
        # self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_view'].write(self.camera.m_view)

        # update pos based on camera forward vector
        self.m_model = glm.translate(self.m_model, self.camera.forward * self.speed)
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
