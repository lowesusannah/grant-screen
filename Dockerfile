# Step 1: Use an official lightweight Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy only the application files into the container
COPY main.py /app/main.py

# Step 4: Install the required production dependencies directly
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# Step 5: Expose port 8000 so the API can accept incoming web traffic
EXPOSE 8000

# Step 6: Define the default command to spin up the Uvicorn web server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
