import tornado.web
import tornado.ioloop

class listRequestHandler(tornado.web)
    
if __name__ == "__main__": 
    app = tornado.web.Application([
        (r"/list", listRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening onn port {port}")
    tornado.ioloop.IOLoop.current().start()
