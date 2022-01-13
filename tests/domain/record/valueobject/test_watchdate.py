import pytest
from api.domainlayer.record.valueobject.watchdate import watchDate
from datetime import datetime, date, timedelta
from pytest import raises

def test_valid_value1():
    date = datetime.today()
    watchdate: watchDate = watchDate(date)
    
    assert watchdate is not None
    assert isinstance(watchdate, watchDate) == True

def test_valid_value2():
    date = datetime.today() - timedelta(days=1)
    watchdate: watchDate = watchDate(date)
    
    assert watchdate is not None
    assert isinstance(watchdate, watchDate) == True

def test_typeerror_value():
    typeerror_value: str = "aaaa"
    
    with raises(TypeError) as e:    
        watchdate: watchDate = watchDate(typeerror_value)
    
    assert str(e.value) == "日付を入力してください"


def test_valueerror_value():
    tomorrow: datetime = datetime.today() + timedelta(days=1)
    with raises(ValueError) as e:
        watchdate: watchDate = watchDate(tomorrow)
    assert str(e.value) == "明日以降の日時は選択できません。"