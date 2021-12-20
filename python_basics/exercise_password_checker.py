username = input('username?')
password = input('password?')

password_length = len(password)
password_obfuscated = '*' * password_length
print(f'{username}, your password {password_obfuscated} is {password_length} letters long')
