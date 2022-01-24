
def leapyear(number: int) -> bool:
    if not (number % 400):
        return True

    if not (number % 100):
        return False

    if not (number % 4):
        return True
    return False
