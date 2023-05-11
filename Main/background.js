const { spawn } = require('child_process');

// Run the Node.js script
const child = spawn('node', ['cnc_0.js']);

// Log the output of the script
child.stdout.on('data', (data) => {
  console.log(`${data}`);
});

// Log any errors from the script
child.stderr.on('data', (data) => {
  console.error(`Error: ${data}`);
});

// Log when the script exits
child.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
