# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt
RUN chmod +x wait-for-it.sh

# # command to run on container start
# CMD [ "python", "./index.py" ]