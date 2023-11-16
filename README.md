# cg-unisinos
Repositório de projetos da disciplina de Computação Gráfica em Tempo-Real da Unisinos.


### Instalando as dependências

```bash
$ pip install -r requirements.txt
```

- **pygame**: biblioteca responsável pelo gerenciamento de janelas e capturar eventos do teclado e mouse.
- **moderngl**: biblioteca wrapper do OpenGL (C++) para Python. simplifica a API para gerenciamento de contexto e máquina de estados do OpenGL.
- **glm**: biblioteca matemática para operações com vetores e matrizes compatíveis com a API do OpenGL.
- **pywaveform**: leitor de arquivos .obj.


### Executando o programa

```bash
$ python main.py
```

#### Controles
- **WASD**: move a camera para frente (↑), para esquerda (←), para trás (↓) e para direita (→)
- **QE**: move a camera para cima (↑) e para baixo (↓)
- **SPACE**: dispara projétil


### Overview dos diretórios e módulos do projeto

Diretórios:
- **objects**: arquivos .obj que podem ser carregados no módulo `vbo.py`
- **shaders**: vertex shaders e fragment shaders para renderizar os objetos que podem ser carregados no módulo `shader_program.py`
- **textures**: imagens .png ou .jpg que podem ser carregadas no módulo `texture.py`


Módulos:
- **camera**: gerenciamento da rotação e movimentação da camera em primeira pessoa.
- **main**: gerenciamento do loop principal da aplicação: criação do contexto OpenGL, instancia a cena, chamada do método render, controle da passagem do tempo, etc.
- **mesh**: módulo para facilitar o acesso as texturas e VBOs em outros módulos da aplicação.
- **model**: gerenciamento dos modelos e objetos 3D. vinculamos a textura e escrevemos a matrix de modelo e de view no programa de Shader.
- **scene**: gerenciamento da cena e dos objetos renderizados.
- **shader_program**: leitura e carregamento de programas de Shader na aplicação.
- **texture**: leitura de arquivos de textura. aplica filtros e mipmap nas texturas.
- **vao**: gerenciamento de objetos de Vertex Array (VAOs), que definem como os vertices e os dados serão passados para a GPU. associa VBOs aos programas de Shader.
- **vbo**: gerenciamento de objetos de Vertex Buffer (VBOs). define os vertices e coordenadas de textura, além dos atributos que serão passados para os programas de Shader.


### Features

**TODO**:
- Implementar .OBJ parser próprio e substituir `pywaveform`
- Implementar bounding box para os modelos
