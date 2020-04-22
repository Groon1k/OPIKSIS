import random


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    message = ''
    for z in range(len(text)):
        symbol = text[z]
        bits = bin(int.from_bytes(symbol.encode(encoding, errors), 'big'))[2:]
        # print('text =', bits)
        message += bits
    return message


def check(q, l):  # проверка на является ли число степенью двойки
    for j in range(l):
        if q == 2 ** j:
            return 1


def inequality(n):  # решение неравенства
    K = 0
    while 2 ** K <= (K + n + 1):
        K += 1
    return K


def append_control_bits(text_without_zero, num_of_control_bits, n_k):  # добавление контрольных битов
    ham = []  # задаю массив, в оторый далее запишется код и контрольные биты
    p = 0  # переменная для чистого счётчика
    ind_of_control_bits = []
    for i in range(n_k):
        if check(i + 1, num_of_control_bits) == 1:
            ham.append(0)  # добавление контрольного бита
            ind_of_control_bits.append(i)
        else:
            ham.append(text_without_zero[p])  # если проверка не проходит, то добавляем символ из сообщения
            p += 1
        # print(ham, 'iteration', i)
    return ham, ind_of_control_bits


def power_count(
        ham_control_bits):  # подсчёт количества степеней, подаю на вход функции сообщение с нулями на местах контрольных битов, ибо они ещё не расчитаны
    amount = [int(0) for j in range(len(bin(len(ham_control_bits))[
                                        2:]))]  # заполняю список таким количеством нулей, какова максимальная степень двойки, которая встречается
    for i in range(len(ham_control_bits)):  # хочу пройтись посимвольно по строке
        for j in range(len(bin(i + 1)[2:])):
            m = bin(i + 1)[2:]  # представляю i-е число в двоичном виде
            m = m[::-1]  # реверс для того, чтобы начинать с 1 степени
            if m[j] == '1' and ham_control_bits[
                i] == '1':  # если есть j степень, то добавляем 1 к количеству вхождений степеней
                amount[j] += 1
    # print(amount)
    return amount  # количество единиц. которые контролирует каждый контрольный бит


def change_con_bits(am, index, all_message):  # замена контрольных битов
    for w in range(len(am)):  # прохожусь по элементам списка с количеством вхождений степеней от 0 и далее
        if am[w] % 2 == 0:  # если число делится на 2 без остатка, т.е чётное
            i = index[w]
            # print('индекс бита, который нужно заменить', i)
            all_message[i] = '0'  # меняю контрольный бит на '0'
            # print(all_message)
        else:
            all_message[index[w]] = '1'  # меняю на '1'
    return all_message


def change(some, p):
    if some[p] == '0':
        some[p] = '1'
    else:
        some[p] = '0'
    return some


def rand_change(mes, inexxx):  # подаю инф сообщение с битами
    ran = random.randint(inexxx[len(inexxx) - 2] + 1,
                         inexxx[len(inexxx) - 1] - 1)  # выбираю рандомный элемент, чтобы изменить его
    print(ran, 'номер ошибки')
    mes_with_mis = []
    mes_with_mis.extend(mes)
    change(mes_with_mis, ran)   # заменяю рандомный элемент на '1' или '0'
    message = []
    message.extend(mes_with_mis)
    #print(mes_with_mis, 'сообщение с ошибкой')
    for i in inexxx:
        mes_with_mis[i] = '0'
    return mes_with_mis, message


def find_mistake(mes_mistake, mes_without_mistake, index, mes_for_change):  # поиск разницы в контр. битах и исправление ошибок
    j = 0
    for i in index:
        if mes_mistake[i] != mes_without_mistake[i]:
            j += i + 1
    print('ошибка в бите пол номером:', j)
    change(mes_for_change, j - 1)
    print(mes_for_change, 'окончательный результат, сообщение с исправленной ошибкой')


text = text_to_bits(input())
print(text, 'закодированное сообщение')
k = inequality(len(text))
long = k + len(text)
print('k =', k)
print('n + k =', long)
ham_with_control_bits, indecies_of_control_bits = append_control_bits(text, k, long)
print(ham_with_control_bits, 'сообщение с нулевыми контрольными битами')
amount_degrees = power_count(ham_with_control_bits)  # количество вхождений степеней
mes_with_comp_con_bits = change_con_bits(amount_degrees, indecies_of_control_bits,
                                         ham_with_control_bits)  # замена контрольных битов на '0' или '1'
print(mes_with_comp_con_bits, 'сообщение без ошибки с расчитаными контрольными битами')
message_with_mistake, mes = rand_change(mes_with_comp_con_bits, indecies_of_control_bits)  # сообщение с ошибкой
print(mes, 'сообщение с ошибкой')
print(message_with_mistake, 'сообщение с ошибкой с нулевыми котрольными битами')
amount_degrees_on_mistake = power_count(
    message_with_mistake)  # количество единиц, которые контролирует сообщение с ошибками
calc_control_bits_on_mes = change_con_bits(amount_degrees_on_mistake, indecies_of_control_bits,
                                           message_with_mistake)  # сообщение с ошибкой и подсчитаными контрольными битами
print('amount', amount_degrees_on_mistake)
print(calc_control_bits_on_mes, 'сообщение с ошибкой, с расчитанными контрольными битами')
find_mistake(calc_control_bits_on_mes, mes_with_comp_con_bits, indecies_of_control_bits, mes)
