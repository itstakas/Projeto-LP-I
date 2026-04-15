explorações_espaciais = {}

def get_explorações_espaciais(): return explorações_espaciais

def inserir_exploração_espacial(exploração_espacial):
    nome_exploração_espacial = exploração_espacial.nome
    if nome_exploração_espacial not in explorações_espaciais.keys():
        explorações_espaciais[nome_exploração_espacial] = exploração_espacial
        return True
    else:
        print('Exploração Espacial ' + nome_exploração_espacial + ' já tem cadastro')
        return False

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
