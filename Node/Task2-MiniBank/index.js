const express = require('express');
const User = require('./models/user');
const app = express();
app.use(express.json());

// Create a demo user
let demoUser = new User('akshansh');

// Route to deposit money
app.post('/deposit', (req, res) => {
    const { amount } = req.body;
    if (!amount || amount < 0) {
        return res.status(400).send('Invalid deposit amount');
    }
    demoUser.deposit(amount);
    res.send(`Deposited: $${amount}. Current balance: $${demoUser.balance}`);
});

// Route to withdraw money
app.post('/withdraw', (req, res) => {
    const { amount } = req.body;
    try {
        demoUser.withdraw(amount);
        res.send(`Withdrew: $${amount}. Current balance: $${demoUser.balance}`);
    } catch (error) {
        res.status(400).send(error.message);
    }
});

// Route to check balance
app.get('/balance', (req, res) => {
    res.send(`The current balance is: $${demoUser.balance}`);
});

// Route to check transaction history
app.get('/history', (req, res) => {
    res.send(`Transaction history: ${JSON.stringify(demoUser.transactions)}`);
});

app.listen(3000, () => {
    console.log("App is running on http://localhost:3000");
});
