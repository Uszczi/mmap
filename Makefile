PROJ_PTH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
APP_PATH = src/map_app
LINT_PATHS = $(APP_PATH) tests

%:
	@:

lint:
	python -m autoflake --in-place --recursive --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables --remove-all-unused-imports $(LINT_PATHS)
	python -m black $(LINT_PATHS)
	python -m isort $(LINT_PATHS)
	python -m mypy $(APP_PATH) --ignore-missing-imports

run:
	cd ${APP_PATH}/web_app && uvicorn app:app --reload --lifespan=off --host 0.0.0.0 --port 8020

db-run:
	docker-compose -f docker/docker-compose.yml up -d

db-remove:
	docker rm -f database-map-app-db-1

cli:
	python ${APP_PATH}/cli/main.py $(filter-out $@,$(MAKECMDGOALS))

####################
### Dependencies ###
####################
compile-deps:
	python -m piptools compile --annotate --no-header  "requirements/dev.in"
	python -m piptools compile --annotate --no-header  "requirements/prod.in"


recompile-deps:
	python -m piptools compile --annotate --no-header  --upgrade "requirements/dev.in"
	python -m piptools compile --annotate --no-header  --upgrade "requirements/prod.in"


sync-deps:
	python -m pip install pip-tools
	python -m piptools sync "requirements/dev.txt"
	python -m pip install -e .


sync-deps-prod:
	python -m pip install pip-tools
	python -m piptools sync "requirements/prod.txt"
	python -m pip install -e .


##################
### Migrations ###
##################
makemigrations:
	cd ${APP_PATH}/models/alembic; alembic revision --autogenerate

migrate:
	cd ${APP_PATH}/models/alembic; alembic upgrade head
