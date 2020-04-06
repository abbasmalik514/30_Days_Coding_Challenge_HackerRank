S = input().strip()

try:
    integer = int(S)
    print(integer)
except ValueError:
    print('Bad String')
