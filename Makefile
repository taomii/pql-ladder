build:
	docker-compose up --build
buildd:
	docker-compose up --build -d
run:
	python3 poller/main.py
kill:
	docker container rm -f $$(docker ps -aq)
poller:
	docker-compose start poller --no-cache
connect-db:
	docker exec -ti charly-db bash
connect-poller:
	docker exec -ti charly-poller bash
clean docker:
	docker system prune
