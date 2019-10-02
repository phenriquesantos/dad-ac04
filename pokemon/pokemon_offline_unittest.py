import unittest
from pokemon_teste_base import *

verificar_online(False)

nao_int = ["", "a", "5", "2-3", "+", " ", 5.6, [], {"a": "b"}, "pikachu"]
nao_str =  [1, 2, [], {"a": "b"}, ""]

class TestOffline(unittest.TestCase):
    @sem_io
    def test_01x_nao_existe(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(0))
        pokemon_nao_existe(lambda : nome_do_pokemon(-1))
        pokemon_nao_existe(lambda : nome_do_pokemon(-2))
        pokemon_nao_existe(lambda : nome_do_pokemon(-666))
        pokemon_nao_existe(lambda : nome_do_pokemon(808))
        pokemon_nao_existe(lambda : nome_do_pokemon(999))
        pokemon_nao_existe(lambda : nome_do_pokemon(1234))

    @sem_io
    def test_01y_nao_existe_pegadinha(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(10001))

    @sem_io
    def test_01z_erro_tipo(self):
        for ne in nao_int:
            valor_errado(lambda : nome_do_pokemon(ne))

    @sem_io
    def test_02z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : numero_do_pokemon(ne))

    @sem_io
    def test_03z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : color_of_pokemon(ne))

    @sem_io
    def test_04z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : cor_do_pokemon(ne))

    @sem_io
    def test_05z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : tipos_do_pokemon(ne))

    @sem_io
    def test_06z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : evolucao_anterior(ne))

    @sem_io
    def test_07z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : evolucoes_proximas(ne))

    @sem_io
    def test_08x_erro_tipo_1(self):
        for ne in nao_str:
            valor_errado(lambda : nivel_do_pokemon(ne, 1234))

    @sem_io
    def test_08y_erro_tipo_2(self):
        for ne in nao_int:
            valor_errado(lambda : nivel_do_pokemon("pikachu", ne))

    @sem_io
    def test_08z_negativo(self):
        for i in [-1, -2, -666]:
            valor_errado(lambda : nivel_do_pokemon("pikachu", i))

    @sem_io
    def test_09z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : cadastrar_treinador(ne))

    @sem_io
    def test_10v_erro_tipo_treinador(self):
        for ne in nao_str:
            valor_errado(lambda : cadastrar_pokemon(ne, "Chapolin", "makuhita", 5000))

    @sem_io
    def test_10w_erro_tipo_apelido(self):
        for ne in nao_str:
            valor_errado(lambda : cadastrar_pokemon("Seu Madruga", ne, "elekid", 5000))

    @sem_io
    def test_10x_erro_tipo_especie(self):
        for ne in nao_str:
            valor_errado(lambda : cadastrar_pokemon("Chiquinha", "Nhonho", ne, 5000))

    @sem_io
    def test_10y_erro_tipo_experiencia(self):
        for ne in nao_int:
            valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", ne))

    @sem_io
    def test_10z_experiencia_negativa(self):
        for i in [-1, -2, -666]:
            valor_errado(lambda : cadastrar_pokemon("Jaiminho", "Seu Barriga", "snorlax", i))

    @sem_io
    def test_11w_erro_tipo_treinador(self):
        for ne in nao_str:
            valor_errado(lambda : ganhar_experiencia(ne, "Dona Florinda", 5000))

    @sem_io
    def test_11x_erro_tipo_pokemon(self):
        for ne in nao_str:
            valor_errado(lambda : ganhar_experiencia("Girafales", ne, 5000))

    @sem_io
    def test_11y_erro_tipo_experiencia(self):
        for ne in nao_int:
            valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", ne))

    @sem_io
    def test_11z_erro_experiencia_negativa(self):
        for ne in [-1, -2, -666]:
            valor_errado(lambda : ganhar_experiencia("Dona Florinda", "Quico", ne))

    @sem_io
    def test_12y_erro_tipo_nome(self):
        for ne in nao_str:
            valor_errado(lambda : localizar_pokemon(ne, "Goku"))

    @sem_io
    def test_12z_erro_tipo_apelido(self):
        for ne in nao_str:
            valor_errado(lambda : localizar_pokemon("Vegeta", ne))

    @sem_io
    def test_13z_erro_tipo(self):
        for ne in nao_str:
            valor_errado(lambda : detalhar_treinador(ne))

    @sem_io
    def test_99a_print(self):
        assert not sem_io.usou_print, "Você não deveria utilizar a função print neste exercício."

    @sem_io
    def test_99b_input(self):
        assert not sem_io.usou_input, "Você não deveria utilizar a função input neste exercício."

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestOffline)
    unittest.TextTestRunner(verbosity = 2,failfast = True).run(suite)

if __name__ == '__main__':
    runTests()
