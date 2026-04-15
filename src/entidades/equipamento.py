equipamentos = {}

def get_equipamentos(): return equipamentos

def inserir_equipamento(equipamento):
    nome_equipamento = equipamento.nome
    if nome_equipamento not in equipamentos.keys():
        equipamentos[nome_equipamento] = equipamento
        return True
    else:
        print('Equipamento ' + nome_equipamento + ' já tem cadastro')
        return False

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
