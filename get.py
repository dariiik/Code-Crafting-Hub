import tornado.web
import tornado.ioloop
import json
#get endpoint
class listRequestHandler(tornado.web):
    def get(self): 
        fh = open("list.txt", "r")
        #read all the files and split the array
        fruits = fh.read().splitlines()
        fh.close()
        #return as a json element
        self.write(json.dumps(fruits))
    
if __name__ == "__main__": 
    app = tornado.web.Application([
        (r"/list", listRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening onn port {port}")
    tornado.ioloop.IOLoop.current().start()
