
from typing import Final


create_schema: Final[dict] = {
    'email' : {
        'type' : 'string',
        'required' : True
    },
    'password' : {
        'type' : 'string',
        'required' : True,
        'min' : 8,
        'max' : 30
    }
}