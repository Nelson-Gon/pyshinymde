FROM debian:bullseye
FROM python:3.9

RUN apt-get update -y && apt-get install -y git
CMD ["python", "pip", "install", "-e", "."]
CMD ["bash", "./scripts/mkdocs.sh"]




