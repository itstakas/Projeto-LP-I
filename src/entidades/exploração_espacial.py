explorações_espaciais = []

def get_explorações_espaciais(): return explorações_espaciais


def inserir_exploração_espacial(exploração_espacial): explorações_espaciais.append(exploração_espacial)


def selecionar_explorações_espaciais(destino=None, duração_máxima_dias=None, tripulada=None):
    filtros = '\nFiltros -- '
    if destino is not None: filtros += 'destino: ' + destino
    if duração_máxima_dias is not None: filtros += ' - duração máxima: ' + str(duração_máxima_dias) + ' dias'
    if tripulada is True: filtros += ' - tripulada'
    elif tripulada is False: filtros += ' - não tripulada'
    explorações_selecionadas = []
    for exploração_espacial in explorações_espaciais:
        if destino is not None and exploração_espacial.destino != destino: continue
        if duração_máxima_dias is not None and exploração_espacial.duração_dias > duração_máxima_dias: continue
        if tripulada in (True, False) and exploração_espacial.tripulada != tripulada: continue
        explorações_selecionadas.append(exploração_espacial)
    return filtros, explorações_selecionadas


class ExploraçãoEspacial:
    def __init__(self, nome, destino, duração_dias, tripulada):
        self.nome = nome
        self.destino = destino if destino in ('lua', 'marte', 'órbita_terrestre', 'asteroide', 'júpiter') else 'indefinido'
        self.duração_dias = duração_dias
        self.tripulada = tripulada


    def __str__(self):
        if self.tripulada: tripulada_str = 'tripulada |'
        else: tripulada_str = ''
        formato = '{} {:<22} {} {:<17} {} {:<9} {} {}'
        exploração_formatada = formato.format(
            '|', self.nome,
            '|', self.destino,
            '|', f'{self.duração_dias:4d}' + ' dias',
            '|', tripulada_str)
        return exploração_formatada
