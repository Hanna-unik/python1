revenue = float(input('Введите значение выручки фирмы: '))
cost = float(input('Введите значение издержки фирмы: '))
profit = revenue - cost
print (' ', profit)
if revenue > cost:
        print ('вы работаете правильно, с прибылью')
        print ('рентабельность выручки - %5s' % (profit / revenue))
        staff = int(input('Сколько человек трудится на фирме?: '))
        print (f'прибыль в расчете на 1 сотрудника составила: {profit / staff:.2f}')
else:
        print('необходимо работать усерднее, вы работаете в убыток')
