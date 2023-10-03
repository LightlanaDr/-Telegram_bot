import data_provided as dp
import model_operation as model
import logger as log

def click_button():
    value = int(input('Введите 1 - для операций с комплексными числами, 2 - для операций с рациональными числами: '))
    if value == 1:
        value_a = dp.input_comlex()
        value_b = dp.input_comlex()
    if value == 2:
        value_a = dp.input_data()
        value_b = dp.input_data()

    value_model = input('Введите значение операции: +, -, * или /: ')
    if value_model == '/':
        result = model.div(value_a, value_b)
        dp.view_data(result)
    if value_model == '+':
        result = model.sum(value_a, value_b)
        dp.view_data(result)
    if value_model == '*':
        result = model.mult(value_a, value_b)
        dp.view_data(result)
    if value_model == '-':
        result = model.sub(value_a, value_b)
        dp.view_data(result)

    log.nums_logger(value_a, value_b, value_model, result)