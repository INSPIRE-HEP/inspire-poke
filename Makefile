JS_LOC = /var/www/html/spires/includes/
JS_LOC = /afs/slac/www/spires/includes/
CSS_LOC = $(JS_LOC)
CGI_LOC = /var/www/cgi-bin/
SPIRES_LOC = /var/www/html/spires/find/
SPIRES_LOC = /afs/slac/www/spires/find/

install: install-web install-cgi

install-web:
	cp *.js $(JS_LOC)
	cp *.css $(CSS_LOC)
	cp header.html $(SPIRES_LOC)
install-cgi:
	sudo cp python/*.py $(CGI_LOC)
