
VENV=venv

all: $(VENV) cert

$(VENV):	requirements.txt
	virtualenv $@
	$@/bin/pip install --upgrade pip
	$@/bin/pip install -r requirements.txt

cert: cert.pem key.pem

cert.pem key.pem:
	openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -nodes -subj \
            "/C=US/ST=State/L=Location/O=OrgName/OU=OrgUnit/CN=example.com"
.PHONY:	clean
clean:
	rm -f cert.pem key.pem
	rm -rf $(VENV)
