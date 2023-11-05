def get_email_login_url(email):
    domain = email.split("@")[-1].lower()
    if domain == "yandex.com":
        return "https://mail.yandex.com"
    elif domain == "gmail.com":
        return "https://mail.google.com"
    else:
        return f"https://mail.{domain}"

email = input("Введите вашу почту: ")
login_url = get_email_login_url(email)
print(f"Ссылка для входа в почту: {login_url}")