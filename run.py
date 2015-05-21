from flzw.app import get_app

if __name__ == '__main__':
    app = get_app()
    app.config.from_envvar('FLZW_CFG')
    app.run(host='0.0.0.0', port=4348, ssl_context=('cert.pem', 'key.pem'), debug=True)
