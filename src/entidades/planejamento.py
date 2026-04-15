from entidades.equipamento import get_equipamentos

planejamentos = {}

def get_planejamentos(): return planejamentos

def inserir_planejamento(planejamento):
    nome_planejamento = planejamento.nome
    if nome_planejamento not in planejamentos.keys():
        planejamentos[nome_planejamento] = planejamento
        return True
    else:
        print('Planejamento ' + nome_planejamento + ' já tem cadastro')
        return False

class Planejamento:
    def __init__(self, nome, data_início, agência_responsável):
        self.nome = nome
        self.data_início = data_início
        self.agência_responsável = agência_responsável
        self.equipamentos = {}

    def __str__(self):
        formato = '{} {:<28} {} {:<12} {} {:<20} {}'
        planejamento_formatado = formato.format(
            '|', self.nome,
            '|', str(self.data_início),
            '|', self.agência_responsável,
            '|')
        return planejamento_formatado

    def inserir_equipamentos(self, nomes_equipamentos):
        for nome_equipamento in nomes_equipamentos:
            if nome_equipamento in get_equipamentos().keys():
                self.equipamentos[nome_equipamento] = get_equipamentos()[nome_equipamento]
            else:
                print('Equipamento ' + nome_equipamento + ' não tem cadastro')
