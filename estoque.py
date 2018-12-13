from errbot import BotPlugin, botcmd, botmatch
import pymongo

class estoque(BotPlugin):
    """Adicionar ao estoque"""
    @botcmd
    def adicionar(self, msg, args):
        """Inicia e bot pergunta qual item listar."""
        yield "Qual item voce quer adiconar a lista?"

    @botmatch(r'^[A-z].*$', flow_only=True)
    def item_a_listar(self, msg, match):
        """Usuario diz qual item adicionar a lista."""
        item_a_listar = match.string
        banco = pymongo.MongoClient().estoque.estoque 
        adicionando_item = banco.insert({"id": str(msg.frm), "item": item_a_listar, "quantidade": 0})

    @botcmd
    def comprei(self, msg, args):
        """Inicia e bot pergunta qual item e quantos adicionar em quantidade."""
        yield "O que e o quanto voce comprou?"

    @botmatch(r'^[A-z].* [0-9].*$', flow_only=True)
    def item_a_incrementar(self, msg, match):
        """Usuario diz oque, e o quanto comprou."""
        item_a_incrementar = match.string.split(' ')[0]
        quantidade = match.string.split(' ')[1]
        yield "Adicionando " + quantidade + " " + item_a_incrementar + "(s). "
        banco_update = pymongo.MongoClient().estoque.estoque
        incrementando = banco_update.find_one_and_update({ "id": str(msg.frm), "item" : item_a_incrementar}, {'$inc': { "quantidade": int(quantidade)}})
        banco_find = pymongo.MongoClient().estoque.estoque
        verificacao_do_estoque = banco_find.find_one({"id": str(msg.frm), "item": item_a_incrementar})
        yield "Show, agora voce tem " + str(int(verificacao_do_estoque["quantidade"])) + " " + verificacao_do_estoque["item"] + "(s)."


    @botcmd
    def usei(self, msg, args):
        """Inicia e bot pergunta qual item e quantos remover em quantidade."""
        yield "O que e o quanto voce usou?"

    @botmatch(r'^[A-z].* [0-9].*$', flow_only=True)
    def item_a_reduzir(self, msg, match):
        """Usuario diz oque, e o quanto usou."""
        item_a_reduzir = match.string.split(' ')[0]
        quantidade = match.string.split(' ')[1]
        yield "Removendo " + quantidade + " " + item_a_reduzir + "(s). "
        banco_update = pymongo.MongoClient().estoque.estoque
        reduzindo = banco_update.find_one_and_update({ "id": str(msg.frm), "item" : item_a_reduzir}, {'$inc': { "quantidade": -(int(quantidade))}})
        banco_find = pymongo.MongoClient().estoque.estoque
        verificacao_do_estoque = banco_find.find_one({"id": str(msg.frm), "item": item_a_reduzir})
        yield "Top, agora voce tem " + str(int(verificacao_do_estoque["quantidade"])) + " " + verificacao_do_estoque["item"] + "(s)."

    @botcmd
    def estoque(self, msg, args):
        """Inicia e bot pergunta qual item usuario quer verificar."""
        yield "Qual item?"

    @botmatch(r'^[A-z].*$', flow_only=True)
    def item_a_verificar(self, msg, match):
        """Usuario diz qual item quer verificar"""
        item_a_verificar = match.string
        banco_find = pymongo.MongoClient().estoque.estoque
        estoque = banco_find.find_one({"id": str(msg.frm), "item": item_a_verificar})
        yield "Voce tem " + str(int(estoque["quantidade"])) + " " + estoque["item"] + "(s)."

    @botcmd
    def saymyname(self, msg, args):
        """ha"""
        yield str(msg.frm)
