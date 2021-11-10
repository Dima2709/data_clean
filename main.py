import pandas as pd

#1) прочитаем файл в переменную log

log = pd.read_csv('log.csv', header = None)

#2) добавим названия колонок user_id, time, bet, win;

log.columns = ['user_id', 'time', 'bet', 'win']

#5) уберём начальную скобку из поля time.

mass = []
mass1 = []
for i in log['time']:
    mass.append(i)

for i in mass:
    if type(i) == str:
        mass1.append(i[1:])
    else:
        mass1.append(i)
for i in range(len(mass1)):
    log['time'][i] = mass1[i]

#4) оставим в поле user_id значение типа: "user_N", где N значение идентификатора;

mass2 = []
for i in log['user_id']:
    mass2.append(i.split(' ')[-1])
for i in range(len(mass2)):
    log['user_id'][i] = mass2[i]

#3) удалим строки, которые содержат значения user_id с ошибками;

for i in range(len(log['user_id'])):
    if log['user_id'][i] == '#error':
        log.drop(labels = [i], axis = 0,inplace=True)
