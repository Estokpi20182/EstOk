from errbot import BotPlugin, botcmd, botmatch
import pymongo

class estoque(BotPlugin):
    """Adicionar ao estoque"""
    @botcmd
    def adicionar(self, msg, args):
        """Inicia"""
        yield "Qual item voce quer adiconar a lista?"

    @botmatch(r'^[A-z].*$', flow_only=True)
    def aitem(self, msg, match):
        """Usuario diz qual item adicionar"""
        aitem = match.string
        aessecara = pymongo.MongoClient().estoque.estoque 
        bananao = aessecara.insert({"id": str(msg.frm), "item": aitem, "quantidade": 0})

    @botcmd
    def comprei(self, msg, args):
        """Inicia"""
        yield "O que e o quanto voce comprou?"

    @botmatch(r'^[A-z].* [0-9].*$', flow_only=True)
    def item(self, msg, match):
        """Usuario diz oque, e o quanto comprou."""
        item = match.string.split(' ')[0]
        quantidade = match.string.split(' ')[1]
        yield "Adicionando " + quantidade + " " + item + "(s). "
        essecara = pymongo.MongoClient().estoque.estoque
        resultado = essecara.find_one_and_update({ "id": str(msg.frm), "item" : item}, {'$inc': { "quantidade": int(quantidade)}})
        banana = pymongo.MongoClient().estoque.estoque
        bananao = banana.find_one({"id": str(msg.frm), "item": item})
        yield "Show, agora voce tem " + str(int(bananao["quantidade"])) + " " + bananao["item"] + "(s)."


    @botcmd
    def usei(self, msg, args):
        """Inicia"""
        yield "O que e o quanto voce usou?"

    @botmatch(r'^[A-z].* [0-9].*$', flow_only=True)
    def uitem(self, msg, match):
        """Usuario diz oque, e o quanto usou."""
        uitem = match.string.split(' ')[0]
        uquantidade = match.string.split(' ')[1]
        yield "Removendo " + uquantidade + " " + uitem + "(s). "
        uessecara = pymongo.MongoClient().estoque.estoque
        uresultado = uessecara.find_one_and_update({ "id": str(msg.frm), "item" : uitem}, {'$inc': { "quantidade": -(int(uquantidade))}})
        ubanana = pymongo.MongoClient().estoque.estoque
        ubananao = ubanana.find_one({"id": str(msg.frm), "item": uitem})
        yield "Show, agora voce tem " + str(int(ubananao["quantidade"])) + " " + ubananao["item"] + "(s)."

    @botcmd
    def estoque(self, msg, args):
        """Cliente perguntando quanto tem de algo"""
        yield "Qual item?"

    @botmatch(r'^[A-z].*$', flow_only=True)
    def qitem(self, msg, match):
        """Perguntar de qual item"""
        item = match.string
        cliente = pymongo.MongoClient().estoque.estoque
        quantidade = cliente.find_one({"id": str(msg.frm), "item": item})
        yield "Voce tem " + str(int(quantidade["quantidade"])) + " " + quantidade["item"] + "(s)."

    @botcmd
    def saymyname(self, msg, args):
        """ha"""
        yield str(msg.frm)
