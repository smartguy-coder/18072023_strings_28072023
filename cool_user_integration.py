# from pywebio.input import input as pw_input
# from pywebio.input import NUMBER, PASSWORD, TEXT, DATETIME, COLOR
# from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast
#

import getpass

user_pass = getpass.getpass("Enter your password")
print(user_pass)



# user_name = pw_input('Enter your name').title()
# put_success(user_name)


# user_password = pw_input('Enter your password', type=PASSWORD)
# put_success(user_password)


# age = pw_input('Enter your age ', type=NUMBER)
# put_warning(age)
#
#
# date = pw_input('Enter your birthday', type=DATETIME)
# put_code(f'Your birthday is {date}\U0001F382')
# toast('tost')
# popup('popup', 'fffffffff')
# put_markdown('put markdown')

