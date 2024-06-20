import banco_dados1 
conexao = banco_dados1.criarConexaoInicial("localhost", "root","root")

nome_bd = "SUS"

sql_create_bd = f"CREATE DATABASE IF NOT EXISTS {nome_bd}"

banco_dados1.criarBancoDados(conexao, "create database if not exists SUS")



sql_create_table_paciente = f"CREATE TABLE IF NOT EXISTS paciente ( \
    CPF VARCHAR(12) PRIMARY KEY, \
    nome VARCHAR(150), \
    idade INT,\
    endereco VARCHAR(50),\
    telefone VARCHAR(11))"
    
banco_dados1.criarTabela(conexao, "SUS", sql_create_table_paciente)
 
def adicionar_Paciente():
    print("por favor, insira seus dados:")
    nome = input("nome: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    endereco = input("Endereco: ")
    telefone = input("Telefone: ")
    
    sql_inserir_paciente = """INSERT INTO paciente (CPF, nome, idade, endereco, telefone) VALUES (%s,%s,%s,%s,%s)"""
   
    dados_paciente = (cpf, nome, idade, endereco, telefone)
    
    banco_dados1.insertNaTabela(conexao,sql_inserir_paciente,dados_paciente)    
adicionar_Paciente() 



sql_create_table_medico = f"CREATE TABLE IF NOT EXISTS medico ( \
    CPF VARCHAR(12) ,\
    nome VARCHAR(150), \
    idade INT,\
    endereco VARCHAR(50),\
    telefone VARCHAR(11),\
    CRM VARCHAR(12) PRIMARY KEY)"   

banco_dados1.criarTabela(conexao, "SUS", sql_create_table_medico)



def adicionar_Medico():
    print("Por favor, insira seus dados:")
    cpf = input("CPF: ")
    nome = input("Nome:")
    idade = int(input("Idade: "))
    endereco = input("Endereco: ")
    telefone = input("Telefone: ")
    crm = input("CRM: ")
    
    sql_inserir_medico = """INSERT INTO medico (CPF, Nome, Idade, Endereco, Telefone, CRM) VALUES (%s,%s,%s,%s,%s,%s) """

    dados_medico = (cpf, nome, idade, endereco, telefone, crm)
    
    banco_dados1.insertNaTabela(conexao,sql_inserir_medico,dados_medico)
adicionar_Medico()

   
def pesquisar_Paciente():
    cpf = input("Digite o CPF do paciente que busca:")
    sql_select_paciente = f"SELECT * FROM pacientes WHERE CPF = '{cpf}' "
    pacientes = banco_dados1.listarBancoDados(conexao,sql_select_paciente)
    print("Resultado da pesquisa de pacientes: ")
    for paciente in pacientes:
        print(paciente)
pesquisar_Paciente()
    
def pesquisar_Medico():
    crm = input("Digite o CPF do médico que busca:")
    sql_select_medico = f"SELECT * FROM medicos WHERE CPF = '{crm}' "
    medicos = banco_dados1.listarBancoDados(conexao,sql_select_medico)
    print("Resultado da pesquisa de medicos: ")
    for medico in medicos:
        print(medico)
pesquisar_Medico()

def excluir_Paciente_Por_CPF(conexao,cpf):
    sql_excluir_paciente = "DELEET FROM pacientes HWERE CPF = %s"
    dados_excluir_paciente = (cpf,)
    
    banco_dados1.excluirBancoDados(conexao,sql_excluir_paciente,dados_excluir_paciente)
    
    print(f"Paciente com CPF {cpf} foi excluído")


def excluir_Medico_Por_CRM(conexao,crm):
    sql_excluir_medivo = "DELEET FROM pacientes HWERE CPF = %s"
    dados_excluir_medico = (crm,)
    
    banco_dados1.excluirBancoDados(conexao,sql_excluir_medivo,dados_excluir_medico)
    
    print(f"Paciente com CRM {crm} foi excluído")


cpf = input("Digite o CPF do paciente que deseja excluir:")
excluir_Paciente_Por_CPF(conexao, cpf)

crm = input("Digite o CRM do médico que deseja excluir:")
excluir_Medico_Por_CRM(conexao, crm)

sql_select = "SELECT * FROM pacientes"
print(banco_dados1.listarBancoDados(conexao,sql_select))

campos_consulta =[
    "id INT AUTO_INCREMENT PRIMARY KEY"
    "CPF VARCHAR(12)"
    "CRM VANCHAR(12)"
    "FOREIGN KEY (cpf) REFERENCES pacientes(CPF)"
    "FOREIGN KEY (crm) REFERENCES medico(CRM)"
]
banco_dados1.criarTabela(conexao, "consultas", campos_consulta, "SUS")

def Agenda_Consulta():
    print("Por favor, insira os dados de consulta: ")
    cpf = input("CPF do paciente: ")
    crm = input("CRM do médico: ")
    
    sql_agendar_consulta = "INSERT INTO consulta (CPF,CRM) VALUES (%s,%s)"
    
    dasdos_consulta = (cpf, crm)
    
    banco_dados1.insertNaTabela(conexao,sql_agendar_consulta,dasdos_consulta)
Agenda_Consulta()

campos_procedimento =[
    "id INT AUTO_INCREMENT PRIMARY KEY"
    "descricao VARCHAR(350)"
    "paciente_CPF VANCHAR(12)"
    "medico_CRM VANCHAR(12"
    "data DATE"
    "FOREIGN KEY (paciente_cpf) REFERENCES pacientes(CPF)"
    "FOREIGN KEY (medico_crm) REFERENCES medico(CRM)"
]
banco_dados1.criarTabela(conexao,"procedimentos",campos_procedimento,"SUS")

def Registrar_procedimento():
    print("Por Favor, insira os dados do procedimento:")
    descricao = input("Descrição:")
    paciente_cpf = input("CPF do paciente:")
    medico_crm = input("CRM do medico:")
    data = input("Data(AAAA-MM-DD):")
    
    sql_inserir_procedimento = """INSERT INTO procedimentos(descricao, paciente_CPF,médico_CRM,data) VAlEUS(%s,%s,%s,%s)"""
    
    dados_procedimento =(descricao,paciente_cpf,medico_crm,data)
    banco_dados1.insertNaTabela(conexao,sql_inserir_procedimento,dados_procedimento)
    print("Procedimento realizado com sucesso!")

def Listar_procedimento():
    sql_select_procedimentos = "SELECT * FROM procedimentos"
    procedimentos = banco_dados1.listarBancoDados(conexao,sql_select_procedimentos)
    
    if procedimentos:
        print("Procedimentos registrados.")
        for procedimento in procedimentos:
            print(procedimento)
    else:
        print("Nenhum procedimento registrado.")
