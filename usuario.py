#coding=utf-8

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import os
clear = lambda: os.system("clear")

OPT_SAIR = 0
APLICAR = 1
aluno_teste = 0
lista_professores = []
lista_alunos = []
class Usuario(object):
    def __init__(self, _nome, _ID,_email):
        self.nome = _nome
        self.ID = _ID
        self.Email = _email
    def __str__(self):
        return ".Nome : {0}\n.Matricula : {1}\n.Email : {2}".format(self.nome,self.ID,self.Email)
    def getNome(self):
        return self.nome
    def setNome(self,_nome):
        self.nome = _nome
    def getID(self):
        return self.ID
    def setID(self,_ID):
        self.ID = _ID
    def getEmail(self):
        return self.Email

class Aluno(Usuario):
    def __init__(self,_nome,_ID,_email,_mwinfo=None):
        Usuario.__init__(self,_nome,_ID,_email)
        self.mwinfo = _mwinfo
    def __str__(self):
        return super(Aluno,self).__str__() + "\n---mwinfo---\n{0}".format(self.mwinfo)
    def getMwinfo(self):
        return self.mwinfo
    def setMWinfo(self,_mwinfo):
        self.mwinfo = _mwinfo

class Professor(Usuario):
    def __init__(self,_nome,_ID,_email,_pibicinfo=[]):
        Usuario.__init__(self,_nome,_ID,_email)
        self.lista_pibicinfo = _pibicinfo
    def __str__(self):
        s = "\n---\n".join([str(pibic) for pibic in self.lista_pibicinfo])
        return super(Professor,self).__str__() + "\n---pibicinfo---\n{0}".format(s)
    def mostra_minInfo(self):
        print "------------------------------"
        print "Nome : " + super(Professor,self).getNome()
        print "Email : " + super(Professor,self).getEmail()
    def getPibicinfo(self):
        return self.lista_pibicinfo
    def setPibicinfo(self,_pibicinfo):
        self.lista_pibicinfo = _pibicinfo


class Mwinfo:
    def __init__(self,_IRA,_hist_escolar):
        self.IRA = _IRA #numero real
        self.hist_escolar = _hist_escolar #lista de tuplas, materias e mencao
        # self.grade_horaria = _grade_horaria #lista de tuplas, materias e horario
    def __str__(self):
        return "IRA = {0}\n---historico escolar---\n{1}".format(self.IRA,self.hist_escolar)
    def getMinmwinfo(self):
    	return (".IRA : " + str(self.getIRA()) + "\n" + 
				".Historico escolar : " + ",".join("(%s,%s)" % tup for tup in self.getHist_escolar()))
    def getIRA(self):
        return self.IRA
    def setIRA(self,_ira):
        self.IRA = _ira
    def getHist_escolar(self):
        return self.hist_escolar
    def setHist_escolar(self,_he):
        self.hist_escolar = _he
    # def getGrade_horaria(self):
        # return self.grade_horaria

class Pibicinfo:
    def __init__(self,_nome,_dono, _descricao, _membros, _atividades, _tempo, _categoria,_minIra, _prereq = [()]):
        self.nome = _nome
        self.dono = _dono #matricula do professor
        self.descricao = _descricao #descricao do pibic
        self.membros = _membros #lista da classe membro que ainda falta fazer
        self.atividades = _atividades #lista de atividades
        self.tempo = _tempo #duracao do pibic em semestres
        self.categoria = _categoria
	self.minIra = _minIra #
	self.prereq = _prereq #
    def __str__(self):
        return "nome = {5}\ndono = {0}\ndescricao = {4}\nmembros = {1}\natividades = {2}\ntempo = {3}\nIRAMin = {6}\nPrereq = {7}".format(self.dono,self.membros,self.atividades,self.tempo,self.descricao,self.nome,self.minIra, self.prereq)
    def getMinpibicinfo(self):
        return (".nome : " + self.getNome() + "\n" +
                ".descricao : " + self.getDescricao() + "\n" +
                ".tema : " + self.getCategoria())
    def getPibicinfo(self):
        return (".nome : " + self.getNome() + "\n" +
                ".descricao : " + self.getDescricao() + "\n" +
                ".categoria : " + self.getCategoria() + "\n" +
                ".membros : " + ",".join([seq[0] for seq in self.getMembros()]) + "\n" +
                ".atividades : \n-" + "\n-".join(self.getAtividades()) + "\n" +
                ".duracao : " + str(self.getTempo()) + "\n" +
                ".Ira minimo : " + str(self.getMinIRA()) + "\n" +
                ".Pre-requisitos : \n-" + "\n-" .join("(%s,%s)" % tup for tup in self.getPreq()))
    def mostra_pibicinfo(self):
        print self.getPibicinfo()
    def mostra_minInfo(self):
        print self.getMinpibicinfo()
    def getNome(self):
        return self.nome
    def getDono(self):
        return self.dono
    def setDono(self,_dono):
        self.dono = _dono
    def getDescricao(self):
        return self.descricao
    def setDescricao(self,_desc):
        self.descricao = _desc
    def getMembros(self):
        return self.membros
    def setMembros(self,_membs):
        self.membros = _membs
    def getAtividades(self):
        return self.atividades
    def setAtividades(self,_act):
        self.atividades = _act
    def getTempo(self):
        return self.tempo
    def setTempo(self,_tempo):
        self.tempo = _tempo
    def getMinIRA(self):
        return self.minIra
    def getPreq(self):
        return self.prereq
    def getCategoria(self):
        return self.categoria

