VERSION=v1
DOCKERUSER=dhanavikram

build:
	docker build -f Dockerfile -t chatbot-frontend .

push:
	docker tag chatbot-frontend $(DOCKERUSER)/chatbot-frontend:$(VERSION)
	docker push $(DOCKERUSER)/chatbot-frontend:$(VERSION)
	docker tag chatbot-frontend $(DOCKERUSER)/chatbot-frontend:latest
	docker push $(DOCKERUSER)/chatbot-frontend:latest