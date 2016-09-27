# coding=utf-8

# 26.09.16

# 2
###############################################################################

def handle():
    k, b, x = 1, 7, 4

    key = input('Введите имя переменной (k, b) или число \n')e
    
    if key.isdigit():
        calc(k, b, int(key))
    
    elif key == 'k':
        k = input('Введите значение k: ')
        if k.isdigit():
            k = int(k)
            calc(k, b, x)

    elif key == 'b':
        b = input('Введите значение k: ')
        if b.isdigit():
            b = int(b)
            calc(k, b, x)        
    else:
        print('Некорректный ввод')
        handle()

def calc(k, b, x):
    res = k*x + b
    print('Результат: ', res, '\n')
    handle()

if __name__ == '__main__':
    handle()