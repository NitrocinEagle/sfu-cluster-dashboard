import pyjsonrpc
import settings


class RequestHandler(pyjsonrpc.HttpRequestHandler):
    methods = settings.methods

# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address=('localhost', settings.PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://localhost:" + str(settings.PORT)
http_server.serve_forever()