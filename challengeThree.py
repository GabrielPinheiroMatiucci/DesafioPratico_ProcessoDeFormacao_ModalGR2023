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
            income = 0
            loan = 0
            print('Insira o seu salário atual: R$ ', end='')
            income = float(input().replace(',', '.'))

            while ((loan <= 0) or (loan > (income * 2))):
                print('Insira o valor desejado do empréstimo: R$ ', end='')
                loan = float(input().replace(',', '.'))

                if (loan > (income * 2)):
                    print('Empréstimo superior ao limite de 2 vezes o salário!\n')

            if (loan % 2 != 0):
                raise ValueError('')

            print('')
            invalidNumbers = False
        except ValueError:
            print('Insira um valor válido!\n')
    
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


def printNotes(notes: dict):
    index = 0
    for key, value in notes.items():
        if (value == 0):
            index += 1
            continue
        if ((index + 1) == len(notes.keys())):
            print(f"{value:.0f} X {key} reais.")
        else:
            print(f"{value:.0f} X {key} reais;")
        index += 1


def checkLoanEqualsSum(loan: float, sum: float):
    return loan == sum


def countGreaterNotes(loan: float):
    sum = 0
    notes = { 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0 }

    notes[100] = loan // 100
    sum += notes[100] * 100
    if checkLoanEqualsSum(loan, sum): return notes

    notes[50] = (loan - sum) // 50
    sum += notes[50] * 50
    if checkLoanEqualsSum(loan, sum): return notes

    notes[20] = (loan - sum) // 20
    sum += notes[20] * 20
    if checkLoanEqualsSum(loan, sum): return notes

    notes[10] = (loan - sum) // 10
    sum += notes[10] * 10
    if checkLoanEqualsSum(loan, sum): return notes

    if (((loan - sum) % 2) == 0):
        notes[2] = (loan - sum) // 2
        sum += notes[2] * 2
    
    if checkLoanEqualsSum(loan, sum): return notes

    notes[5] = (loan - sum) // 5
    sum += notes[5] * 5
    if checkLoanEqualsSum(loan, sum): return notes

    notes[2] = (loan - sum) // 2
    sum += notes[2] * 2
    return notes
    

def countLowerNotes(loan: float, greaterNotes: dict):
    sum = 0
    notes = { 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0 }

    notes[20] = greaterNotes[100] * 5 + greaterNotes[50] * 2
    notes[10] = greaterNotes[50]
    sum += notes[20] * 20
    sum += notes[10] * 10
    if checkLoanEqualsSum(loan, sum): return notes

    differenceTwentyNotes = (loan - sum) // 20
    notes[20] += differenceTwentyNotes
    sum += differenceTwentyNotes * 20
    if checkLoanEqualsSum(loan, sum): return notes

    differenceTenNotes = (loan - sum) // 10
    notes[10] += differenceTenNotes
    sum += differenceTenNotes * 10

    temporary = notes[10] // 2
    notes[20] += temporary
    notes[10] -= (temporary * 2)
    if checkLoanEqualsSum(loan, sum): return notes

    if (((loan - sum) % 2) == 0):
        notes[2] = (loan - sum) // 2
        sum += notes[2] * 2
    
    if checkLoanEqualsSum(loan, sum): return notes

    notes[5] = (loan - sum) // 5
    sum += notes[5] * 5
    if checkLoanEqualsSum(loan, sum): return notes

    notes[2] = (loan - sum) // 2
    sum += notes[2] * 2
    return notes


def countMixedNotes(loan: float):
    notes = { 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0 }
    gNotes = countGreaterNotes(loan / 2)
    lNotes = countLowerNotes((loan / 2), gNotes)

    for lNote, gNote in zip(lNotes.items(), gNotes.items()):
        notes[lNote[0]] += lNote[1]
        notes[gNote[0]] += gNote[1]

    temporary = notes[5] // 2
    notes[10] += temporary
    notes[5] -= (temporary * 2)

    temporary = notes[10] // 2
    notes[20] += temporary
    notes[10] -= (temporary * 2)

    return notes


def solutionChallengeThree():
    name, admissionDate, income, loan = inputValues()

    if ((((date.today() - admissionDate).days) / 365) <= 5):
        print('Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.')
    else:
        print('Opções de retirada do empréstimo')
        print('Notas de maior valor:')
        greaterNotes = countGreaterNotes(loan)
        printNotes(greaterNotes)
        print('')
        print('Notas de menor valor:')
        lowerNotes = countLowerNotes(loan, greaterNotes)
        printNotes(lowerNotes)
        print('')
        print('Notas meio a meio:')
        mixedNotes = countMixedNotes(loan)
        printNotes(mixedNotes)
