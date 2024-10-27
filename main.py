from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
d.appendleft(-1)
print(d)

print(d.pop())
print(d.pop())
print(d.pop())
print(d)

d.extend([8, 8, 8])
d.extendleft([1, 2, 3])
print(d)

d.clear()
print(d)

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(f"Стек последобавления элементов - {stack}")

print(f"удаление элемента {stack.pop()}")
print(f"удаление элемента {stack.pop()}")

print(stack)

































def validate(s):
    # Создаем стек на основе deque() для эфктивности 
    stack = deque()
    # Создаем словарь ключ_значения с скобками для отслеживания правильности
    br = {")": "(", "[": "]", "}": "{}"}
    # перебираем каждую скобку из "s"
    for char in s:
        # если скобка является открывающей
        if char in br.values():
            # добавляем в стек
            stack.append(char)
            # если скобка является закрывающей
        elif char in br.keys():
            # если стак пустой или скобка не
            # правильная по отношению к последнейв стеке
            if not stack or stack.pop() != br[char]:
                # возвращаяем false
                return False
    
    # если стек пустой после проверки возврощаем true
    return not stack
print(validate("({[]})"))
print(validate("({[}"))