.PHONY: all prepare-example run-example run-cmd

INFO_MSG = First, run the command: make prepare-example.\\nIt creates a database with an example form and also \
a superuser for access to the site administration. You would set your username and password.

all:
	@echo "make prepare-example"
	@echo "    It creates a database with an example form and also a superuser."
	@echo "make run-example"
	@echo "    Run example site."
	@echo "make run-cmd"
	@echo "    Run the Django Manager command. Example: make run-cmd cmd=shell"


prepare-example:
	cd example && ./manage.py migrate && ./manage.py loaddata data-forms.json && ./manage.py createsuperuser

run-example:
	@if [ ! -f example/dev.db ]; then \
		echo ${INFO_MSG}; \
	else \
		cd example && ./manage.py runserver; \
	fi

run-cmd:
	@if [ ! -f example/dev.db ]; then \
		echo ${INFO_MSG}; \
	else \
		cd example && ./manage.py ${cmd}; \
	fi
