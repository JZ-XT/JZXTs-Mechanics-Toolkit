def convert(kw):
    hp = kw / 0.745699872
    return hp

print('''
    JZXT's KW to HP Converter
''')
KW = input ('How Many KW? ')
hp = convert(int(KW))
print(str(KW) + ' KW is {0:.2f}'.format(hp) + ' HP')
