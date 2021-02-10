# Решение для 1 слова
# def int_func(*args):
#     word = input("Введите слово ")
#     if word.isascii() == False or word.isalpha() == False:
#         print('Введены невернын значения')
#     else:
#         print(word.title())
#     return
# int_func()


# Решение для нескольких
def int_func():
    line = input('Введите слова через пробел ').lower()
    if all(96 < ord(let) < 123 or ord(let) == 32 for let in line):
        return line.title()
    else:
        return 'введены неверные даные'
print(int_func())
