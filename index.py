#only for starting the server
import tornado.web
import tornado.ioloop #waits for the request
#get method
class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is a python command.")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])
    port = 8882
    app.listen(port)
    print(f"Application is ready annd listening on port {port}")

    tornado.ioloop.IOLoop.current().start()

