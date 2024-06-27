# Пример использования стека типа LIFO


a = input('to check: ')
stack = []
fl_verify = True

for lt in a:
    if lt in '([{':
        stack.append(lt)
    elif lt in ')]}':
        if len(stack) == 0:
            fl_verify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        fl_verify = False
        break

if fl_verify and len(stack) == 0:
    print('Yes')
else:
    print('No')
