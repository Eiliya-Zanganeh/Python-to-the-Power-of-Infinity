pre = 0
crr = 1
idx = 0

while idx < 20:
    print(pre + crr, end='-')
    state = crr
    crr = pre + crr
    pre = state

    idx += 1
