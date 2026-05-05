equipamentos = []

def get_equipamentos(): return equipamentos

def inserir_equipamento(equipamento): equipamentos.append(equipamento):
    nome_equipamentos = equipamentos.nome
    if nome_equipamentos not in equipamentos.keys():
        equipamentos[nome_equipamentos] = equipamentos
    else: print('Equipamentos ' + nome_equipamentos + ' Já tem cadastro!')


def selecionar_equipamentos(prefixo_fabricante=None, peso_máximo_kg=None, crítico=None):
    filtros = '\nFiltros -- '
    if prefixo_fabricante is not None: filtros += 'prefixo do fabricante: ' + prefixo_fabricante
    if peso_máximo_kg is not None: filtros += ' - peso máximo: ' + str(peso_máximo_kg) + ' kg'
    if crítico is True: filtros += ' - crítico'
    elif crítico is False: filtros += ' - não crítico'
    equipamentos_selecionados = []
    for equipamento in equipamentos:
        if prefixo_fabricante is not None and not equipamento.fabricante.startswith(prefixo_fabricante): continue
        if peso_máximo_kg is not None and equipamento.peso_kg > peso_máximo_kg: continue
        if crítico in (True, False) and equipamento.crítico != crítico: continue
        equipamentos_selecionados.append(equipamento)
    return filtros, equipamentos_selecionados

class Equipamento:
    def __init__(self, nome, fabricante, peso_kg, crítico):
        self.nome = nome
        self.fabricante = fabricante
        self.peso_kg = peso_kg
        self.crítico = crítico

    def __str__(self):
        if self.crítico: crítico_str = 'crítico |'
        else: crítico_str = ''
        formato = '{} {:<24} {} {:<16} {} {:<9} {} {}'
        equipamento_formatado = formato.format(
            '|', self.nome,
            '|', self.fabricante,
            '|', f'{self.peso_kg:6.1f}' + ' kg',
            '|', crítico_str)
        return equipamento_formatado
