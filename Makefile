JS_LOC = /var/www/html/spires/includes/
CSS_LOC = $(JS_LOC)
CGI_LOC = /var/www/cgi-bin/

install:
	cp *.js $(JS_LOC)
	cp *.css $(CSS_LOC)
	sudo cp python/*.py $(CGI_LOC)