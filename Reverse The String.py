def special_reverse_string(txt):
    out = ""
    reversedstring= txt[::-1].replace(" ","")
    for char in list(txt):
        if not char.isspace():
            if char.isupper():
                out+= reversedstring[0].upper()
            else:
                out+=reversedstring[0].lower()
            reversedstring = reversedstring[1:]
        else: out+=" "
    return out

def special_reverse_string2(txt):
  lst = [i for i in txt[::-1] if i != ' ']
  return ''.join(char if char == ' ' else lst.pop(0).upper() if char.isupper() else lst.pop(0).lower() for char in txt)


#print(special_reverse_string("Edabit"))
print(special_reverse_string('Hello World!'))