from app import create_app
from flask.ext.script import Manager

app = create_app()

manager = Manager(app)


@manager.command
def profile(length=25):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length])
    app.run()

if __name__ == '__main__':
    manager.run()

