first_name = 'Taylor'
print(first_name)

last_name = 'Galbraith'
print(last_name)

age = 27 # int
bank_account = 42933.23 #float 
loves_code = True #bool


# age= "twenty-seven"
print(age)
# print(type(age))

if age >= 18:
    print('I am an adult')

elif age > 13:
    print('im a teen')

else:
    print('im a baby')

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(number)

film_list = ['rED', 'black Magic', 'arri']

for film in film_list:
    print(film.capitalize())

open_file = open("FinalGrades.csv")

# for row in open_file:
#     print(row)


for row in open_file:
    row = row.split(',')
    for value in row:
        if value.startswith('R'):
            print(value)





open_file.close()

