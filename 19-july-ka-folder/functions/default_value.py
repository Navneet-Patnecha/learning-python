def generate_passwd(username , password):

    username = username[:4]
    password = password[-4:]

    value = username + password
    return value

last_pass = generate_passwd('navneet', '1234567')
print(last_pass)





