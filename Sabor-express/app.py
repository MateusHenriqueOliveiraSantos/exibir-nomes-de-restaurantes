import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'status':False},
                {'nome':'Pizza Suprema','categoria':'Pizza', 'status':True},
                {'nome':'Cantina','categoria':'Italiano', 'status':False}]

def exibir_nome_do_programa():
    '''exibe o nome do programa'''
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    '''exibe as opções do que o usuário poderá escolher fazer'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. ativar/desativar restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''exibe um subtitulo descrevendo o que cada escolha do usuário estára executando
    
    Input: texto como parâmetro em cada função

    Output: texto na tela para o usuário descrevendo o que será executado 

    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    '''encerra a aplicação'''
    exibir_subtitulo('Finalizando o app!')

def voltar_ao_menu_principal():
    '''volta ao menu principal para que o usuàrio escolha outra ação
    
    Input: apertar qualquer tecla

    Output: volta para o main para que seja escolhida a próxima ação
    
    '''
    input('\nDigite uma tecla para voltar ao meno principal!')
    main()

def opcao_invalida():
    '''se colocar uma opção inválida ele mostra que a opção é inválida e volta ao menu principal para que sejam escolhidas outras ações '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''faz o cadastro de novos restaurantes e volta ao menu principal para que sejam escolhidas outras ações
    
    Inputs: 
    - o nome do restaurante
    - a categoria do restaurante

    Outputs:
    -dados do restaurante adicionado
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes!')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria_do_restaurante, 'status':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''lista todos os restaurante já adicionados
    
    inputs:
    -nome do restaurante
    -categoria do restaurante
    -status do restaurante

    Outputs:
    -lista de todos os resturantes
    -volta ao menu principal para escolher as próximas ações
    
    '''
    exibir_subtitulo('Listando os restaurantes:')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status = 'ativado' if restaurante['status'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''altera o estado atual em que estiver o restaurante selecionado
    
    Input: nome do restaurante

    Outputs:
    -altera o status do restaurante selecionado(se existir)
    -mostra que o status foi alterado(ativado\desativado)

    '''
    exibir_subtitulo('Alterando estado do restaurante!')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''onde o usuário escolhe a opção desejada
    
    Inputs:
    -opção escolhida pelo usuário

    Outputs:
    -retorna uma função diante da respectiva opção escolhida
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''limpa o console e mostra a tela inicial do programa com as opções para que o usuário escolha'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