def pertence(lista,filtro):
    i=0
    for x in lista:
        if filtro(x):
            return True, i
        i+=1
    return False, -1

def pertence_recursivo(lista,filtro):
	indices = []
	i=0
	for x in lista:
		if filtro(x):
			indices.append(i)
		i+=1
	return indices

def pesquisar_pibics():
    #para cada professor listar os pibics de acordo com a categoria escolhida, alem disso quando for escolher um pibic para ser visitado deve-se checar qual professor o pibic foi escolhido
    tipo = raw_input("Digite o tema do pibic : ")
    lista_categoria = []
    lista_pibics = []
    lista_final = []
    voltar = 0
    for professor in lista_professores:
    	posicoes = pertence_recursivo(professor.getPibicinfo(),lambda x: x.categoria == tipo)
        if posicoes != []:
            lista_categoria.append((professor.getNome(),posicoes)) #adiciona o professor e o pibic relacionado a ele na lista de encontrados a partir do tema
    if lista_categoria != []:
        while not voltar:
            k = 0
	    clear()
	    print "Pibics com o tema " + tipo + " encontrados : "
            for lista_pibics in lista_categoria:
                existe, posicao = pertence(lista_professores, lambda x: x.nome == lista_pibics[0]) #busca o professor contido na lista de pibics da categoria
                lista_professores[posicao].mostra_minInfo() #Mostra a informacao basica de cada professor
                for j in lista_pibics[1]: #para cada pibic que se enquadra na categoria
                    print ".Pibic " + str(k+1)
                    k+=1
                    lista_professores[posicao].getPibicinfo()[j].mostra_minInfo() #mostra a informacao basica do pibic
                    lista_final.append(lista_professores[posicao].getPibicinfo()[j])
            print "------------------------------"
            print "0.Voltar"
            opt = int(raw_input("Ver detalhamente o pibic : "))
            if opt == OPT_SAIR:
                voltar = 1
            else:
                if apply_to_pibic(lista_alunos[aluno_teste],lista_final[opt-1]) == OPT_SAIR:
                    return OPT_SAIR
    else:
	print "[ALRT] Nenhum pibic com o tema " + tipo + " foi encontrado"
	raw_input("[ENTER] para continuar")
	clear()

def sendApplymail(aluno,professor,pibic):
    msg = MIMEMultipart()
    msg['From'] = aluno.getEmail()
    msg['To'] = professor.getEmail()
    msg['Subject'] = "Aplicacao no pibic"
    msg.attach(MIMEText("Ola professor(a) voce possui uma nova aplicacao no seu pibic, as informacoes quanto ao pibic e o aluno estao abaixo: " + str("\n---Informacoes do aluno---\n" + aluno.getNome() + "\t" + str(aluno.getID()) + "\n" + aluno.getMwinfo().getMinmwinfo() + "\n---Informacoes do pibic---\n" + pibic.getMinpibicinfo()), 'plain'))
    server = smtplib.SMTP('smtp.live.com', 587) #conecta smtp para live.com email que estamos utilizando para enviar no momento
    server.set_debuglevel(1)
    server.starttls()
    server.login("rapharelo@hotmail.com","populoso96")
    text = msg.as_string()
    server.sendmail(aluno.getEmail(),professor.getEmail(),text)
    server.quit()
    print "[OK] Email enviado com sucesso"
    raw_input("[ENTER] para continuar")

