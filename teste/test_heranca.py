from codigo.heranca import *

def test_professor_completo():
    professor01 = Professor()
    professor01.set_nome("Samuel")
    professor01.set_cpf(11055233242)
    professor01.set_titulacao("Doutorado")

    assert professor01.get_nome() == "Carlos"
    assert professor01.get_cpf() == 11055233242
    assert professor01.get_titulacao() == "Doutorado"

def test_aluno_ensino_medio_aprovado():

    aluno01 = AlunoEnsinoMedio()
    aluno01.set_nome("Eduardo")
    aluno01.set_matricula(110491278)

    media = aluno01.calcular_media(6.0, 8.0)

    assert media == 7.0
    assert aluno01.aprovacao() is True

def test_aluno_ensino_graduacao_aprovado():
    aluno02 = AlunoGraduacao()
    aluno02.set_nome("Eduardo")
    aluno02.set_matricula(110491278)
    media = aluno02.calcular_media(7.0, 8.0)
    assert media == 7.5
    assert aluno02.aprovacao() is True

def test_aluno_ensino_medio_reprovado():
    aluno03 = AlunoEnsinoMedio()
    aluno03.set_nome("Bruno")
    aluno03.set_matricula(110491278)
    media = aluno03.calcular_media(2.0, 2.0)
    assert media == 2.0
    assert aluno03.aprovacao() is False

def test_aluno_ensino_graduacao_reprovado():
    aluno04 = AlunoGraduacao()
    aluno04.set_nome("Thiago")
    aluno04.set_matricula(110491278)
    media = aluno04.calcular_media(4.0, 4.0)
    assert media == 4.0
    assert aluno04.aprovacao() is False

# testes dos alunos de ensino medio e graduacao para ver se sao aprovados ou reprovados (acima)

def test_exibir_dados_professor():
    professor02 = Professor()
    professor02.set_nome("Marco")
    professor02.set_titulacao("Goat")
    resultado = professor02.exibir_dados()
    assert resultado == "Nome: Marco, Titulação: Goat"