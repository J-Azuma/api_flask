## flaskの起動用ファイル
from api import app

if __name__ == '__main__':
    app.run(debug=False)