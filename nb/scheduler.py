import tornado.web


class Scheduler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, Test!")
        self.render('scheduler-background.html')
