# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app/notebooks
WORKDIR /app/notebooks

# Copy just the requirements.txt to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Notebook
RUN pip install jupyter

# Copy the contents of the "notebooks" folder to the container at /app/notebooks
COPY notebooks/ /app/notebooks/

# Copy the entire "data" folder to the container at /app/data
COPY data/ /app/data/

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Define environment variable
ENV NAME World

# Run Jupyter when the container launches
CMD ["jupyter-notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
