const express = require('express');
const app = express();

app.use(express.json()); 

let balance = 0;
let transactions = [];

app.get('/balance', (req, res) => {
    res.send(`The current balance is: ${balance}`);
});

app.get('/history', (req, res) => {
    res.send(`These are the transactions: ${JSON.stringify(transactions)}`);
});

// Route to handle deposits
app.post('/deposit', (req, res) => {
    const { amount } = req.body;
    if (!amount || amount < 0) {
        return res.status(400).send('Invalid deposit amount');
    }
    balance += amount;
    transactions.push({ type: 'deposit', amount });
    res.send(`Deposited: $${amount}. Current balance: $${balance}`);
});

// Route to handle withdrawals
app.post('/withdraw', (req, res) => {
    const { amount } = req.body;
    if (!amount || amount < 0 || amount > balance) {
        return res.status(400).send('Invalid withdrawal amount');
    }
    balance -= amount;
    transactions.push({ type: 'withdraw', amount });
    res.send(`Withdrew: $${amount}. Current balance: $${balance}`);
});

app.listen(3000, () => {
    console.log("App is running on http://localhost:3000");
});
