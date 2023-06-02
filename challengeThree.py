from datetime import date

def inputDate():
    admissionDate = ''
    while len(admissionDate) != 3:
        try:
            print('Insira a data de admissão (dd/mm/aaaa): ', end='')
            admissionDate = [int(value) for value in input().split('/')]

            if (not (1 <= admissionDate[0] <= 31)):
                raise ValueError('')
            if (not (1 <= admissionDate[1] <= 12)):
                raise ValueError('')
            if (admissionDate[2] < 1000):
                raise ValueError('')
        except ValueError:
            print('Digite uma data válida')
            admissionDate = ''
        except IndexError:
            print('Digite uma data válida')
            admissionDate = ''
    
    return date(day=admissionDate[0], month=admissionDate[1], year=admissionDate[2])


def inputNumbers():
    invalidNumbers = True
    while invalidNumbers:
        try:
            print('Insira o seu salário atual: R$ ', end='')
            income = float(input().replace(',', '.'))
            print('Insira o valor desejado do empréstimo: R$ ', end='')
            loan = float(input().replace(',', '.'))
            print('')
            invalidNumbers = False
        except:
            print('Digite valores válidos')
    
    return [income, loan]


def inputValues():
    name = ''
    admissionDate = ''
    income = 0
    loan = 0

    print('Insira o seu nome: ', end='')
    name = input()

    admissionDate = inputDate()
    income, loan = inputNumbers()

    return [name, admissionDate, income, loan]


def solutionChallengeThree():
    name, admissionDate, income, loan = inputValues()
    print(admissionDate)

    