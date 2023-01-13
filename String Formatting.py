def print_formatted(number):
    for i in range(1,number+1):
        Decimal = i
        Octal = oct(i)
        Hexadecimal = hex(i)
        Binary = bin(i)
        print(f"{Decimal} {Octal} {Hexadecimal} {Binary}")
    # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)