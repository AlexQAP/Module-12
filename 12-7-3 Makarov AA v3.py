per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print ("Ставки по депозитам, %:", per_cent)
money = int(input('Введите сумму депозита: '))
TKB = int((per_cent['ТКБ']) * (money/100))
SKB = int((per_cent['СКБ']) * (money/100))
VTB = int((per_cent['ВТБ']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))
deposit = {'ТКБ': TKB,'СКБ': SKB, 'ВТБ': VTB, 'СБЕР': SBER}
deposit_max = [TKB, SKB, VTB, SBER]
print ("Средства, накопленные за 1 год, руб.:", deposit)
print ("Максимальная сумма, которую вы можете заработать, руб.:", max(deposit_max))