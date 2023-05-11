# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory to /potparser
WORKDIR /potparser

# Copy the current directory contents into the container at /potparser
COPY . /potparser

# Run pip to install the package
RUN pip install .

# Set the default command to run when a container starts
CMD ["potparser"]