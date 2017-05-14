from datetime import date


def main():
    born_before = date(1988,6,1)
    dates = prop()
    while dates is not None:
        if dates <= born_before:
            print('is at least 29 years old',date)

        dates = prop()


def prop():
    print('enter a birth date')
    month = int(input('month>>>'))

    if month == 0:
        return None

    else:
        year = int(input('year>>>'))
        day = int(input('day>>>'))

    return date(year,month,day)

main()
