#coding=utf-8

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

OPT_SAIR = 0
APLICAR = 1
aluno_teste = 1
lista_professores = []
lista_alunos = []
class Usuario(object):
    def __init__(self, _nome, _ID,_email):
        self.nome = _nome
        self.ID = _ID
        self.Email = _email
    def __str__(self):
        return "nome = {0}\tID = {1}\tEmail = {2}".format(self.nome,self.ID,self.Email)
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
        print "ID : " + str(super(Professor,self).getID())
        print "Email : " + super(Professor,self).getEmail()
        i=1
        for pibic in self.lista_pibicinfo:
            print "---Pibic {0}---".format(i)
            print "Nome do pibic : " + pibic.getNome()
            print "Descricao : " + pibic.getDescricao()
            i+=1
        print "------------------------------"
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
    def __init__(self,_nome,_dono, _descricao, _membros, _atividades, _tempo, _minIra, _prereq = [()]):
        self.nome = _nome
        self.dono = _dono #matricula do professor
        self.descricao = _descricao #descricao do pibic
        self.membros = _membros #lista da classe membro que ainda falta fazer
        self.atividades = _atividades #lista de atividades
        self.tempo = _tempo #duracao do pibic em semestres
	self.minIra = _minIra #
	self.prereq = _prereq #
    def __str__(self):
        return "nome = {5}\ndono = {0}\ndescricao = {4}\nmembros = {1}\natividades = {2}\ntempo = {3}\nIRAMin = {6}\nPrereq = {7}".format(self.dono,self.membros,self.atividades,self.tempo,self.descricao,self.nome,self.minIra, self.prereq)
    def mostra_pibicinfo(self):
        print "nome : " + self.getNome()
        print "descricao : " + self.getDescricao()
        print "membros : ", self.getMembros()
        print "atividades : ", self.getAtividades()
        print "duracao : " + str(self.getTempo())
        print "Ira minimo : " + str(self.getMinIRA())
        print "Pre requisitos : ", self.getPreq()
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

def pertence(lista,filtro):
    i=0
    for x in lista:
        if filtro(x):
            return True, i
        i+=1
    return False, -1

def pesquisar_pibics():
    #para cada professor listar os pibics de acordo com a categoria escolhida, alem disso quando for escolher um pibic para ser visitado deve-se checar qual professor o pibic foi escolhido
    # for professor in lista_professor:
        # existe, posicao = pertence_recursivo(professor.getPibicinfo(),lambda x: x.categoria == tipo)
        # if existe:
    print "nem tem pibic bbk"


def sendApplymail(professor,aluno):
    msg = MIMEMultipart()
    msg['From'] = aluno.getEmail()
    msg['To'] = professor.getEmail()
    msg['Subject'] = "Aplicacao no pibic"
    msg.attach(MIMEText(str(str(aluno) + "\n" + str(professor)), 'plain'))
    server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls()
    server.login("rapharelo@hotmail.com","populoso96")
    text = msg.as_string()
    server.sendmail(aluno.getEmail(),professor.getEmail(),text)
    server.quit()
    print "Enviei"

def mostrar_pibic_detalhado(posicao,which):
    lista_professores[posicao].getPibicinfo()[which].mostra_pibicinfo()
    print "0.Voltar"
    print "1.Aplicar-se"
    opt = int(raw_input("Insira uma opcao : "))
    if opt == APLICAR:
        sendApplymail(lista_professores[posicao],lista_alunos[aluno_teste])
        return OPT_SAIR

def pesquisar_professores():
    who = raw_input("Nome do professor a ser buscado : ")
    voltar = 0
    while not voltar:
        existe, posicao = pertence(lista_professores, lambda x: x.nome == who)
        if existe:
            lista_professores[posicao].mostra_minInfo()
            print "0.Voltar"
            opt = int(raw_input("Ver detalhamente o pibic : "))
            if opt == OPT_SAIR:
                voltar = 1
            elif opt > len(lista_professores[posicao].getPibicinfo()) or opt < 1:
                print "[ERRO] Pibic inexistente"
            else:
                if mostrar_pibic_detalhado(posicao,opt-1) == OPT_SAIR:
                    return OPT_SAIR
        else:
            print "[ERRO] Professor inexistente"
            return

def menu():
    sair = OPT_SAIR
    while(not sair):
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
    lista_professores.append(Professor("Rezende",123,"rapharelo@hotmail.com",[Pibicinfo("Seguranca",123,"Trabalhar com topicos na area de seguranca",[],["Varredura de redes","Verificar falhas","Realizar ataques"],2, 2, [("Canto Coral", "MM"), ("OA", "MS")])]))
    lista_professores.append(Professor("Ladeira",12,"samuelpala@gmail.com",[Pibicinfo("Inteligencia artificial",12,"Aplicacao de inteligencia artificial",[("Diego",1)],["Analisar o problema","Verificar a inteligencia","treinar a maquina"],4, 3, [("CB", "SS"), ("POO", "MS")]),Pibicinfo("BBKisse",12,"Aplicacao da bbkisse",[("Amaral",1),("Zika",0)],["Analisar o problema","Verificar a bbkisse","treinar a maquina para ser bbk"],20, 4, [("ED", "MM"), ("BD", "SR")])]))
    #teste professores OK
    # for professor in lista_professores:
        # print "-------------------------------"
        # print professor
    lista_alunos.append(Aluno("Rafael",554913100,"rapharelo@hotmail.com",Mwinfo(2.9,[("CB","MM"),("ED","SS"),("PS","MS"),("OA","MM"),("BD","II"),("POO","MS")])))
    lista_alunos.append(Aluno("Samuel",110066120,"rapharelo@hotmail.com",Mwinfo(3.6,[("CB","SS"),("ED","SS"),("PS","SS"),("OA","SS"),("BD","SS"),("POO","SS")])))
    #teste alunos
    # for aluno in lista_alunos:
        # print "---------------------------------"
        # print aluno

def main():
    init_cenarios()
    menu()
if __name__ == "__main__":
    main()
