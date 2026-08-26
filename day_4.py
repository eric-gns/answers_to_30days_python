# EXERCISES!

a = 'thirty'
b = 'days'
c = 'of'
d = 'python'

concatenated_string = a + ' ' + b + ' ' + c + ' ' + d
print(concatenated_string)

e = 'Coding'
f = 'for'
g = 'all'

concatenated_string_2 = e + ' ' + f + ' ' + g
print(concatenated_string_2)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

slice = company[:: 5]
print(slice)

sub_string = 'Coding'
print(company.find(sub_string))

print(company.replace('Coding' , 'Python'))

print(company[10])

abbreviation = company[0] + company[7] + company[11]
print('abbreviation: ' +abbreviation)

print(company.index('C'))
print(company.index('F'))

print(company.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))
print(sentence[31:54])
print(sentence.index('because'))

substring = 'Coding'
print(sentence.startswith(substring))
print(sentence.endswith(substring))

substring2 = '   Coding For All      '
print(substring2.strip())

libraries = 'Django, Flask, Bottle, Pyramid, Falcon'
print('# '.join(libraries.split(', ')))

sentence2 = 'I am enjoying this challenge.\n I just wonder what\n is next.'
print(sentence2)


tab_escape = 'Name\t Age\t Country\t City\n Asabeneh\t 250\t Finland\t Helsinki'
print(tab_escape)

radius = 10
pi = 3.14
float(pi)
area_of_circle = pi * radius ** 2

print('radius = {radius} \narea = {pi} * radius ** 2 \n the area of the circle with radius 10 is {area_of_circle}'.format(radius=radius, pi=pi, area_of_circle=area_of_circle))
    
l = 8
m = 6
int(l)
int(m)
sum = l + m
diff = l - m
product = l * m
division = l / m
floor_division = l // m
exponent = l ** m

print('{l} + {m} = {sum}\n{l} - {m} = {diff:.2f}\n{l} * {m} = {product}\n{l} / {m} = {division:.2f}\n{l} // {m} = {floor_division}\n{l} ** {m} = {exponent}'.format(l=l, m=m, sum=sum, diff=diff, product=product, division=division, floor_division=floor_division, exponent=exponent))



