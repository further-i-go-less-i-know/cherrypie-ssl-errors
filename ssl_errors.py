
import cherrypy
from cherrypy.lib import static
import os

localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)

    
        
if __name__ == "__main__":
    #configuration stuff
    import os, os.path
    localDir = os.path.abspath(os.path.dirname(__file__))
    CA = '/home/user/folder1/server.crt'
    KEY = '/home/user/folder1/server.key'

    cherrypy.config.update({'server.socket_host': 'foobardomain.org','environment':'production','server.ssl_module': 'builtin',
        'server.socket_port': 8080, 'server.ssl_certificate': CA, 'server.ssl_private_key': KEY, 
        'request.show_tracebacks': False, 'tools.staticdir.root': '/home/user/folder', 'log.error_file': '/home/user/folder/cherrypy_errors.log', 
        'log.access_file': '/home/user/folder/cherrypy_access.log'
                       })
    from cherrypy.process.plugins import Daemonizer
    d = Daemonizer(cherrypy.engine)
    d.subscribe()

    conf = {
            '/static': {'tools.staticfile.on':True,'tools.staticfile.filename': '/home/user/folder/css/zen.css'},
           '/favicon.ico':
            {'tools.staticfile.on':True,'tools.staticfile.filename': '/home/user/folder/webbrowser-favorites.ico'},
            '/images':{'tools.staticdir.on':True, 'tools.staticdir.dir': 'images'}
            }

    cherrypy.quickstart(DownloadTwitter(), '/', config=conf)
