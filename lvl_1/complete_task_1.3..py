while True:
    m = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    s = ''
    for i in range(3):
        s += input( f'Введите {i+1}-ю букву названия месяца: ' ).lower()
        indexes = [ i for i in range( len(m) ) if m[i].startswith(s[:3]) ]
        if len( indexes ) == 1 or indexes == [3-1, 5-1]:
            match indexes[0] + 1:
                case 4|6|9|11: print('30')
                case 2:        print('28 или 29')
                case _:        print('31')
            print()
            break
        if len( indexes ) == 0:
            s = ''
            print( 'Повторите ввод.' )
            print()
            break
