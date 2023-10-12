# cg-unisinos
Repositório de projetos da disciplina de Computação Gráfica em Tempo-Real da Unisinos.


### Instalando as dependências

```bash
$ pip install -r requirements.txt
```


### Executando o programa

```bash
$ python main.py
```

#### Comandos
- **WASD**: move a camera para frente (↑), para esquerda (←), para trás (↓) e para direita (→)
- *QE*: move a camera para cima (↑) e para baixo (↓)



### Overview dos diretórios e módulos do projeto

Diretórios:
- **objects**: arquivos .obj que podem ser carregados no módulo `model.py`
- **shaders**: vertex shaders e fragment shaders para renderizar os objetos que podem ser carregados no módulo `shader_program.py`
- **textures**: imagens .png ou .jpg que podem ser carregadas no módulo `texture.py`


Módulos (`TODO`):
- **camera**
- **main**
- **mesh**
- **model**
- **scene**
- **shader_program**
- **texture**
- **vao**
- **vbo**
