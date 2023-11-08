stack = []

def push():
    n = input("Введите элемент, который хотите добваить\n")
    stack.append(n)

def pop():
    stack.remove(stack[-1])

while True:
    print("\nВыберите функцию\n1. Добавить элемент в стек\n2. Извлечь элемент")
    choose = input()

    if choose == "1":
        push()
    elif choose == "2":
        if len(stack) == 0:
            print("Элементов больше не осталось")
            continue
        else:
            pop()
    else:
        continue

    print(stack)