# Merkkijonoliteraalit

print('O"reilly')
print("O'reilly")
print('''O'reilly''')
print('''Oh'"Really''')

print("tab\ttab\tline\nand new\nline")

print(" C:\temp\test.py")
print(" C:\\temp\\test.py")
print(r"Raw: C:\temp\test.py")

utf_str = 'A\u00c4B\U000000e8C'
print(utf_str)
print(len(utf_str))

multiline_str = '''This is a example string with embedded newlines.
Known as a tripled-quoted string.
    Whitespace are included
so the above line is indented with whitespaces.

'''
print(multiline_str)

skandit = "åäö ja ÅÄÖ"
print("Bytes:", skandit.encode('utf-8'))
print(skandit.encode('utf-8').decode('utf-8'))

print(len(skandit))
print(len(skandit.encode('utf-8')))
