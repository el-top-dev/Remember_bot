import datetime
from dataclasses import dataclass


@dataclass
class Base_user_information:
    username: str
    sing_up_date: datetime.datetime
    is_using_status: bool


if __name__ == '__main__':
    t1 = Base_user_information(username=12, sing_up_date=datetime.datetime.now(), is_using_status=True)
    print(type(t1.username))

