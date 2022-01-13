import datetime
from api.domainlayer.record.valueobject.watchdate import watchDate
from datetime import date, timedelta

def test_valid_value1():
    date = datetime.date.today()
    watchdate: watchDate = watchDate(date)
    
    assert watchdate is not None
    assert isinstance(watchdate, watchDate) == True

def test_valid_value2():
    date = datetime.date.today() - timedelta(days=1)
    watchdate: watchDate = watchDate(date)
    
    assert watchdate is not None
    assert isinstance(watchdate, watchDate) == True

# def test_typeerror_value():
#     typeerror_value: str = "aaaa"
#     watchdate: watchDate = watchDate(typeerror_value)


# def test_tomorrow():
#     tomorrow: date = date.today() + timedelta(days=1)
#     watchdate: watchDate = watchDate(tomorrow)
    