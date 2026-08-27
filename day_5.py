empty_list = []
fruits = ['apple', 'banana', 'lemon', 'durian', 'santol']
print(len(fruits))
print(fruits[0])
print(fruits[2])
print(fruits[-1])

it_company = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_company)
print(len(it_company))
it_company.insert(3, 'Twitter') 
print(it_company)
it_company.append('Tesla')
print(it_company)
it_company.insert(5, 'Meta')
print(it_company)
print([company.upper() for company in it_company if company == 'Facebook'])

if 'Google' in it_company:
    print('Google is in the list')

it_company.reverse()
print(it_company)


#SKIP TO LEVEL 2 EXERCISES I ALREADY DID MANY IN GEMINI GEM

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
ages.append(min(ages))
ages.append(max(ages))
median_age = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
print('Median age:', median_age)
average_age = sum(ages) / len(ages)
print('Average age:', average_age)      

diff_1 = abs(min(ages) - average_age)
diff_2 =abs(max(ages) - average_age)

if diff_1 > diff_2 :
    print('diff 1 is greater')
    

