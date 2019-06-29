def studentDiscounts(x):
    return 0.9*x

def regularDiscounts(x):
    return 0.95*x

print(regularDiscounts(studentDiscounts(100)))

