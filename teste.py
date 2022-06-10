
import os
import datetime as dt

os.system('cls')



start = input('pressione enter para começar!')
start_time = dt.datetime.now()
chars = input ('digite o mais rapido que puder! ')
end_time =  dt.datetime.now()


total_time = (end_time - start_time)
total_time = total_time.total_seconds()

CPS = len(chars)/total_time

wordlist = chars.split(' ')
total_time_m = total_time/60
WPS = len(wordlist)/total_time_m

print('---------------------------------------------------------------------')
print('Você digita '+ str(CPS)+ ' letras por segundo')
print('Você digita '+ str(WPS)+ ' palavras por minuto')
print('---------------------------------------------------------------------')