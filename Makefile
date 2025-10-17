IMAGE ?= tgbot-spammer
TAG ?= latest

.PHONY: docker-build

docker-build:
	docker build -t $(IMAGE):$(TAG) .
