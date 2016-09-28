# coding=utf-8

def to_fahrenheit(value):
    try:
        return float(value) * 1.8 + 32
    except ValueError as e:
        print(e)
        return None


def to_celsius(value):
    try:
        return float(value - 32) * 0.556
    except ValueError as e:
        print(e)
        return None


def is_number(str_value):
    try:
        float(str_value)
        return True
    except ValueError as e:
        print(e)
        return False


# температура не может быть меньше абсолютного нуля
def is_valid_temperature(value, scale):
    try:
        value = float(value)
    except ValueError as e:
        print(e)
        return None

    if scale == 'c':
        return value >= -273.15
    elif scale == 'f':
        return value >= to_fahrenheit(-273.15)
    
    print('Invalid scale.')
    return None


def handle():
    scale = input('Выберите шкалу температуры нажав C или F: ').lower()
    if scale not in ['c', 'f']:
        print('Некорректный выбор шкалы. Повторите ввод.')
        handle()

    SCALE_MESSAGE = {
        'f': 'Выбрана шкала Фаренгейта',
        'c': 'Выбрана шкала Цельсия' 
    }
    print(SCALE_MESSAGE[scale]) # вывод сообщения об успешном выборе

    valid = False
    values = []

    # собираем ввод пока не получим валидный
    while not valid:
        values = [
            token for token in input(
                'Последовательно введите 4 значения температуры, ' 
                'разделяя их пробелами: \n')
            .replace(',', '.') # дробные числа можно вводить используя ','
            .split() 
        ]

        valid = values \
            and len(values) == 4 \
            and all(is_number(token) for token in values) \
            and all(is_valid_temperature(token, scale) for token in values)
        
        if not valid:
            print('Некорректный ввод значений. Повторите ввод.')

    numeric_values = (float(v) for v in values)

    average = sum(numeric_values) / len(values)

    if scale == 'c':
        average_celsius = average
        average_fahrenheit = to_fahrenheit(average)
    else:
        average_fahrenheit = average
        average_celsius = to_celsius(average)       
    
    results = (
        'Средняя температура по Цельсию: {c} \n'
        'Средняя температура по Фаренгейту: {f} \n').format(
            c=round(average_celsius, 2), f=round(average_fahrenheit, 2))

    print(results)

    if input('Рассчитать снова? (введите yes) ').lower() == 'yes':
        handle()


if __name__ == '__main__':
    handle()
