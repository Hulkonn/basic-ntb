import tornado

from nb.scheduler import Scheduler


def makeapp():
    app = tornado.web.Application([
        (r"/", Scheduler),
    ])
    return app


def main():
    app = makeapp()
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(16161, 'localhost')
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
