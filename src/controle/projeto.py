from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import Data
from entidades.equipamento import inserir_equipamento, Equipamento, get_equipamentos
from entidades.exploração_espacial import inserir_exploração_espacial, ExploraçãoEspacial, get_explorações_espaciais
from entidades.planejamento import inserir_planejamento, Planejamento, get_planejamentos
from entidades.proposta import criar_proposta, get_propostas, selecionar_propostas

def cadastrar_equipamentos():
    inserir_equipamento(Equipamento(nome='Tanque de Oxigênio', fabricante='Air Liquide', peso_kg=85.5, crítico=True))
    inserir_equipamento(Equipamento('Câmera Multiespectral', 'Thales Alenia', 12.3, False))
    inserir_equipamento(Equipamento('Espectrômetro de Massa', 'NASA JPL', 45.0, True))
    inserir_equipamento(Equipamento('Reserva Alimentar 30d', 'SpaceFood Inc', 120.0, False))
    inserir_equipamento(Equipamento('Painel Solar Dobrável', 'Airbus Defence', 38.7, False))
    inserir_equipamento(Equipamento('Sensor de Radiação', 'NASA JPL', 8.2, True))
    inserir_equipamento(Equipamento('Reserva de Combustível', 'Air Liquide', 200.0, True))

def cadastrar_explorações_espaciais():
    inserir_exploração_espacial(ExploraçãoEspacial(nome='Artemis IV', destino='lua', duração_dias=14, tripulada=True))
    inserir_exploração_espacial(ExploraçãoEspacial('Mars Base Alpha', 'marte', 730, True))
    inserir_exploração_espacial(ExploraçãoEspacial('ISS Resupply 2026', 'órbita_terrestre', 7, False))
    inserir_exploração_espacial(ExploraçãoEspacial('Hayabusa III', 'asteroide', 365, False))
    inserir_exploração_espacial(ExploraçãoEspacial('Europa Scout', 'júpiter', 1460, False))
    inserir_exploração_espacial(ExploraçãoEspacial('Lunar Gateway', 'lua', 90, False))

def cadastrar_planejamentos():
    planejamento = Planejamento(nome='Missão Lunar Básica', data_início=Data(1, 2, 2025), agência_responsável='NASA')
    inserir_planejamento(planejamento)
    planejamento.inserir_equipamentos(['Tanque de Oxigênio', 'Sensor de Radiação', 'Câmera Multiespectral'])

    planejamento = Planejamento('Missão Marte Avançada', Data(15, 7, 2026), 'SpaceX')
    inserir_planejamento(planejamento)
    planejamento.inserir_equipamentos(['Tanque de Oxigênio', 'Espectrômetro de Massa', 'Reserva de Combustível'])

    planejamento = Planejamento('Missão Orbital Simples', Data(10, 4, 2024), 'ESA')
    inserir_planejamento(planejamento)
    planejamento.inserir_equipamentos(['Câmera Multiespectral', 'Painel Solar Dobrável'])

    planejamento = Planejamento('Missão Asteroide Científica', Data(20, 9, 2025), 'NASA')
    inserir_planejamento(planejamento)
    planejamento.inserir_equipamentos(['Espectrômetro de Massa', 'Câmera Multiespectral', 'Sensor de Radiação'])

    planejamento = Planejamento('Missão Lunar Europeia', Data(5, 3, 2026), 'ESA')
    inserir_planejamento(planejamento)
    planejamento.inserir_equipamentos(['Painel Solar Dobrável', 'Sensor de Radiação'])

    planejamento = Planejamento('Missão Lunar NASA Pesada', Data(10, 6, 2025), 'NASA')
    inserir_planejamento(planejamento)
    planejamento.inserir_equipamentos(['Reserva de Combustível', 'Tanque de Oxigênio', 'Reserva Alimentar 30d'])

def cadastrar_propostas():
    criar_proposta('Missão Lunar Básica', 'Artemis IV', Data(1, 2, 2025))
    criar_proposta('Missão Marte Avançada', 'Mars Base Alpha', Data(15, 7, 2026))
    criar_proposta('Missão Orbital Simples', 'ISS Resupply 2026', Data(10, 4, 2024))
    criar_proposta('Missão Asteroide Científica', 'Hayabusa III', Data(20, 9, 2025))
    criar_proposta('Missão Lunar Europeia', 'Lunar Gateway', Data(5, 3, 2026))
    criar_proposta('Missão Lunar NASA Pesada', 'Artemis IV', Data(10, 6, 2025))

def imprimir_somente_para_alinhar_formatação():
    print('\nPlanejamentos : nome - data de início - agência responsável')
    for planejamento in get_planejamentos().values(): print(planejamento)
    print('\nEquipamentos : nome - fabricante - peso - crítico')
    for planejamento in get_planejamentos().values():
        for equipamento in planejamento.equipamentos.values(): print(equipamento)

if __name__ == '__main__':
    print('\nProposta de Equipamentos de um Planejamento para uma Exploração Espacial')
    cadastrar_equipamentos()
    imprimir_objetos(cabeçalho='\nEquipamento : nome - fabricante - peso - crítico',
                     objetos=get_equipamentos().values())

    cadastrar_explorações_espaciais()
    imprimir_objetos('\nExploraçãoEspacial : nome - destino - duração - tripulada',
                     get_explorações_espaciais().values())

    cadastrar_planejamentos()
    imprimir_somente_para_alinhar_formatação()

    print('\nPlanejamento : nome - data de início - agência responsável')
    print(' - Equipamento : nome - fabricante - peso - crítico')
    for índice, planejamento in enumerate(get_planejamentos().values()):
        imprimir_objeto(índice=índice, objeto_str=str(planejamento))
        imprimir_objetos_internos(planejamento.equipamentos.values())

    cadastrar_propostas()
    cabeçalho_proposta = 'Proposta : nome do planejamento - nome da exploração espacial - data da proposta'
    imprimir_objetos('\n' + cabeçalho_proposta, get_propostas())

    cabeçalho_proposta_filtros = (cabeçalho_proposta
        + '\n -- destino da exploração - agência do planejamento - pesos dos equipamentos')

    filtros, propostas_selecionadas = selecionar_propostas()
    imprimir_objetos_associação_filtros(cabeçalho_proposta_filtros, propostas_selecionadas, filtros)

    filtros, propostas_selecionadas = selecionar_propostas(data_mínima_proposta=Data(1, 1, 2025))
    imprimir_objetos_associação_filtros(cabeçalho_proposta_filtros, propostas_selecionadas, filtros)

    filtros, propostas_selecionadas = selecionar_propostas(Data(1, 1, 2025), destino_exploração_espacial='lua')
    imprimir_objetos_associação_filtros(cabeçalho_proposta_filtros, propostas_selecionadas, filtros)

    filtros, propostas_selecionadas = selecionar_propostas(Data(1, 1, 2025), 'lua',
                                                            prefixo_agência_responsável_planejamento='NASA')
    imprimir_objetos_associação_filtros(cabeçalho_proposta_filtros, propostas_selecionadas, filtros)

    filtros, propostas_selecionadas = selecionar_propostas(Data(1, 1, 2025), 'lua', 'NASA',
                                                            peso_máximo_kg_equipamento=100.0)
    imprimir_objetos_associação_filtros(cabeçalho_proposta_filtros, propostas_selecionadas, filtros)
