from requests import api
from pokemon_teste_base import *

verificar_online(True)

def reset():
    resposta = api.post(f"{site_treinador}/reset")
    assert resposta.status_code == 200

@sem_io
def test_01a_ok():
    assert nome_do_pokemon(1) == "bulbasaur"
    assert nome_do_pokemon(55) == "golduck"
    assert nome_do_pokemon(25) == "pikachu"
    assert nome_do_pokemon(700) == "sylveon"
    assert nome_do_pokemon(807) == "zeraora"

@sem_io
def test_02a_ok():
    assert numero_do_pokemon("EEVEE") == 133
    assert numero_do_pokemon("Psyduck") == 54
    assert numero_do_pokemon("marill") == 183
    assert numero_do_pokemon("SkiTtY") == 300
    assert numero_do_pokemon("Zeraora") == 807

@sem_io
def test_02b_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : numero_do_pokemon(ne))

@sem_io
def test_03a_ok():
    assert color_of_pokemon("EEVEE") == "brown"
    assert color_of_pokemon("Psyduck") == "yellow"
    assert color_of_pokemon("marill") == "blue"
    assert color_of_pokemon("SkiTtY") == "pink"
    assert color_of_pokemon("magneton") == "gray"
    assert color_of_pokemon("GASTLY") == "purple"
    assert color_of_pokemon("LeDyBa") == "red"
    assert color_of_pokemon("togekiss") == "white"
    assert color_of_pokemon("Torterra") == "green"
    assert color_of_pokemon("xurkiTree") == "black"

@sem_io
def test_03b_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : color_of_pokemon(ne))

@sem_io
def test_04a_ok():
    assert cor_do_pokemon("EEVEE") == "marrom"
    assert cor_do_pokemon("Psyduck") == "amarelo"
    assert cor_do_pokemon("marill") == "azul"
    assert cor_do_pokemon("SkiTtY") == "rosa"
    assert cor_do_pokemon("magneton") == "cinza"
    assert cor_do_pokemon("GASTLY") == "roxo"
    assert cor_do_pokemon("LeDyBa") == "vermelho"
    assert cor_do_pokemon("togekiss") == "branco"
    assert cor_do_pokemon("Torterra") == "verde"
    assert cor_do_pokemon("xurkiTree") == "preto"

@sem_io
def test_04b_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : cor_do_pokemon(ne))

@sem_io
def test_05a_ok():
    assert_equals_unordered_list(["voador", "noturno"], tipos_do_pokemon("murKrow"))
    assert_equals_unordered_list(["água", "elétrico"], tipos_do_pokemon("cHinChou"))
    assert_equals_unordered_list(["terra"], tipos_do_pokemon("hippowdon"))
    assert_equals_unordered_list(["pedra", "voador"], tipos_do_pokemon("archeops"))
    assert_equals_unordered_list(["lutador", "fantasma"], tipos_do_pokemon("MARSHADOW"))
    assert_equals_unordered_list(["grama"], tipos_do_pokemon("chikorita"))
    assert_equals_unordered_list(["normal", "fada"], tipos_do_pokemon("jigglypuff"))
    assert_equals_unordered_list(["aço"], tipos_do_pokemon("KLINK"))
    assert_equals_unordered_list(["lutador", "inseto"], tipos_do_pokemon("Heracross"))
    assert_equals_unordered_list(["veneno", "noturno"], tipos_do_pokemon("DRAPION"))
    assert_equals_unordered_list(["fogo"], tipos_do_pokemon("darumaka"))
    assert_equals_unordered_list(["psíquico", "gelo"], tipos_do_pokemon("JYNX"))
    assert_equals_unordered_list(["dragão"], tipos_do_pokemon("dRaTiNi"))

@sem_io
def test_05b_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : tipos_do_pokemon(ne))

@sem_io
def test_06a_ok():
    assert evolucao_anterior("togetic") == "togepi"
    assert evolucao_anterior("togeKiss") == "togetic"
    assert evolucao_anterior("EEleKtriK") == "tynamo"
    assert evolucao_anterior("EELEKTROSS") == "eelektrik"
    assert evolucao_anterior("Pikachu") == "pichu"
    assert evolucao_anterior("rAiChu") == "pikachu"

