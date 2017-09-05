class Cardapio(object):
	def __init__(self):
		self.semanas = []

	def adSemana(self, semana):
		self.semanas.append(semana)

class Semana(object):

	def __init__(self):
		self.refeicoes = []

	def adRefeicao(self, refeicao):
		self.refeicoes.append(refeicao)

class Refeicao(object):

	def __init__(self, dia, cafe, almoco, lanche, janta):
		self.dia = dia
		self.cafe = cafe
		self.almoco = almoco
		self.lanche = lanche
		self.janta = janta
