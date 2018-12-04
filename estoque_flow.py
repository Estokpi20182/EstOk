from errbot import botflow, FlowRoot, BotFlow


class EstoqueFlow(BotFlow):
    """Fluxo das mensagens para adicionar itens a lista."""

    @botflow
    def adiciona(self, flow: FlowRoot):
        """Adicionar item a lista"""
        acidiona = flow.connect('adicionar', auto_trigger=True)
        evai = acidiona.connect('aitem')

    @botflow
    def comprar(self, flow: FlowRoot):
        """Adicionar quantidade a lista"""
        pergunta = flow.connect('comprei', auto_trigger=True)
        resposta = pergunta.connect('item')

    @botflow
    def remover(self, flow: FlowRoot):
        """Remover quantidade a lista"""
        qualq = flow.connect('usei', auto_trigger=True)
        qiusou = qualq.connect('uitem')

    @botflow
    def oquetem(self, flow: FlowRoot):
        """Checar o estoque"""
        perguntaquanto = flow.connect('estoque', auto_trigger=True)
        oque = perguntaquanto.connect('qitem')