def apply_to_pibic(aluno,pibic):
    clear()
    existe, posicao = pertence(lista_professores, lambda x: x.ID == pibic.getDono())
    professor  = lista_professores[posicao]
    professor.mostra_minInfo()
    print "---Detalhes do pibic---"
    pibic.mostra_pibicinfo()
    print "-----------------------"
    print "0.Voltar"
    print "1.Aplicar-se"
    opt = int(raw_input("Insira uma opcao : "))
    if opt == APLICAR:
        if aluno.getMwinfo().getIRA() >= pibic.getMinIRA():
            sendApplymail(aluno,professor,pibic)
            return OPT_SAIR
        else:
            print "[ALRT] O IRA do aluno eh menor do que o necessario"
	    raw_input("[ENTER] para continuar")

def pesquisar_professores():
    who = raw_input("Nome do professor a ser buscado : ")
    voltar = 0
    while not voltar:
	clear()
        existe, posicao = pertence(lista_professores, lambda x: x.nome == who)
        if existe:
            lista_professores[posicao].mostra_minInfo()
            i=1
            for pibic in lista_professores[posicao].getPibicinfo():
                print "\tPibic {0}".format(i)
                pibic.mostra_minInfo()
                i+=1
            print "------------------------------"
            print "0.Voltar"
            opt = int(raw_input("Ver detalhadamente o pibic : "))
            if opt == OPT_SAIR:
                voltar = 1
            elif opt > len(lista_professores[posicao].getPibicinfo()) or opt < 1:
                print "[ERRO] Pibic inexistente"
            else:
                if apply_to_pibic(lista_alunos[aluno_teste],lista_professores[posicao].getPibicinfo()[opt-1]) == OPT_SAIR:
                    return OPT_SAIR
        else:
            print "[ERRO] Professor inexistente"
            return

def menu():
    sair = OPT_SAIR
    while(not sair):
	clear()
        print "---Menu---"
        print "0.Sair\n1.Pesquisar Pibics\n2.Pesquisar Professores"
        opt = int(raw_input("Insira sua opcao : "))
        if(opt == 1):
            pesquisar_pibics()
        elif(opt == 2):
            pesquisar_professores()
        elif(opt == OPT_SAIR):
            sair = 1

def init_cenarios():
    lista_professores.append(
    Professor("Rezende",123,"gdbranco@gmail.com",#Nome, ID e email do professor
        [Pibicinfo("Seguranca",123,"Trabalhar com topicos na area de seguranca", #Criacao do pibic Area, ID do professor, Descricao
        [], #Lista de membros
        ["Varredura de redes","Verificar falhas","Realizar ataques"], #Lista de atividades
        2, #Duracao
        "computacao", #Tema
        3, #IRA minimo
        [("Canto Coral", "MM"), ("OA", "MS")])])) #Pre requisitos
    lista_professores.append(
    Professor("Ladeira",12,"gdbranco@gmail.com",
        [Pibicinfo("Inteligencia artificial",12,"Aplicacao de inteligencia artificial",
        [("Diego",1)],
        ["Analisar o problema","Verificar a inteligencia","treinar a maquina"],
        4,
        "computacao",
        4,
        [("CB", "SS"), ("POO", "MS")])]))
    lista_professores.append(
    Professor("Fernanda Lima",10,"ferlima@cic.unb.br",
        [Pibicinfo("Engenharia de Software",10,"pic - projeto de informacao cientifica",
        [("Rafael",0),("Guilherme",0)],
        ["Levantar os requisitos","Planejamento dos riscos","Desenvolvimento do prototipo de baixa fidelidade","desenvolvimento do prototipo"],
        1,
        "computacao",
        3,
        [("PS","MM"),("POO","MS")])]))
    lista_alunos.append(Aluno("Rafael",554913100,"rapharelo@hotmail.com",#Nome, matricula e email do aluno
        Mwinfo(5,[("CB","MM"),("ED","SS"),("PS","MS"),("OA","MM"),("BD","II"),("POO","MS")]))) #informacoes do matribula web
    lista_alunos.append(Aluno("Samuel",110066120,"samuelpala@gmail.com",
        Mwinfo(3.6,[("CB","SS"),("ED","SS"),("PS","SS"),("OA","SS"),("BD","SS"),("POO","SS")])))

def main():
    init_cenarios()
    menu()
if __name__ == "__main__":
    main()