@sem_io
def test_06b_nao_tem():
    assert evolucao_anterior("togepi") == None
    assert evolucao_anterior("TYNAMO") == None
    assert evolucao_anterior("Pichu") == None

@sem_io
def test_06c_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : evolucao_anterior(ne))

@sem_io
def test_07a_ok_evolucoes_simples():
    assert_equals_unordered_list(["charmeleon"], evolucoes_proximas("charmander"))
    assert_equals_unordered_list(["charizard"], evolucoes_proximas("ChArMeLeON"))
    assert_equals_unordered_list(["combusken"], evolucoes_proximas("torchic"))

@sem_io
def test_07b_ok_nao_tem_simples():
    assert_equals_unordered_list([], evolucoes_proximas("CHARIZARD"))
    assert_equals_unordered_list([], evolucoes_proximas("gEnGar"))
    assert_equals_unordered_list([], evolucoes_proximas("ALAkazam"))
    assert_equals_unordered_list([], evolucoes_proximas("turtonator"))
    assert_equals_unordered_list([], evolucoes_proximas("lugia"))

@sem_io
def test_07c_ok_evolucoes_complexas():
    assert_equals_unordered_list(["poliwhirl"], evolucoes_proximas("Poliwag"))
    assert_equals_unordered_list(["gloom"], evolucoes_proximas("oDDiSH"))
    assert_equals_unordered_list(["poliwrath", "politoed"], evolucoes_proximas("PoliWHIRL"))
    assert_equals_unordered_list(["vileplume", "bellossom"], evolucoes_proximas("GLOOM"))
    assert_equals_unordered_list(["ninjask", "shedinja"], evolucoes_proximas("nincada"))
    assert_equals_unordered_list(["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"], evolucoes_proximas("eevee"))
    assert_equals_unordered_list(["hitmonlee", "hitmonchan", "hitmontop"], evolucoes_proximas("tyrogue"))

@sem_io
def test_07d_ok_nao_tem_complexas():
    assert_equals_unordered_list([], evolucoes_proximas("espeon"))
    assert_equals_unordered_list([], evolucoes_proximas("leafeon"))
    assert_equals_unordered_list([], evolucoes_proximas("politoed"))
    assert_equals_unordered_list([], evolucoes_proximas("lugia"))

@sem_io
def test_07e_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : evolucoes_proximas(ne))

@sem_io
def test_08a_simples():
    nivel_do_pokemon("Magikarp",       900) ==  8 # 1
    nivel_do_pokemon("Magikarp",   1000000) == 92 # 1
    nivel_do_pokemon("SLOWBRO",      65000) == 40 # 2
    nivel_do_pokemon("OcTiLLeRy",   280000) == 65 # 2
    nivel_do_pokemon("blastoise",   110000) == 49 # 4
    nivel_do_pokemon("mewtwo",     1000000) == 92 # 1
    nivel_do_pokemon("FRAXURE",     280000) == 60 # 1
    nivel_do_pokemon("lunatone",     20000) == 29 # 3
    nivel_do_pokemon("skitty",       50000) == 39 # 3
    nivel_do_pokemon("torchic",      40000) == 36 # 4
    nivel_do_pokemon("ODDISH",        5000) == 20 # 4

@sem_io
def test_08b_complexos():
    nivel_do_pokemon("zangoose",      9000) == 17 # 5
    nivel_do_pokemon("milotic",      65000) == 37 # 5
    nivel_do_pokemon("Lumineon",    160000) == 55 # 5
    nivel_do_pokemon("NINJASK",     300000) == 72 # 5
    nivel_do_pokemon("zangoose",    580000) == 97 # 5
    nivel_do_pokemon("makuhita",       600) == 10 # 6
    nivel_do_pokemon("gulpin",        7000) == 20 # 6
    nivel_do_pokemon("seviper",     150000) == 50 # 6
    nivel_do_pokemon("drifblim",   1000000) == 87 # 6

