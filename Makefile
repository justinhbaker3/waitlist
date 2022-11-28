.PHONY: build-docker
build-docker:
	docker build . --tag waitlist

.PHONY: run-docker
run-docker:
	docker run -p 8000:8000 waitlist

.PHONY: test
test:
	python babelfishbanking/manage.py test waitlist
	