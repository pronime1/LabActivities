def fibonacci(p):
    if p <=0:
        return "invalid"
    elif p ==1:
        return 0
    elif p ==2:
        return 1

    return fibonacci(p-1) + fibonacci(p-2)

if __name__ == "__main__":
    print(fibonacci(5))