@sem_io
def test_08c_limites():
    nivel_do_pokemon("pinsir",           0) ==   1 # 1
    nivel_do_pokemon("bibarel",          0) ==   1 # 2
    nivel_do_pokemon("aipom",            0) ==   1 # 3
    nivel_do_pokemon("Makuhita",         0) ==   1 # 6
    nivel_do_pokemon("Magikarp",      1249) ==   9 # 1
    nivel_do_pokemon("MeTaPoD",        999) ==   9 # 2
    nivel_do_pokemon("Magikarp",      1250) ==  10 # 1
    nivel_do_pokemon("Butterfree",    1000) ==  10 # 2
    nivel_do_pokemon("charmeleon",   29948) ==  32 # 4
    nivel_do_pokemon("charmeleon",   29949) ==  33 # 4
    nivel_do_pokemon("hariyama",     71676) ==  40 # 6
    nivel_do_pokemon("hariyama",     71677) ==  41 # 6
    nivel_do_pokemon("togePI",      799999) ==  99 # 3
    nivel_do_pokemon("gengar",     1059859) ==  99 # 4
    nivel_do_pokemon("zangoose",    599999) ==  99 # 5
    nivel_do_pokemon("SWALot",     1639999) ==  99 # 6
    nivel_do_pokemon("sYLVEON",    1000000) == 100 # 2
    nivel_do_pokemon("Jigglypuff", 1000000) == 100 # 3
    nivel_do_pokemon("LEDIAN",      800000) == 100 # 3
    nivel_do_pokemon("vaPorEON", 999999999) == 100 # 2
    nivel_do_pokemon("VILEPLUME",  1059860) == 100 # 4
    nivel_do_pokemon("zangoose",    600000) == 100 # 5
    nivel_do_pokemon("SWALOT",     1640000) == 100 # 6

@sem_io
def test_08d_nao_existe():
    for ne in nao_existe:
        pokemon_nao_existe(lambda : nivel_do_pokemon(ne, 1234))

@sem_io
def test_09a_ok():
    reset()

    treinador_nao_cadastrado(lambda : detalhar_treinador("Ash Ketchum"))
    assert cadastrar_treinador("Ash Ketchum")
    assert detalhar_treinador("Ash Ketchum") == {}

    treinador_nao_cadastrado(lambda : detalhar_treinador("Misty"))
    assert cadastrar_treinador("Misty")
    assert detalhar_treinador("Misty") == {}

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
        "Misty": {"nome": "Misty", "pokemons": {}}
    }

@sem_io
def test_09b_limpeza():
    reset()
    assert cadastrar_treinador("Jessie")
    assert cadastrar_treinador("James")
    reset()
    treinador_nao_cadastrado(lambda : detalhar_treinador("Jessie"))
    treinador_nao_cadastrado(lambda : detalhar_treinador("James"))

@sem_io
def test_09c_repetido():
    reset()
    assert cadastrar_treinador("Jessie")
    assert not cadastrar_treinador("Jessie")
    assert detalhar_treinador("Jessie") == {}
    cadastrar_pokemon("Jessie", "A", "ARBOK", 20000)
    cadastrar_pokemon("Jessie", "B", "wobbuffet", 2000)
    cadastrar_pokemon("Jessie", "C", "Lickitung", 2500)
    assert not cadastrar_treinador("Jessie")

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Jessie": {
            "nome": "Jessie",
            "pokemons": {
                "A": {"apelido": "A", "tipo": "arbok", "experiencia": 20000},
                "B": {"apelido": "B", "tipo": "wobbuffet", "experiencia": 2000},
                "C": {"apelido": "C", "tipo": "lickitung", "experiencia": 2500}
            }
        }
    }

