FROM python:3-alpine

RUN apk add --no-cache git
<<<<<<< HEAD
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-framartinez24

WORKDIR /ajedrez-2024-framartinez24

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python cli.py"]

# docker buildx build -t ajedrez-2024-framartinez24 .
# docker run -i /ajedrez-2024-framartinez24
=======
RUN git clone https://github.com/um-computacion-tm/first-circleci-dqmdz-um.git

WORKDIR /first-circleci-dqmdz-um

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python main.py"]

# docker buildx build -t first-circleci-dqmdz-um .
# docker run -i first-circleci-dqmdz-um
>>>>>>> main
