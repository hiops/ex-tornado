from app import XApplication
import wsgiref.simple_server

LISTEN_PORT = 8000


def wsgi_main():
    server = wsgiref.simple_server.make_server('', LISTEN_PORT, XApplication())
    server.serve_forever()


if __name__ == "__main__":
    wsgi_main()