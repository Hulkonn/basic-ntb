import tornado

from pathlib import Path
from nb.scheduler import Scheduler


def makeapp():
    #ToDo: Integrate subfolder support for template Rendering
    tmp_template_path = Path().resolve() / 'basic-html-pages' / 'scheduler-background'
    settings = dict(
        template_path=str(tmp_template_path)
    )
    app = tornado.web.Application([
        (r"/", Scheduler),
    ],
    **settings)
    return app


def main():
    app = makeapp()
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(16161, 'localhost')
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
