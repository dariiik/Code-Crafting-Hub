import tornado.web
import tornado.ioloop 
import psycopg2
import json 

class getHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("stateless.html")

class statelessHandler(tornado.web.RequestHandler):
    def post(self):
        con = psycopg2.connect(
            host = "darigamac", 
            database = "darigaid", 
            user = "postgres", 
            password = "postgres"
        )

        cur = con.cursor()

        cur.execute("select id, name from profiles where id = 362")

        rows = cur.fetchall()

        cur.close()
        con.close()

        self.set_header("content-type", "application/json")
        self.write(json.dumps(rows[0]))

    
    if (__name__ == "__main__"): 
        app = tornado.web.Application([
            ("/stateless", getHandler), 
            ("/stateless/read", statelessHandler)
        ])
