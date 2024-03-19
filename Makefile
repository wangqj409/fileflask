dev: init
	flask  --app file run
.PHONY: dev

run: init
	gunicorn -w 4 -b 0.0.0.0  'file:app'
.PHONY: run

init:
	pip install Flask gunicorn