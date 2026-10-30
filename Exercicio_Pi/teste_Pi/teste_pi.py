from Exercicio_Pi.exercicio_pi.exercicio_pi import *

def test_deve_retornar_nome_escolaridade_professor():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Doutorado")
    professor = Professor()
    professor.set_escolaridade(escolaridade)
    assert professor.get_nome_escolaridade() == "Doutorado"

def test_deve_retornar_pessoa_sem_escolaridade():
    professor = Professor()
    assert professor.get_nome_escolaridade() == "Pessoa sem escolaridade"
# LETRA A ACIMA

def test_escolaridade_coordenador_curso():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Mestrado")
    coordenador = Professor()
    coordenador.set_escolaridade(escolaridade)
    curso = Curso()
    curso.set_coordenador(coordenador)
    assert curso.get_coordenador().get_nome_escolaridade() == "Mestrado"

def test_sem_escolaridade_coordenador_curso():
    curso = Curso()
    assert curso.get_nome_escolaridade_coordenador() == 'Coordenador sem escolaridade'

# LETRA B ACIMA

def test_escolaridade_diretor_escola():
    escolaridade = Escolaridade()
    escolaridade.set_nome("Mestrado")
    diretor = Professor()
    diretor.set_escolaridade(escolaridade)
    escola = Escola()
    escola.set_diretor(diretor)
    assert escola.get_diretor().get_nome_escolaridade() == "Mestrado"

def test_sem_escolaridade_diretor_escola():
    escola = Escola()
    assert escola.get_escolaridade_diretor() == "Diretor sem escolaridade"

# LETRA C ACIMA

def test_deve_retornar_nome_estado_naturalidade_aluno():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    aluno = Aluno()
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "RJ"

def test_deve_retornar_aluno_sem_estado_naturalidade():
    aluno = Aluno()
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem estado naturalidade"

# LETRA D ACIMA

def test_cidade_nascimento_professor():
    cidade_natal = Cidade()
    cidade_natal.set_cidade("SP")
    professor = Professor()
    professor.set_naturalidade(cidade_natal)
    assert professor.get_naturalidade().get_cidade() == "SP"

def test_sem_cidade_nascimento_professor():
    cidade = Cidade()
    assert cidade.get_nome_estado() == "Cidade sem estado"

# LETRA E ACIMA

def test_deve_retornar_nome_estado_cidade():
    estado = Estado()
    estado.set_nome("RJ")
    cidade = Cidade()
    cidade.set_estado(estado)
    assert cidade.get_nome_estado() == "RJ"

def test_deve_retornar_cidade_sem_estado():
    cidade = Cidade()
    assert cidade.get_nome_estado() == "Cidade sem estado"

# LETRA F ACIMA

def test_professor_com_tipo_ensino():
    tipo_ensino = TipoEnsino()
    tipo_ensino.set_nome("Ensino Médio")
    curso = Curso()
    curso.set_tipo_ensino(tipo_ensino)
    professor = Professor()
    professor.set_curso_contratacao(curso)
    assert professor.get_nome_tipo_ensino() == "Ensino Médio"

def test_sem_tipo_ensino_professor_contratacao():
    professor = Professor()
    assert professor.get_nome_tipo_ensino() == "Professor sem tipo de ensino"

# LETRA G ACIMA

def test_deve_retornar_curso_sem_coordenador():
    curso = Curso()
    assert curso.get_nome_coordenador() == "Curso sem coordenador"

def test_deve_retornar_nome_coordenador_curso():
    coordenador = Professor()
    coordenador.set_nome("Marco")
    curso = Curso()
    curso.set_coordenador(coordenador)
    assert curso.get_nome_coordenador() == "Marco"

#LETRA H ACIMA

def test_diretor_professor():
    diretor = Professor()
    diretor.set_nome("Carlos")
    escola = Escola()
    escola.set_diretor(diretor)
    professor = Professor()
    professor.set_escola(escola)
    assert professor.get_nome_diretor_escola() == "Carlos"

def test_sem_escola_diretor_professor():
    professor = Professor()
    assert professor.get_nome_diretor_escola() == "Professor sem escola"

def test_sem_diretor():
    escola = Escola()
    professor = Professor()
    professor.set_escola(escola)
    assert professor.get_nome_diretor_escola() == "Escola sem diretor"

# LETRA I ACIMA


def test_deve_retornar_professor_sem_curso():
    professor = Professor()
    assert professor.get_nome_coordenador() == "Professor sem curso"

def test_deve_retornar_nome_coordenador_professor():
    coordenador = Professor()
    coordenador.set_nome("Marco")
    curso = Curso()
    curso.set_coordenador(coordenador)
    professor = Professor()
    professor.set_curso(curso)
    assert professor.get_nome_coordenador() == "Marco"

# LETRA J ACIMA
