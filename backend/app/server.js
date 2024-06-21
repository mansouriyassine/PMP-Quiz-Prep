const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const mongoose = require('mongoose');

// Load environment variables
dotenv.config();

console.log('MONGODB_URI:', process.env.MONGODB_URI);
console.log('PORT:', process.env.PORT);

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.set('strictQuery', false);
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => {
  console.log('Connected to MongoDB');
})
.catch((error) => {
  console.error('MongoDB connection error:', error);
  console.error('Error name:', error.name);
  console.error('Error message:', error.message);
  if (error.reason) {
    console.error('Error reason:', error.reason);
  }
  // Log the full error object for debugging
  console.error('Full error object:', JSON.stringify(error, null, 2));
});

// Routes
app.get('/', (req, res) => {
  res.send('PMP Quiz Prep API is running');
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});