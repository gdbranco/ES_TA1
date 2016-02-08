class Usuario:
	def __init__(self, _nome, _ID):
		self.nome = _nome
		self.ID = _ID
	def __str__(self):
		return "nome = {0}\tID = {1}".format(self.nome,self.ID)
	def getNome(self):
		return.nome
	def getID(self):
		return.ID

class Aluno(Usuario):
	def __init__(self,_nome,_ID,_mwinfo):
		Usuario.__init__(self,_nome,_ID)
		self.mwinfo = _mwinfo
	def __str__(self):
		return Usuario.__str__ + "\n---mwinfo---\n{0}".format(self.mwinfo)
	def getMwinfo(self):
		return self.mwinfo

class Professor(Usuario):
	def __init__(self,_nome,_ID,_pibicinfo):
		Usuario.__init__(self,_nome,_ID)
	def __str__(self):
		return Usuario.__str__ + "\n---pibicinfo---\n{0}".format(self.pibicinfo)
	def getPibicinfo(self):
		return self.pibicinfo


class Mwinfo:
	def __init__(self,_IRA,_hist_escolar,_grade_horaria):
		self.IRA = _IRA #numero real
		self.hist_escolar = _hist_escolar #lista de tuplas, materias e menção
		self.grade_horaria = _grade_horaria #lista de tuplas, materias e horario
	def __str__(self):
		return "IRA = {0}\n---historico escolar---\n{1}\n---grade horaria---\n{2}".format(self.IRA,self.hist_escolar,self.grade_horaria)
	def getIRA(self):
		return self.IRA
	def getHist_escolar(self):
		return self.hist_escolar
	def getGrade_horaria(self):
		return self.grade_horaria

class Pibicinfo:
	def __init__(self, _dono, _membros, _atividades, _tempo):
		self.dono = _dono
		self.membros = _membros #lista da classe membro que ainda falta fazer
		self.atividades = _atividades
		self.tempo = _tempo
	def __str__(self):
		return "dono = {0}\nmembros = {1}\natividades = {2}\ntempo = {3}".format(self.dono,self.membros,self.atividades,self.tempo)
	def getDono(self):
		return self.dono
	def getMembros(self):
		return self.membros
	def getAtividades(self):
		return self.atividades
	def getTempo(self):
		return self.tempo
