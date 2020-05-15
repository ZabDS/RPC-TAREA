from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def suma(a,b):
        return int(a)+int(b)
    
    def resta(a,b):
        return int(a)-int(b)
    
    def mult(a,b):
        return int(a)*int(b)
    
    def div(a,b):
        if int(b) == 0:
            return "Math Error"
        else:
            return int(a)/int(b)
    
    server.register_function(suma, 'suma')
    server.register_function(resta, 'resta')
    server.register_function(mult, 'mult')
    server.register_function(div, 'div')
    
    server.serve_forever()