#!/usr/bin/env python3

# perform a ROTn encoding
def rot_n(plain_text, shift_by):
    rot_text = ""
    if shift_by > 26:
        shift_by -= 26
    elif shift_by < -26:
        shift_by += 26
    for char in plain_text:
        if char.isalpha():
            if ord(char) >= 65 and ord(char) <= 90: #65-90 Uppercase
                rotchar = ord(char) + shift_by
                if rotchar > 90:
                    rotchar -= 26
                elif rotchar < 65:
                    rotchar += 26
            else: # 97-122
                rotchar = ord(char) + shift_by
                if rotchar > 122:
                    rotchar -= 26
                elif rotchar < 97:
                    rotchar += 26
            rot_text = rot_text + chr(rotchar)
        else:
            rot_text = rot_text + str(char)
    return rot_text

print(rot_n("abC###", 24))

