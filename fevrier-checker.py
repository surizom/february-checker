import calendar

FEVRIER_MONTH = 2

def is_fevrier_square(annee):
    return (0, 28) == calendar.monthrange(annee, FEVRIER_MONTH)


for annee in range(2000, 3000):
    if is_fevrier_square(annee):
        print(annee)


