#  EulerTask5 - Наименьшее кратное

# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
# Какое самое маленькое число делится нацело на все числа от 1 до 20?
def sep_num(number):
    """
    Функция раскладывающая число на простые множители в виде:
    {множитель1:количество раз которое встречается множитель1, множитель2:...},
    например - 12 -> 2 * 2 , 3 * 1  ->  {2: 2, 3: 1}
    :param number: целое число
    :return: словарь
    """
    lst_fact = []
    while number != 1:
        for factor in range(2, number + 1):
            if number % factor == 0:
                lst_fact.append(factor)
                number = int(number / factor)  # int необходимо чтобы числа можно было использовать в range()
                break
    d_fact = {}
    for factor in lst_fact:
        d_fact[factor] = lst_fact.count(factor)
    return d_fact


def get_numerator(max_num):
    """
    Функция, раскладывающая ряд чисел на общие множители
    :param max_num: целое число
    :return: минимальное число, которое делится нацело на все числа до числа max_num
    """
    d_fact = {}
    for num in range(1, max_num + 1):
        d_num = sep_num(num)
        for fact in d_num:
            if fact not in d_fact:
                d_fact[fact] = d_num[fact]
            elif fact in d_fact:
                d_fact[fact] = max(d_num[fact], d_fact[fact])
    s = 1
    for num in d_fact:
        s *= int(num) ** int(d_fact[num])
    return s


print(f"Cамое маленькое число, которое делится нацело на все числа от 1 до 10: {get_numerator(10)}")
print(f"Cамое маленькое число, которое делится нацело на все числа от 1 до 20: {get_numerator(20)}")
