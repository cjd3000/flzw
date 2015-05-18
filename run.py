from flzw.app import get_app

if __name__ == '__main__':
    app = get_app()
    app.run(host='127.0.0.1', port=4348, ssl_context=('cert.pem','key.pem'), debug=True)
