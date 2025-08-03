from datetime import datetime, date, time
class Compromisso:
    def __init__(self, descricao:str, data:date, hora:time):
        self.descricao  = descricao
        self.data = data
        self.hora = hora

    def __str__(self):
        str_data = self.data.strftime("%d/%m/%Y")
        str_hora = self.hora.strftime("%H:%M")
        return f"Descrição: {self.descricao} Data: {str_data} Hora: {str_hora}"