# Модуль логирования

from datetime import datetime as dt

def nums_logger(num1, num2, operation, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time} {num1} {operation} {num2} = {result} \n')