# Step 1: Use an official lightweight Python image
FROM python:3.11-slim

# Step 2: Set working directory in container
WORKDIR /app

# Step 3: Copy dependency file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application code
COPY . .

# Step 5: Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
