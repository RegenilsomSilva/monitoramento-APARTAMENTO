
from datetime import datetime


Mostrando_o_horario_que_enviou  = datetime.now().strftime('%H:%M')
Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')

print(Mostrando_o_horario_que_enviou,'\n')
print(Mostra_a_data_do_ano,'\n')
print(f'Valores Atualizado as {Mostrando_o_horario_que_enviou} do Dia {Mostra_a_data_do_ano}')