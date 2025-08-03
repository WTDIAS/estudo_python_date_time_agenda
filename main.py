from compromisso import Compromisso
from utils import validadores


stop = False
agenda = {}

try:
    qtd_agendamento = int(input("Deseja fazer mais que um agendamento? Informe a quantidade.").strip())
except:
    qtd_agendamento = 1


while qtd_agendamento > 0:
    descricao = input("Forneça a descrição para o compromisso ou stop para sair: ")
    descricao = descricao.strip().lower().title()

    while True:
        input_data = input("Forneça a DATA para o compromisso ou stop para sair: ").strip() 
        if input_data == "stop":
            break
        data = validadores.valida_data(input_data)
        if data:
            break          
        else:
            print("Data inválida, tente novamente: ")        
    
            
    while True:
        input_hora = input("Forneça o HORARIO para o compromisso ou stop para sair: ").strip()
        if input_hora == "stop":
            break
        hora = validadores.valida_hora(input_hora)
        if hora:
            break          
        else:
            print("Data inválida, tente novamente: ")

    meu_compromisso = Compromisso(descricao,data,hora)
    chave = validadores.gerar_chave()
    agenda[chave] = meu_compromisso
    
    qtd_agendamento -= 1


for chave, valor in agenda.items():
        print(chave, valor)
    



