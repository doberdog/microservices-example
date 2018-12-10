const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 5000;

const server = require('http').Server(app);
const socketIO = require('socket.io')(server);
const socket = socketIO.of('/petrichor');
const rabbitMQHandler = require('./rabbit_connection');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

rabbitMQHandler((connection) => {
    connection.createChannel((err, channel) => {
        if (err) {
            throw new Error(err);
        }
        const weatherQueue = 'petrichor';
        channel.assertQueue('', {exclusive: true}, (err, queue) => {
            if (err) {
                throw new Error(err)
            }
            channel.bindQueue(queue.queue, weatherQueue, '');
            channel.consume(queue.que, (msg) => {
                const result = JSON.stringify(
                    {
                        result: Object.values(JSON.parse(msg.content.toString()).task)
                            .reduce((accumulator, currentValue) =>
                                parseInt(accumulator) + parseInt(currentValue)
                            )
                    });
                socket.emit('petrichor', result)
            })
        }, {noAck: true})
    })
});

// API calls
app.get('/api/hello', (req, res) => {
  res.send({ express: 'Hello From Express' });
});

app.post('/api/weather', (req, res) => {
    rabbitMQHandler((connection) => {
        connection.createChannel((err, channel) => {
            if (err) {
                throw new Error(err)
            }
            const ex = 'payload';
            const msg = JSON.stringify({task: req.body });
            channel.publish(ex, '', new Buffer(msg), {persistent: false});
            channel.close(() => {connection.close()})
        })
    });
});

if (process.env.NODE_ENV === 'production') {
  // Serve any static files
  app.use(express.static(path.join(__dirname, 'client/build')));

  // Handle React routing, return all requests to React app
  app.get('*', function(req, res) {
    res.sendFile(path.join(__dirname, 'client/build', 'index.html'));
  });
}

app.listen(port, () => console.log(`Petrichor API listening on port ${port}`));
