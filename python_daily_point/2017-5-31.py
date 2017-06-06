import random
import string

def gen_cookie():

    ascii_le = string.ascii_letters
    digits = string.digits

    str_dir = ascii_le+digits
    lst_dir = list(str_dir*10)

    cookie = ''.join(random.sample(lst_dir,10))

    return cookie
    # pass


print(gen_cookie())
