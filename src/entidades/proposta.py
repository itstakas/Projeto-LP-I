from entidades.exploração_espacial import get_explorações_espaciais
from entidades.planejamento import get_planejamentos

propostas = []

def get_propostas(): return propostas

def inserir_proposta(proposta):
    if proposta not in propostas: propostas.append(proposta)
    else: print('Proposta já tem cadastro --- ' + str(proposta))

def criar_proposta(nome_planejamento, nome_exploração_espacial, data):
    planejamento = get_planejamentos().get(nome_planejamento)
    if planejamento is None:
        print('Planejamento ' + nome_planejamento + ' não cadastrado')
        return
    exploração_espacial = get_explorações_espaciais().get(nome_exploração_espacial)
    if exploração_espacial is None:
        print('Exploração Espacial ' + nome_exploração_espacial + ' não cadastrada')
        return
    proposta = Proposta(planejamento, exploração_espacial, data)
    inserir_proposta(proposta)

def selecionar_propostas(data_mínima_proposta=None, destino_exploração_espacial=None,
                          prefixo_agência_responsável_planejamento=None, peso_máximo_kg_equipamento=None):
    filtros = '\nFiltros -- '
    if data_mínima_proposta is not None: filtros += 'data mínima da proposta: ' + str(data_mínima_proposta)
    if destino_exploração_espacial is not None: filtros += ' - destino da exploração: ' + destino_exploração_espacial
    if prefixo_agência_responsável_planejamento is not None: filtros += ' - prefixo da agência responsável do planejamento: ' + prefixo_agência_responsável_planejamento
    if peso_máximo_kg_equipamento is not None: filtros += ' - peso máximo do equipamento: ' + str(peso_máximo_kg_equipamento) + ' kg'
    propostas_selecionadas = []
    for proposta in propostas:
        if data_mínima_proposta is not None and proposta.data < data_mínima_proposta: continue
        if destino_exploração_espacial is not None and proposta.exploração_espacial.destino != destino_exploração_espacial: continue
        if prefixo_agência_responsável_planejamento is not None and not proposta.planejamento.agência_responsável.startswith(prefixo_agência_responsável_planejamento): continue
        excluir_proposta = False
        for equipamento in proposta.planejamento.equipamentos.values():
            if peso_máximo_kg_equipamento is not None and equipamento.peso_kg > peso_máximo_kg_equipamento:
                excluir_proposta = True
                break
        if excluir_proposta: continue
        propostas_selecionadas.append(proposta)
    return filtros, propostas_selecionadas

class Proposta:
    def __init__(self, planejamento, exploração_espacial, data):
        self.planejamento = planejamento
        self.exploração_espacial = exploração_espacial
        self.data = data

    def __str__(self):
        formato = '{} {:<28} {} {:<22} {} {:<12} {}'
        proposta_formatada = formato.format(
            '|', self.planejamento.nome,
            '|', self.exploração_espacial.nome,
            '|', str(self.data),
            '|')
        return proposta_formatada

    def str_atributos_equipamentos(self):
        atributos_str = ''
        for índice, equipamento in enumerate(self.planejamento.equipamentos.values()):
            if índice > 0: atributos_str += ' - '
            atributos_str += f'{equipamento.peso_kg:.1f}' + ' kg'
        return atributos_str

    def str_filtro(self):
        formato = '{:<17} {} {:<20} {} {:<25} {}'
        filtro_formatado = formato.format(
            self.exploração_espacial.destino,
            '|', self.planejamento.agência_responsável,
            '|', self.str_atributos_equipamentos(),
            '|')
        return self.__str__() + filtro_formatado
