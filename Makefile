pgadmin:
	pipenv run gunicorn --bind 10.0.1.7:5050 --workers=1 --threads=25 --chdir $$(PIPENV_VERBOSITY=-1 pipenv --venv)/lib/python3.8/site-packages/pgadmin4/ pgAdmin4:app
pgadmin-p:
	pipenv run gunicorn -p $$(pwd)/.vscode/pgadmin-d.pid --bind 10.0.1.7:5050 --workers=1 --threads=25 --chdir $$(PIPENV_VERBOSITY=-1 pipenv --venv)/lib/python3.8/site-packages/pgadmin4/ pgAdmin4:app
django:
	pipenv run ./manage.py runserver 10.0.1.7:8989
django-d:
	nohup make django > .vscode/django-d.out 2> .vscode/django-d.err < /dev/null & echo $$! > .vscode/django-d.pid
pgadmin-d:
	nohup make pgadmin-p > .vscode/pgadmin-d.out 2> .vscode/pgadmin-d.err < /dev/null &
stop-django-d:
	kill $$(cat .vscode/django-d.pid)
stop-pgadmin-d:
	kill $$(cat .vscode/pgadmin-d.pid)