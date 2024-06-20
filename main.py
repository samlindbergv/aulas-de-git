from funcoes import *

def exercutar_sisitema():
    while True:
        print("\nMenu")
        print("1.Adicionar Paciente")
        print("2.Adicionar Médico")
        print("3.Pesquisar Paciente")
        print("4.Pesquisar Médico")
        print("5.Excluir Paciente")
        print("6.Excluir Médico")
        print("7.Agendar Consulta")
        print("8.Resgistrar Procedimento")
        print("9.Listar Procedimento")
        print("10.Sair")
        
        opcao = input("Escolha uma opção:")
        
        if opcao == '1':
            adicionar_Paciente()
        elif opcao == '2':
            adicionar_Medico()
        elif opcao == '3':
            pesquisar_Paciente()
        elif opcao == '4':
            pesquisar_Medico()
        elif opcao == '5':
            cpf = input("Digite o CPF do paciente que deseja excluir:")
            excluir_Paciente_Por_CPF(cpf)
        elif opcao == '6':
            crm = input("Digite o CRM do médico que deseja excluir:")
            excluir_Medico_Por_CRM(crm)
        elif opcao == '7':
            Agenda_Consulta()
        elif opcao == '8':
            Registrar_procedimento
        elif opcao == '9':
            Listar_procedimento
            
        elif opcao == '10':
            print("Obrigado por usar o Sistema")
            break
        else:
            print("Opição inválida. Tente novamente")
exercutar_sisitema()