@sem_io
def test_10a_ok():
    reset()

    assert cadastrar_treinador("Ash Ketchum")
    cadastrar_pokemon("Ash Ketchum", "P", "Pikachu", 50000)
    assert cadastrar_treinador("Misty")
    cadastrar_pokemon("Misty", "A", "STARYU", 10000)
    cadastrar_pokemon("Misty", "B", "sTaRyU", 12000)
    assert cadastrar_treinador("Brock")
    cadastrar_pokemon("Brock", "O", "onix", 8000)
    cadastrar_pokemon("Brock", "G", "Geodude", 20000)
    assert cadastrar_treinador("James")
    cadastrar_pokemon("James", "A", "KOFFING", 5000)
    cadastrar_pokemon("James", "B", "MeowTH", 20000)

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 50000}}},
        "Misty": {"nome": "Misty", "pokemons": {"A": {"apelido": "A", "tipo": "staryu", "experiencia": 10000}, "B": {"apelido": "B", "tipo": "staryu", "experiencia": 12000}}},
        "Brock": {"nome": "Brock", "pokemons": {"O": {"apelido": "O", "tipo": "onix", "experiencia": 8000}, "G": {"apelido": "G", "tipo": "geodude", "experiencia": 20000}}},
        "James": {
            "nome": "James",
            "pokemons": {
                "A": {"apelido": "A", "tipo": "koffing", "experiencia": 5000},
                "B": {"apelido": "B", "tipo": "meowth", "experiencia": 20000}
            }
        }
    }

@sem_io
def test_10b_treinador_nao_existe():
    reset()
    treinador_nao_cadastrado(lambda : cadastrar_pokemon("Max", "D", "lapras", 40000))
    assert api.get(f"{site_treinador}/treinador").json() == {}

@sem_io
def test_10c_pokemon_nao_existe():
    reset()
    assert cadastrar_treinador("Iris")
    pokemon_nao_existe(lambda : cadastrar_pokemon("Iris", "D", "homer", 40000))
    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Iris": {"nome": "Iris", "pokemons": {}}
    }

@sem_io
def test_10d_pokemon_ja_existe():
    reset()
    assert cadastrar_treinador("Misty")
    cadastrar_pokemon("Misty", "estrela", "STARMIE", 40000)
    pokemon_ja_cadastrado(lambda : cadastrar_pokemon("Misty", "estrela", "staryu", 1000))

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Misty": {"nome": "Misty", "pokemons": {"estrela": {"apelido": "estrela", "tipo": "starmie", "experiencia": 40000}}}
    }

@sem_io
def test_10e_treinador_errado():
    reset()
    assert cadastrar_treinador("Ash Ketchum")
    treinador_nao_cadastrado(lambda : cadastrar_pokemon("Gary", "pi", "pikachu", 40000))
    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}}
    }

@sem_io
def test_11a_ok():
    reset()

    assert cadastrar_treinador("Ash Ketchum")
    cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)
    ganhar_experiencia("Ash Ketchum", "P", 1500)

    assert cadastrar_treinador("James")
    cadastrar_pokemon("James", "P", "WEEZING", 10000)
    cadastrar_pokemon("James", "Q", "VictREeBEL", 12000)
    ganhar_experiencia("James", "P", 2500)

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 51500}}},
        "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 12500}, "Q": {"apelido": "Q", "tipo": "victreebel", "experiencia": 12000}}}
    }

@sem_io
def test_11b_treinador_nao_existe():
    reset()
    treinador_nao_cadastrado(lambda : ganhar_experiencia("Cilan", "bob-esponja", 10000))
    assert api.get(f"{site_treinador}/treinador").json() == {}

@sem_io
def test_11c_pokemon_nao_existe():
    reset()
    assert cadastrar_treinador("Bonnie")
    pokemon_nao_cadastrado(lambda : ganhar_experiencia("Bonnie", "bob-esponja", 40000))

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Bonnie": {"nome": "Bonnie", "pokemons": {}}
    }

@sem_io
def test_11d_treinador_errado():
    reset()
    assert cadastrar_treinador("Serena")
    assert cadastrar_treinador("Dawn")
    cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
    pokemon_nao_cadastrado(lambda : ganhar_experiencia("Dawn", "fen", 100))

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
        "Dawn": {"nome": "Dawn", "pokemons": {}}
    }

