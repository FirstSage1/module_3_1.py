# Модуль 3_1 пространство имен.
# ==========================================
calls = 0
cort_str_ = (0)


def String_info(str_):  # Содание функции
    global cort_str_  # Объявление глоальной пер. внутри функции
    long_str_ = len(str_)
    hi_str_ = str_.upper()
    low_str_ = str_.lower()
    cort_str_ = (long_str_, hi_str_, low_str_)
    global calls
    calls += 1


String_info("Рубеж")
print(cort_str_)
String_info("Приход")
print(cort_str_)

flag_ = False


def is_contains(string, list_to_searh):
    global flag_
    flag_ = string in list_to_searh
    global calls
    calls += 1


is_contains('Добр', [24, 'Добр', 'добрый'])
print(flag_)
is_contains('Добр', [24, 'Добро', 'добрый'])
print(flag_)

print(calls)
