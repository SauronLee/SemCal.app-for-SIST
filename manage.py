from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

app = Flask(__name__)
#env = os.environ.get("FLASK_ENV","develop")
app = create_app("develop")
#sCommand line argument
manager = Manager(app)
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()
