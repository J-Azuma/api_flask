from logging import debug
import pytest
from api  import create_app
from api.database import init_db
import api

@pytest.fixture
def app():
    app = create_app()
    
  # 何も分からん
    with api.app.app_context():
        init_db(app)

    yield app 


@pytest.fixture
def client(app):
    return app.test_client()

  