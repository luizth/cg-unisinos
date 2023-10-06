#version 330 core


layout (location = 1) in vec3 in_position;

out vec2 uv_0;

uniform mat4 m_proj;
uniform mat4 m_view;


void main() {

    gl_Position = m_proj * m_view * vec4(in_position, 1.0);
}
