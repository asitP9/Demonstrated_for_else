"""
Using for ... else in practice
Ensuring a list contains
at least one integer divisible by a given value

Are any of these numbers divisible by 12?
[2, 3, 25, 9]

No, so lets append a number that is
[2, 3, 25, 9, 12]
"""

if __name__ == '__main__':
    items=[2, 3, 25, 9]
    divisor=12

    for item in items:
        if item%divisor==0:
            found=item
            break
    else:                                       #nobreak
        items.append(divisor)
        found=divisor
    print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
