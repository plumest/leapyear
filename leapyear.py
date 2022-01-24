
def leapyear(number: int) -> bool:
    if not (number % 400):
        return True

    elif (number % 4 == 0) and (number % 100 != 0):
        return True

    else:
        return False
