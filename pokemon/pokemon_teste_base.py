from requests import api, exceptions
from pokemon import *

def online():
    pokeapi = "offline"
    try:
        resposta1 = api.get("http://localhost:8000/api/v2/")
        pokeapi = "zumbi"
        if resposta1.status_code == 200 and resposta1.json()['pokemon'] == 'http://localhost:8000/api/v2/pokemon/':
            pokeapi = "online"
    except exceptions.ConnectionError as x:
        pokeapi = "offline"
    except:
        pokeapi = "zumbi"

    treinador = "offline"
    try:
        resposta2 = api.get("http://localhost:9000/hello")
        treinador = "zumbi"
        if resposta2.status_code == 200 and resposta2.text == 'Pikachu, eu escolho você!':
            treinador = "online"
    except exceptions.ConnectionError as x:
        treinador = "offline"
    except:
        treinador = "zumbi"

    if pokeapi == "online" and treinador == "online": return "online"
    if pokeapi == "offline" and treinador == "offline": return "offline"
    return "zumbi"

def verificar_online(desejado):
    z = online()
    if desejado:
        if z == "offline": raise Exception("Os servidores estão off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        if z == "zumbi": raise Exception("Os servidores aparentemente não estão ambos em funcionamento. Estes testes só devem ser executados com ambos os servidores on-line.")
        if site_treinador != "http://127.0.0.1:9000" or site_pokeapi != "http://127.0.0.1:8000": raise Exception("As URLs para as APIs estão incorretas.")
    else:
        if z == "online": raise Exception("Os servidores estão on-line. Estes testes só devem ser executados com ambos os servidores off-line.")
        if z == "zumbi": raise Exception("Há alguma coisa em execução nas portas dos servidores. Estes testes só devem ser executados com ambos os servidores off-line.")

def verificar_erro(interno, tipo_erro):
    try:
        interno()
    except Exception as x:
        assert type(x) is tipo_erro
    else:
        assert False

def pokemon_nao_existe(interno):
    verificar_erro(interno, PokemonNaoExisteException)

def pokemon_nao_cadastrado(interno):
    verificar_erro(interno, PokemonNaoCadastradoException)

def treinador_nao_cadastrado(interno):
    verificar_erro(interno, TreinadorNaoCadastradoException)

def pokemon_ja_cadastrado(interno):
    verificar_erro(interno, PokemonJaCadastradoException)

def valor_errado(interno):
    verificar_erro(interno, ValueError)

nao_existe = ["DOBBY", "Peppa-Pig", "batman", "SpiderMan"]

def assert_equals_unordered_list(esperada, obtida):
    assert len(esperada) == len(obtida)
    for item in esperada:
        assert item in obtida

class NoStdIO:
    def __init__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        self.__usou_print = False
        self.__usou_input = False

    def __enter__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        sys.stdout = self
        sys.stdin = self

    def __exit__(self, a, b, c):
        import sys
        sys.stdout = self.__oout
        sys.stdin = self.__oin

    def write(self, str):
        self.__usou_print = True
        return self.__oout.write(str)

    def readline(self):
        self.__usou_input = True
        return self.__oin.readline()

    def flush(self):
        pass

    @property
    def usou_print(self):
        return self.__usou_print

    @property
    def usou_input(self):
        return self.__usou_input

    def __call__(self, delegate):
        from functools import wraps
        @wraps(delegate)
        def sem_input(*args, **kwargs):
            with self:
                return delegate(*args, **kwargs)
        return sem_input

sem_io = NoStdIO()