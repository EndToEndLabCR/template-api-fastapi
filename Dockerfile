# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Install bash
RUN apt-get update && apt-get install -y bash

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefer-binary -v -r requirements.txt

# Copy the rest of the application code into the container
COPY ./ .


ENV PYTHONPATH=.
ENV PYTHONBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

# Add and configure a non-root user
RUN addgroup --system appuser && adduser --system --ingroup appuser -u 999 appuser

# Ensure the working directory is owned by the non-root user
RUN chown -R appuser:appuser /app && \
    chown -R appuser:appuser /tmp

COPY /start.sh /start.sh
RUN chmod a+x /start.sh

# Switch to the non-root user
USER 999

#Expose the application port
EXPOSE 5000

# Configure container start behaviour
ENTRYPOINT ["/start.sh"]
