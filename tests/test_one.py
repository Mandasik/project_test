from capitalizers.capitalizer.func import get_function

get = get_function()

test_glossary = {1: 'd', 6: 'b'}
if get(test_glossary, 1, 'gay') != 'd':
    raise Exception('функция не находит существующий ключ')

if get(test_glossary, 4, 'gay') != 'gay':
    raise Exception('функция не использует значение по умолчанию')

if get({}, 4, 'gay') != 'gay':
    raise Exception('Функция не работает')

print('Всё работает')