#examplo list and tupla
mesesAno = ('Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
entrada = input('Digite sua data de nascimento com ex DD-MM-YYYY \n')
mesNascimento = int(entrada[3:5])-1
print('Você nasceu no mês ', mesesAno[mesNascimento])
