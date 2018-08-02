import tornado
import os

from nb.scheduler import Scheduler


def makeapp():
    #ToDo: Integrate subfolder support for template Rendering
    dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmp_template_path = dirpath + '/basic-html-pages/scheduler-background'
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
