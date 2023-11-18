from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        self.vaos['pyramid'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['pyramid'])
        self.vaos['cube'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['cube'])

        self.vaos['table'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['table'])
        self.vaos['trout'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['trout'])
        # self.vaos['teapot'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['teapot'])
        self.vaos['terrain'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['terrain'])
        self.vaos['skull'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['skull'])
        self.vaos['projectile'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['projectile'])
        self.vaos['car'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['car'])


    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attrib)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
