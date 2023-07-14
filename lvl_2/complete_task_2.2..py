def quarter_of(month):
    match month:
        case 1 | 2 | 3:
            return '1 квартал'
        case 4 | 5 | 6:
            return '2 квартал '
        case 7 | 8 | 9:
            return '3 квартал'
        case 10 | 11 | 12:
            return '4 квартал'

month = float(input("Введите номер месяца: "))
print(quarter_of(month))
