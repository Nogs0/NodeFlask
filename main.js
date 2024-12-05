const http = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer(async (req, res) => {
  http.get(`http://127.0.0.1:5000/`, (resFlask) => {
    let rawData = '';
    resFlask.on('data', (chunk) => {
      rawData += chunk;
    });

    resFlask.on('end', async () => {
      try {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html');
        res.end(rawData);
      } catch (e) {
        console.error(e.message);
      }
    });
  })
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});