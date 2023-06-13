from data_manager import DataManager

dm = DataManager()
name = input('What is your first name?\n')
surname = input('What is your last name?\n')
email = input('What is your email?\n')
check = input('Type email again.\n')


while email != check:
    print('Emails do not match.')
    email = input('What is your email?\n')
    check = input('Type email again.\n')

if email == check and not dm.check_email(email):
    dm.post_new_user(name, surname, email)
    print("You're in the club!")
else:
    print('Already a user.')
    #