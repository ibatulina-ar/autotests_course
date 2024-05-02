# Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.

print('D:\AQA_task\idea\main.exe')

route = 'D:\AQA_task\idea\main.exe'

# находим индекс точки
delete = route.find('.')

# делаем срез до точки и разделяем строку по \
route_list = (route[:delete].split('\\'))

print(f'Диск - {route_list[0]}. Корневая папка - {route_list[1]}. Название файла - {route_list[-1]}')
