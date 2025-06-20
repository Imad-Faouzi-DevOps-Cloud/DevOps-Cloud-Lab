# Use the official Node.js LTS image
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Copy dependency files first for caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app files
COPY . .

# Expose the port this app runs on
EXPOSE 3000

# Command to run the app
CMD ["node", "server.js"]
