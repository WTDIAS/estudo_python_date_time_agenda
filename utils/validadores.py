
from datetime import datetime


def gerar_chave():
    try:
        chave = datetime.now().strftime("%d%m%Y%H%M%S")        
        return chave
    except ValueError:
        return False

def valida_data(str_data):
    try:
        return datetime.strptime(str_data,"%d/%m/%Y").date()
    except ValueError:
        return False
    

def valida_hora(str_hora):
    try:
        return datetime.strptime(str_hora,"%H:%M").time()
    except ValueError:
        return False