@sem_io
def test_12a_ok():
    reset()

    assert cadastrar_treinador("Ash Ketchum")
    cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

    assert cadastrar_treinador("James")
    cadastrar_pokemon("James", "P", "WEEZING", 10000)
    cadastrar_pokemon("James", "Q", "Gloom", 12000)

    pikachu = localizar_pokemon("Ash Ketchum", "P")
    weezing = localizar_pokemon("James", "P")
    gloom = localizar_pokemon("James", "Q")

    assert type(pikachu) is Pokemon
    assert pikachu.nome_treinador == "Ash Ketchum"
    assert pikachu.apelido == "P"
    assert pikachu.tipo == "pikachu"
    assert pikachu.experiencia == 50000
    assert pikachu.nivel == 36
    assert pikachu.cor == "amarelo"
    assert pikachu.evoluiu_de == "pichu"
    assert_equals_unordered_list(["raichu"], pikachu.evolui_para)

    assert type(weezing) is Pokemon
    assert weezing.nome_treinador == "James"
    assert weezing.apelido == "P"
    assert weezing.tipo == "weezing"
    assert weezing.experiencia == 10000
    assert weezing.nivel == 21
    assert weezing.cor == "roxo"
    assert weezing.evoluiu_de == "koffing"
    assert_equals_unordered_list([], weezing.evolui_para)

    assert type(gloom) is Pokemon
    assert gloom.nome_treinador == "James"
    assert gloom.apelido == "Q"
    assert gloom.tipo == "gloom"
    assert gloom.experiencia == 12000
    assert gloom.nivel == 25
    assert gloom.cor == "azul"
    assert gloom.evoluiu_de == "oddish"
    assert_equals_unordered_list(["vileplume", "bellossom"], gloom.evolui_para)

@sem_io
def test_12b_treinador_nao_existe():
    reset()
    treinador_nao_cadastrado(lambda : localizar_pokemon("Cilan", "bob-esponja"))
    assert api.get(f"{site_treinador}/treinador").json() == {}

@sem_io
def test_12c_pokemon_nao_existe():
    reset()
    assert cadastrar_treinador("Bonnie")
    pokemon_nao_cadastrado(lambda : localizar_pokemon("Bonnie", "bob-esponja"))

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Bonnie": {"nome": "Bonnie", "pokemons": {}}
    }

@sem_io
def test_12d_treinador_errado():
    reset()
    assert cadastrar_treinador("Serena")
    assert cadastrar_treinador("Dawn")
    cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
    pokemon_nao_cadastrado(lambda : localizar_pokemon("Dawn", "fen"))

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
        "Dawn": {"nome": "Dawn", "pokemons": {}}
    }

@sem_io
def test_13a_ok():
    reset()

    assert cadastrar_treinador("Ash Ketchum")
    cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

    assert cadastrar_treinador("James")
    cadastrar_pokemon("James", "P", "WEEZING", 10000)
    cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

    ash = detalhar_treinador("Ash Ketchum")
    james = detalhar_treinador("James")

    assert ash == {"P": "pikachu"}
    assert james == {"P": "weezing", "Q": "weepinbell"}

@sem_io
def test_13b_treinador_nao_existe():
    reset()
    treinador_nao_cadastrado(lambda : detalhar_treinador("Cilan"))
    assert api.get(f"{site_treinador}/treinador").json() == {}

@sem_io
def test_14a_ok():
    reset()

    assert cadastrar_treinador("Ash Ketchum")
    cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

    assert cadastrar_treinador("Prof. Carvalho")

    assert cadastrar_treinador("James")
    cadastrar_pokemon("James", "P", "WEEZING", 10000)
    cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

    excluir_treinador("Ash Ketchum")

    resposta1 = api.get(f"{site_treinador}/treinador")
    assert resposta1.json() == {
        "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
        "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
    }
    treinador_nao_cadastrado(lambda : detalhar_treinador("Ash Ketchum"))
    treinador_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"))

    excluir_treinador("James")

    resposta2 = api.get(f"{site_treinador}/treinador")
    assert resposta2.json() == {
        "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
    }
    treinador_nao_cadastrado(lambda : detalhar_treinador("James"))
    treinador_nao_cadastrado(lambda : localizar_pokemon("James", "P"))
    treinador_nao_cadastrado(lambda : localizar_pokemon("James", "Q"))

    excluir_treinador("Prof. Carvalho")

    resposta3 = api.get(f"{site_treinador}/treinador")
    assert resposta3.json() == {}
    treinador_nao_cadastrado(lambda : detalhar_treinador("Prof. Carvalho"))

