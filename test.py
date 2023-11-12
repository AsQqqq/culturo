from database.decorators import get_testing

if not get_testing(login="danila"):
    print("1")
else:
    print("2")