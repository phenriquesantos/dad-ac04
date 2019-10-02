from requests import api
from dataclasses import dataclass

"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar e executar o PokeAPI, o treinador e os testes no documento entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Se algum dos parâmetros ser inválido, uma ValueError deve ser lançada. Recomenda-se usar as funções check_int e check_str acima para ajudar na validação.
6. Se algum parâmetro puder ser determinado como inválido antes que alguma chamada a um servidor externo seja realizada, então ele deve ser detectado como tal sem que o servidor seja contactado, mesmo se ele estiver off-line.
7. Em todos os casos onde procura-se algum tipo de pokémon pelo nome ou pelo número e o mesmo não existir, uma exceção PokemonNaoExisteException deve ser lançada.
8. Em todos os casos onde procura-se algum treinador cadastrado e o mesmo não existir, uma exceção TreinadorNaoCadastradoException deve ser lançada.
9. Em todos os casos onde procura-se algum pokémon cadastrado e o mesmo não existir, uma exceção PokemonNaoCadastradoException deve ser lançada.
10. Em todos os casos onde tenta-se cadastrar um pokémon e o mesmo já exista, uma exceção PokemonJaCadastradoException deve ser lançada.
11. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower() e upper() da classe string.
12. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.
13. Não faça conexões com as URLs externas (https://pokeapi.co). O motivo disso é que eles irão bloquear IPs que fizerem um número muito grande de requisições.

Alguns exemplos de URLs que podem servir de inspiração:
http://localhost:8000/api/v2/
http://localhost:8000/api/v2/pokemon/39/
http://localhost:8000/api/v2/pokemon/jigglypuff/
http://localhost:8000/api/v2/pokemon-species/39/
http://localhost:8000/api/v2/pokemon-species/jigglypuff/
http://localhost:8000/api/v2/evolution-chain/11/
http://localhost:8000/api/v2/growth-rate/1/
http://localhost:8000/api/v2/pokemon-color/2/
"""

"""
Não altere estas URLs. Elas são utilizadas para conectar no treinador e no PokeAPI, respectivamente.
"""
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "http://127.0.0.1:8000"
pokeapi_version = "/api/v2"

"""
Vamos precisar destas quatro exceções personalizadas.
"""
class PokemonNaoExisteException(Exception):
    pass

class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma ValueError se não for.
"""
def check_int(a):
    if type(a) is not int:
        raise ValueError()

"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia e lança uma ValueError se não for.
"""
def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()

"""
Esta classe será utilizada no exercício 12 abaixo.
"""
@dataclass(frozen = True)
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int
    cor: str
    evoluiu_de: str
    evolui_para: list

def get_pokemon(param):
    result = api.get(site_pokeapi + pokeapi_version + '/pokemon/' + str(param).lower() + '/')
    if result.status_code == 200:
        return result.json()

    else:
        raise PokemonNaoExisteException()

def get_specie(url_especie):
    result = api.get(url_especie)
    if result.status_code == 200:
        return result.json()

"""
1. Dado o número de um pokémon, qual é o nome dele?
"""
def nome_do_pokemon(numero):
    check_int(numero)
    pokemon = get_pokemon(numero)
    return pokemon['name']

"""
2. Dado o nome de um pokémon, qual é o número dele?
"""
def numero_do_pokemon(nome):
    check_str(nome)
    pokemon = get_pokemon(nome)
    return pokemon['id']

"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?
"""
def color_of_pokemon(nome):
    check_str(nome)
    pokemon = get_pokemon(nome)
    pokemon_specie = get_specie(pokemon['species']['url'])
    return pokemon_specie['color']['name']

"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?
"""
def cor_do_pokemon(nome):
    colors = { "brown": "marrom", "yellow": "amarelo", "blue": "azul", "pink": "rosa",
               "gray": "cinza", "purple": "roxo", "red": "vermelho", "white": "branco",
               "green": "verde", "black": "preto" }

    return colors[color_of_pokemon(nome)]

"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""
def tipos_do_pokemon(nome):
    check_str(nome)
    pokemon = get_pokemon(nome)
    pt_types = { "normal": "normal", "fighting": "lutador", "flying": "voador", 
                 "poison": "veneno", "ground": "terra", "rock": "pedra", "bug": "inseto",
                 "ghost": "fantasma", "steel": "aço", "fire": "fogo", "water": "água", 
                 "grass": "grama", "electric": "elétrico", "psychic": "psíquico", 
                 "ice": "gelo", "dragon": "dragão", "dark": "noturno", "fairy": "fada" }
    types = []
    for poke_type in pokemon['types']:
        types.append(pt_types[poke_type['type']['name']])
    
    return types

"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    check_str(nome)
    pokemon = get_pokemon(nome)
    specie_pokemon = get_specie(pokemon['species']['url'])
    if specie_pokemon['evolves_from_species'] == None:
        return None

    return specie_pokemon['evolves_from_species']['name']

"""
7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evoluitivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []
"""

def get_evolution(nome):
    check_str(nome)
    pokemon = get_pokemon(nome)
    pokemon_specie = get_specie(pokemon['species']['url'])
    result = api.get(pokemon_specie['evolution_chain']['url'])
    return result.json()

def search_evolve(array, target):
    result = []

    for i in array:
        if i['species']['name'] == target.lower():
            result = i['evolves_to']
        else:
            if i['evolves_to'] != []:
                result = search_evolve(i['evolves_to'], target)

    return result

def next_evolutions(evolves):
    result = []
    for specie in evolves:
        result.append(specie['species']['name'])
    
    return result

def evolucoes_proximas(nome):
    pokemon = get_evolution(nome)
    if pokemon['chain']['species']['name'] == nome.lower():
        return next_evolutions(pokemon['chain']['evolves_to'])
    else:
        my_specie = search_evolve(pokemon['chain']['evolves_to'], nome)
        return next_evolutions(my_specie)
"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
"""
def nivel_do_pokemon(nome, experiencia):
    if experiencia < 0:
        raise ValueError()

    check_str(nome)
    pokemon = get_pokemon(nome)
    pokemon_specie = get_specie(pokemon['species']['url'])
    result = api.get(pokemon_specie['growth_rate']['url'])
    level = result.json()
    current_level = 0
    for i in level['levels']:
        if i['experience'] < experiencia:
            current_level = i['level']
        else:
            break

    return current_level
    

"""
9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e False em caso contrário (já existia).
"""
def cadastrar_treinador(nome):
    check = api.put(site_treinador + '/treinador/' + nome)
    if check.status_code == 303:
        return False

    return check.json()


"""
10. Imagine que você capturou dois pokémons do mesmo tipo. Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, mas não pode ter dois pokémons diferentes com o mesmo apelido.
Assim sendo, dado um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência, cadastre o pokémon com o tipo correspondente ao treinador dado na API do treinador.
Certifique-se de que todos os dados são válidos.
"""
def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    get_pokemon(tipo_pokemon)
    data = {'tipo': tipo_pokemon.lower(), 'experiencia': experiencia}
    result = api.put(site_treinador + '/treinador/' + nome_treinador + '/' + apelido_pokemon, None, json=data)
    if result.status_code == 404:
        raise TreinadorNaoCadastradoException()
    elif result.status_code == 409:
        raise PokemonJaCadastradoException()

    return True

"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.
"""
def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):
    # /treinador/<nome>/<apelido>/exp
    result = api.post(site_treinador + '/treinador/' + nome_treinador + '/' + apelido_pokemon + '/exp', None, json={'experiencia': experiencia})
    if result.status_code == 404:
        if result.content.decode('utf-8') == "Treinador não existe.":
            raise TreinadorNaoCadastradoException()
        elif result.content.decode('utf-8') == "Pokémon não existe.":
            raise PokemonNaoCadastradoException()
    
    return True

"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon mostrando:
Qual é a sua espécie, a sua quantidade de experiência e em que nível ele está.
"""
def localizar_pokemon(nome_treinador, apelido_pokemon):
    result = api.get(site_treinador + '/treinador/' + nome_treinador + '/' + apelido_pokemon)
    if result.status_code == 404:
        if result.content.decode('utf-8') == "Treinador não existe.":
            raise TreinadorNaoCadastradoException()
        elif result.content.decode('utf-8') == "Pokémon não existe.":
            raise PokemonNaoCadastradoException()

    treinador_pokemon = result.json()
    nivel_pokemon = nivel_do_pokemon(treinador_pokemon['tipo'], treinador_pokemon['experiencia'])
    cor_pokemon = cor_do_pokemon(treinador_pokemon['tipo'])
    evolucao_ant = evolucao_anterior(treinador_pokemon['tipo'])
    evolucoes = evolucoes_proximas(treinador_pokemon['tipo'])

    return Pokemon(nome_treinador, apelido_pokemon, treinador_pokemon['tipo'], treinador_pokemon['experiencia'], nivel_pokemon, cor_pokemon, evolucao_ant, evolucoes)

"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário contendo como chaves, os apelidos de seus pokémons e como valores os tipos deles.
"""
def detalhar_treinador(nome_treinador):
    result = api.get(site_treinador + '/treinador/' + nome_treinador)
    if result.status_code == 404:
        raise TreinadorNaoCadastradoException()

    treinador = result.json()
    retorno = {}
    for pokemon in treinador['pokemons']:
        retorno[pokemon] = treinador['pokemons'][pokemon]['tipo'] 

    return retorno


"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.
"""
def excluir_treinador(nome_treinador):
    result = api.delete(site_treinador + '/treinador/' + nome_treinador)
    if result.status_code == 404:
        raise TreinadorNaoCadastradoException()

    return True

"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.
"""
def excluir_pokemon(nome_treinador, apelido_pokemon):
    result = api.delete(site_treinador + '/treinador/' + nome_treinador + '/' + apelido_pokemon)
    if result.status_code == 404:
        if result.content.decode('utf-8') == "Treinador não existe.":
            raise TreinadorNaoCadastradoException()
        elif result.content.decode('utf-8') == "Pokémon não existe.":
            raise PokemonNaoCadastradoException()

    return True

# if __name__ == "__main__":
#     # print(evolucoes_proximas('charmander'))
#     # print(evolucoes_proximas("ChArMeLeON"))
#     # print(evolucoes_proximas('CHARIZARD'))
#     # print(evolucoes_proximas("torchic"))
#     # print(evolucoes_proximas("turtonator"))
#     # print(evolucoes_proximas("PoliWHIRL"))
#     # print(evolucoes_proximas("espeon"))
#     # print(evolucoes_proximas("leafeon"))
#     # print(evolucoes_proximas("politoed"))
#     # print(evolucoes_proximas("lugia"))
#     # print(nivel_do_pokemon("Magikarp",       900))
#     # print(cadastrar_treinador("Ash Ketchum"))
#     # print(detalhar_treinador("Ash Ketchum") == {})
#     # print(cadastrar_treinador("Jessie"))
#     # print(cadastrar_pokemon("Jessie", "A", "ARBOK", 20000))
#     # print(cadastrar_pokemon("Jessie", "C", "Lickitung", 2500))
#     # print(cadastrar_pokemon("Max", "D", "lapras", 40000))
#     # cadastrar_treinador("Ash Ketchum")
#     # cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)
#     # localizar_pokemon("Ash Ketchum", "P")
#     # ganhar_experiencia("Ash Ketchu", "P", 1500)