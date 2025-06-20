require('dotenv').config();
const express = require('express');
const fs = require('fs');
const path = require('path');

const SECRET_URL = process.env.SECRET_URL;
if (!SECRET_URL) {
    throw new Error('SECRET_URL not set in .env file');
}

const app = express();
app.use(express.json());

app.all(`/${SECRET_URL}`, (req, res) => {
    if (req.method === 'GET') {
        return res.status(200).send('up');
    }
    const data = req.body;
    if (!data || Object.keys(data).length === 0) {
        console.log('nothing received');
        return res.status(204).send('');
    }
    const { title, message, priority } = data;
    console.log(`  title: ${title}`);
    console.log(`  msg: ${message}`);
    console.log(`  priority: ${priority}`);
    // TODO: implement logger
    try {
        fs.writeFileSync(
            path.join(__dirname, '../logs/latest_notification.json'),
            JSON.stringify({ title, message, priority })
        );
    } catch (e) {
        console.log(`Failed to write notification: ${e}`);
    }
    return res.status(204).send('');
});

app.get(`/${SECRET_URL}/version`, (req, res) => {
    res.status(200).json({ version: '1.0.0' });
});

app.post(`/${SECRET_URL}/message`, (req, res) => {
    const data = req.body;
    if (!data || Object.keys(data).length === 0) {
        console.log('nothing received');
        return res.status(204).send('');
    }
    const { title, message, priority } = data;
    console.log(`  title: ${title}`);
    console.log(`  msg: ${message}`);
    console.log(`  priority: ${priority}`);
    // logger
    try {
        fs.writeFileSync(
            path.join(__dirname, '../logs/latest_notification.json'),
            JSON.stringify({ title, message, priority })
        );
    } catch (e) {
        console.log(`Failed to write notification: ${e}`);
    }
    return res.status(200).json({});
});

const PORT = 5123;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on port ${PORT}`);
});
