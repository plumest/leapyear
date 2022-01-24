
def leapyear(number: int) -> bool:
    if not (number % 400):
        return True

    elif not (number % 4) and (number % 100):
        return True

    else:
        return False
