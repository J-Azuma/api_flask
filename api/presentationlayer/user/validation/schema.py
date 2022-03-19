
from typing import Final


create_schema: Final[dict] = {
    'email' : {
        'type' : 'string',
        'required' : True,
        'regex' : '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$',
        'empty': False
    },
    'password' : {
        'type' : 'string',
        'required' : True,
        'regex' : '\\A(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\\d)[a-zA-Z\\d]{8,30}\\Z', # 大文字小文字数字が必要
        'minlength' : 8,
        'maxlength' : 30,
        'empty': False
    }
}