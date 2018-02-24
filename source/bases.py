#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def _value_for_bit(bit):
    assert type(bit) is str

    key = [(i, s) for i, s in enumerate(string.printable)]

    for a_key in key:
        if a_key[1] == bit:
            return a_key[0]

    assert False, "bit, {}, is not represented in list of value, bit pairs\n{}".format(repr(bit), key)


def _bit_for_value(value):
    assert type(value) is int

    key = [(i, s) for i, s in enumerate(string.printable)]

    for a_key in key:
        if a_key[0] == value:
            return a_key[1]

    assert False, "bit, {}, is not represented in list of value, bit pairs\n{}".format(repr(value), key)


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    accumulator = 0
    for digit_place, a_bit in enumerate(digits[::-1]):
        accumulator += _value_for_bit(a_bit) * pow(base, digit_place)

    return accumulator


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    bit_to_value_list = []
    digit_place = 0
    while True:
        value = pow(base, digit_place)
        if value <= number:
            bit_to_value_list.append(value)
        else:
            break

        digit_place += 1

    encoded_bytes = ""
    digit_place = 1
    while digit_place < len(bit_to_value_list) +1:
        value_for_digit_place = bit_to_value_list[-digit_place]
        bit_value_to_add = base -1
        while True:
            digit_product = bit_value_to_add * value_for_digit_place
            if digit_product <= number:
                number -= digit_product
                encoded_bytes += _bit_for_value(bit_value_to_add)
                break
            else:
                bit_value_to_add -= 1

        digit_place += 1

    return encoded_bytes


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    number_10 = decode(digits, base1)
    converted_number = encode(number_10, base2)

    return converted_number


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