@sem_io
def test_14b_treinador_nao_existe():
    reset()

    treinador_nao_cadastrado(lambda : excluir_treinador("Kiawe"))
    assert api.get(f"{site_treinador}/treinador").json() == {}

    assert cadastrar_treinador("Kiawe")
    cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
    treinador_nao_cadastrado(lambda : excluir_treinador("Lillie"))
    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
    }

    excluir_treinador("Kiawe")
    assert api.get(f"{site_treinador}/treinador").json() == {}

@sem_io
def test_15a_ok():
    reset()

    assert cadastrar_treinador("Ash Ketchum")
    cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

    assert cadastrar_treinador("Prof. Carvalho")

    assert cadastrar_treinador("James")
    cadastrar_pokemon("James", "P", "WEEZING", 10000)
    cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

    excluir_pokemon("Ash Ketchum", "P")

    resposta1 = api.get(f"{site_treinador}/treinador")
    assert resposta1.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
        "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
        "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
    }
    pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"))
    localizar_pokemon("James", "P")
    localizar_pokemon("James", "Q")

    excluir_pokemon("James", "Q")

    resposta2 = api.get(f"{site_treinador}/treinador")
    assert resposta2.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
        "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}}},
        "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
    }
    pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"))
    localizar_pokemon("James", "P")
    pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"))

    excluir_pokemon("James", "P")

    resposta3 = api.get(f"{site_treinador}/treinador")
    assert resposta3.json() == {
        "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
        "James": {"nome": "James", "pokemons": {}},
        "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
    }
    pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"))
    pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "P"))
    pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"))

@sem_io
def test_15b_treinador_nao_existe():
    reset()

    assert cadastrar_treinador("Kiawe")
    cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
    treinador_nao_cadastrado(lambda : excluir_pokemon("Lillie", "c"))
    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
    }

    localizar_pokemon("Kiawe", "c")
    assert api.get(f"{site_treinador}/treinador").json() == {
        "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
    }

@sem_io
def test_15c_pokemon_nao_existe():
    reset()

    assert cadastrar_treinador("Kiawe")
    cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
    pokemon_nao_cadastrado(lambda : excluir_pokemon("Kiawe", "d"))
    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {
        "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
    }

    localizar_pokemon("Kiawe", "c")
    assert api.get(f"{site_treinador}/treinador").json() == {
        "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
    }

    excluir_pokemon("Kiawe", "c")
    assert api.get(f"{site_treinador}/treinador").json() == {
        "Kiawe": {"nome": "Kiawe", "pokemons": {}}
    }

@sem_io
def test_98a_limpeza():
    reset()
    assert cadastrar_treinador("Tracey")
    cadastrar_pokemon("Tracey", "m", "MARILL", 40000)

    reset()
    treinador_nao_cadastrado(lambda : detalhar_treinador("Tracey"))
    treinador_nao_cadastrado(lambda : localizar_pokemon("Tracey", "m"))
    treinador_nao_cadastrado(lambda : ganhar_experiencia("Tracey", "m", 4000))
    treinador_nao_cadastrado(lambda : cadastrar_pokemon("Tracey", "t", "togepi", 500))
    treinador_nao_cadastrado(lambda : excluir_pokemon("Tracey", "t"))
    treinador_nao_cadastrado(lambda : excluir_treinador("Tracey"))

    resposta = api.get(f"{site_treinador}/treinador")
    assert resposta.json() == {}

@sem_io
def test_99a_print():
    assert not sem_io.usou_print, "Você não deveria utilizar a função print neste exercício."

@sem_io
def test_99b_input():
    assert not sem_io.usou_input, "Você não deveria utilizar a função input neste exercício."