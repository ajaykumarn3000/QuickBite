# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy your application code
COPY . .

# Install dependencies
RUN npm install

# Build the app for production
RUN npm run build

# Install a simple HTTP server to serve static files
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["serve", "-s", "build", "-l", "3000"]
