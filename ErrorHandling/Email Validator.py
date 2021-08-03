from ErrorHandling.custom_exceptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError
from ErrorHandling.helpers import valid_domain_extensions
email = input()

def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")
    try:
        name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in valid_domain_extensions:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    return True

while email != "End":
    if valid_email(email):
        print("Email is valid")
    email = input()
