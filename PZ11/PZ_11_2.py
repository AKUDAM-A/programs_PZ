import string

text = "CTpoka - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."


def digits_only(s):
    for ch in s:
        if ch in string.digits:
            yield ch


print("Исходная строка:")
print(text)

print("\nЦифры в строке:")
print("".join(digits_only(text)))
