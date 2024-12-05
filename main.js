const http = require('node:http');

const hostname = '127.0.0.1';
const port = 3001;

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${hostname}:${port}`);
  const youtubeUrl = url.searchParams.get('url');

  if (!youtubeUrl) {
    res.statusCode = 400;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(
      { 
      error: "Parâmetro 'url' é necessário!" 
    }));
    return;
  }

  const flaskPath = `/analyze?url=${encodeURIComponent(youtubeUrl)}`;

  const options = {
    hostname: '127.0.0.1',
    port: 5000,
    path: flaskPath,
    method: 'GET',
  };

  const reqFlask = http.request(options, (resFlask) => {
    let rawData = '';
    resFlask.on('data', (chunk) => {
      rawData += chunk;
    });

    resFlask.on('end', () => {
      try {
        res.statusCode = resFlask.statusCode;
        res.setHeader('Content-Type', 'application/json');
        res.end(rawData);
      } catch (e) {
        console.error(e.message);
        res.statusCode = 500;
        res.end('Internal Server Error');
      }
    });
  });

  reqFlask.on('error', (e) => {
    console.error(`Problem with request: ${e.message}`);
    res.statusCode = 500;
    res.end('Error connecting to Flask server');
  });

  reqFlask.end();
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
