# Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их пробелом,
# а также поменяет местами первые два символа первой строки на первые два символа второй строки и наоборот.

str_1 = 'Дай-ка угадаю, кто-то украл твой сладкий рулет?'
str_2 = 'Когда-то и меня вела дорога приключений, а потом мне прострелили колено'

# str_1_1 и str_2_1 переменные в в которых поменяли первые 2 символа
str_1_1 = str_1.replace(str_1[:2], str_2[:2])
str_2_1 = str_2.replace(str_2[:2], str_1[:2])

print(str_1_1 + ' ' + str_2_1)
