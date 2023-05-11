// Require the 'process' module
const process = require('process');

// Define a function to check if a message is spam
function isSpam(message) {
  // Define regular expressions to match common spam patterns
  const urlRegex = /http\S+/gi;
  const phoneRegex = /\d{10}/g;
  const emailRegex = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;

  // Check if the message contains any URLs
  if (message.match(urlRegex)) {
    return true;
  }

  // Check if the message contains any phone numbers
  if (message.match(phoneRegex)) {
    return true;
  }

  // Check if the message contains any email addresses
  if (message.match(emailRegex)) {
    return true;
  }

  // Add more spam detection rules as needed

  // If none of the rules match, the message is not spam
  return false;
}

// Define a function to handle incoming messages
function handleMessage(message) {
  // Check if the message is spam
  if (isSpam(message.body)) {
    console.log(`Spam message detected: ${message.body}`);

    // Block the user who sent the spam message
    const chatId = message.chat.id._serialized;
    const contactId = message.sender.id._serialized;
    process.emit('blockContact', { chatId, contactId });
  }
}

// Add a listener for incoming messages
process.on('message', handleMessage);