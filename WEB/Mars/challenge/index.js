const express = require('express');
const app = express();
const routes = require('./routes');
const path = require('path');

app.use(express.json());
app.set('views', './views');
app.use('/static', express.static(path.resolve('static')));

app.use(routes);

app.all('*', (req, res) => {
    return res.status(404).send('404 page not found');
});

// Listen on all network interfaces (0.0.0.0)
app.listen(5005, '0.0.0.0', () => {
    console.log('Server is listening on http://0.0.0.0:5005');
});