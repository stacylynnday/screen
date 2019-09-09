# Use an official Python runtime as a parent image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the conainer at /app
COPY . /app

#RUN pip install pandas

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME iHeart

# Run analyzeCSVFiles.py when the container launches
CMD ["python", "analyzeCSVFiles.py"]
##RUN ["python", "analyzeCSVFiles.py"]
