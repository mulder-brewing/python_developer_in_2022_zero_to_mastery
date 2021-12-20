# importing date class from datetime module
from datetime import date

birth_year = input('what year were you born?')
age = date.today().year - int(birth_year)
print(f'your age is {age}')
