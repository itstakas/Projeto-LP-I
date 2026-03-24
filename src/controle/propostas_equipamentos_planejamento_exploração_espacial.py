from util.gerais import imprimir_objetos
from entidades.exploração_espacial import (inserir_exploração_espacial, ExploraçãoEspacial,
    get_explorações_espaciais, selecionar_explorações_espaciais)
from entidades.equipamento import (inserir_equipamento, Equipamento,
    get_equipamentos, selecionar_equipamentos)

def cadastrar_explorações_espaciais():
    inserir_exploração_espacial(ExploraçãoEspacial(nome='Artemis IV', destino='lua', duração_dias=14, tripulada=True))
    inserir_exploração_espacial(ExploraçãoEspacial('Mars Base Alpha', 'marte', 730, True))
    inserir_exploração_espacial(ExploraçãoEspacial('ISS Resupply 2026', 'órbita_terrestre', 7, False))
    inserir_exploração_espacial(ExploraçãoEspacial('Hayabusa III', 'asteroide', 365, False))
    inserir_exploração_espacial(ExploraçãoEspacial('Europa Scout', 'júpiter', 1460, False))
    inserir_exploração_espacial(ExploraçãoEspacial('Lunar Gateway', 'lua', 90, False))

def cadastrar_equipamentos():
    inserir_equipamento(Equipamento(nome='Tanque de Oxigênio', fabricante='Air Liquide', peso_kg=85.5, crítico=True))
    inserir_equipamento(Equipamento('Câmera Multiespectral', 'Thales Alenia', 12.3, False))
    inserir_equipamento(Equipamento('Espectrômetro de Massa', 'NASA JPL', 45.0, True))
    inserir_equipamento(Equipamento('Reserva Alimentar 30d', 'SpaceFood Inc', 120.0, False))
    inserir_equipamento(Equipamento('Painel Solar Dobrável', 'Airbus Defence', 38.7, False))
    inserir_equipamento(Equipamento('Sensor de Radiação', 'NASA JPL', 8.2, True))
    inserir_equipamento(Equipamento('Reserva de Combustível', 'Air Liquide', 200.0, True))

if __name__ == '__main__':
    cadastrar_explorações_espaciais()
    cabeçalho = 'ExploraçãoEspacial : nome - destino - duração - tripulada'
    imprimir_objetos('\n' + cabeçalho, get_explorações_espaciais())

    filtros, selecionadas = selecionar_explorações_espaciais()
    imprimir_objetos(cabeçalho, selecionadas, filtros)

    filtros, selecionadas = selecionar_explorações_espaciais(duração_máxima_dias=400)
    imprimir_objetos(cabeçalho, selecionadas, filtros)

    filtros, selecionadas = selecionar_explorações_espaciais(duração_máxima_dias=400, destino='lua')
    imprimir_objetos(cabeçalho, selecionadas, filtros)

    filtros, selecionadas = selecionar_explorações_espaciais(duração_máxima_dias=400, destino='lua', tripulada=True)
    imprimir_objetos(cabeçalho, selecionadas, filtros)

    cadastrar_equipamentos()
    cabeçalho = 'Equipamento : nome - fabricante - peso - crítico'
    imprimir_objetos('\n' + cabeçalho, get_equipamentos())

    filtros, selecionados = selecionar_equipamentos()
    imprimir_objetos(cabeçalho, selecionados, filtros)

    filtros, selecionados = selecionar_equipamentos(prefixo_fabricante='Air')
    imprimir_objetos(cabeçalho, selecionados, filtros)

    filtros, selecionados = selecionar_equipamentos(prefixo_fabricante='Air', peso_máximo_kg=100.0)
    imprimir_objetos(cabeçalho, selecionados, filtros)

    filtros, selecionados = selecionar_equipamentos(prefixo_fabricante='Air', peso_máximo_kg=100.0, crítico=True)
    imprimir_objetos(cabeçalho, selecionados, filtros)
