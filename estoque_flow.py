from errbot import botflow, FlowRoot, BotFlow


class EstoqueFlow(BotFlow):
    """Fluxo das mensagens para adicionar itens a lista."""

    @botflow
    def adiciona(self, flow: FlowRoot):
        """Adicionar item a lista"""
        inicia_adicionar = flow.connect('adicionar', auto_trigger=True)
        identifica_e_lista_item = inicia_adicionar.connect('item_a_listar')

    @botflow
    def incrementa(self, flow: FlowRoot):
        """Incrementar quantidade a lista"""
        inicia_comprar = flow.connect('comprei', auto_trigger=True)
        identifica_incrementa_e_verifica_item = inicia_comprar.connect('item_a_incrementar')

    @botflow
    def reduz(self, flow: FlowRoot):
        """Reduzir quantidade a lista"""
        inicia_reduz = flow.connect('usei', auto_trigger=True)
        identifica_reduz_e_verifica_item = inicia_reduz.connect('item_a_reduzir')

    @botflow
    def estoque(self, flow: FlowRoot):
        """Checar o estoque"""
        inicia_estoque = flow.connect('estoque', auto_trigger=True)
        identifica_e_verifica_item = inicia_estoque.connect('item_a_verificar')
