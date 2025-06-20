up:
	docker-compose up -d

down:
	docker-compose down

install:
	pip install --no-cache-dir -r requirements.txt

run-load-raw:
	PYTHONPATH=$$(pwd) python pipeline_beam/landing_to_raw.py

run-load-trusted:
	PYTHONPATH=$$(pwd) python pipeline_beam/raw_to_trusted.py

run-load-refined:
	PYTHONPATH=$$(pwd) python pipeline_beam/trusted_to_refined.py

run-gcs-landing-to-raw:
	PYTHONPATH=$$(pwd) python utils/gcs/landing_to_raw.py

run-gcs-raw-to-trusted:
	PYTHONPATH=$$(pwd) python utils/gcs/raw_to_trusted.py

run-gcs-trusted-to-refined:
	PYTHONPATH=$$(pwd) python utils/gcs/trusted_to_refined.py

run-postgres-generate:
	PYTHONPATH=$$(pwd) python utils/postgres/main.py

export-python-path:
	export PYTHONPATH="$${PYTHONPATH}:$$(pwd)"

help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  up 						- Start the Docker containers"
	@echo "  down 						- Stop the Docker containers"
	@echo "  install 					- Install the dependencies"
	@echo "  run-load-raw 				- Run the landing to raw pipeline (BEAM)"
	@echo "  run-load-trusted 			- Run the raw to trusted pipeline (BEAM)"
	@echo "  run-load-refined 			- Run the trusted to refined pipeline (BEAM)"
	@echo "  run-gcs-landing-to-raw 	- Run the GCS landing to raw pipeline (GCS)"
	@echo "  run-gcs-raw-to-trusted 	- Run the GCS raw to trusted pipeline (GCS)"
	@echo "  run-gcs-trusted-to-refined - Run the GCS trusted to refined pipeline (GCS)"
	@echo "  run-postgres-generate 		- Run the postgres container (POSTGRES)"
	@echo "  export-python-path 		- Export the Python path"
