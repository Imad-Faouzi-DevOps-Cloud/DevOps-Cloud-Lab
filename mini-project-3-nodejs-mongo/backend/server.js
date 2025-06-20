// Import the Express web framework
const express = require('express');

// Import Mongoose to connect to MongoDB
const mongoose = require('mongoose');

// Initialize the Express app
const app = express();

// Use environment variables for config
const PORT = process.env.PORT || 3000;
const MONGO_URI = process.env.MONGO_URI || 'mongodb://mongo:27017/test';

// Connect to MongoDB using Mongoose
mongoose.connect(MONGO_URI)
  .then(() => console.log('✅ Connected to MongoDB'))
  .catch(err => console.error('❌ MongoDB connection error:', err));

// Define a test route
app.get('/', (req, res) => {
  res.send('Hello from Node.js + MongoDB Docker Compose App!');
});

// Start listening on specified port
app.listen(PORT,'0.0.0.0', () => {
  console.log(`🚀 Server is running on http://localhost:${PORT}`);
});
