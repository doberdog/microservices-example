const amqp = require('amqplib/callback_api');

module.exports = (callback) => {
    amqp.connect('amqp://guest:guest@localhost:5672',
        (error, conn) => {
            if (error) {
                throw new Error(error);
            }
            callback(conn);
        })
};