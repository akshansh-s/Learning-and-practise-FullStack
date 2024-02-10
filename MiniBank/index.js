const express = require('express');
const User = require('./models/users.js');
const app = express();
app.use(express.json());
let demoUser = new User('akshansh','ilovefintech',10000);

//Routes---
//Login
app.post('/login', async (req, res) => { 
    const { username, password } = req.body;
    const user = demoUser; 

    if (username !== user.username) {
        return res.status(401).send("Invalid username or password");
    }

    try {
        // Compare the plain text password with the hashed password
        const isMatch = await bcrypt.compare(password, user.hashedPassword);
        if (!isMatch) {
            return res.status(401).send("Invalid username or password");
        }

        res.send(`User ${username} logged in successfully`);
    } catch (error) {
        // Errors during password comparison
        res.status(500).send("An error occurred during login");
    }
});

// Deposit money
app.post('/deposit', (req, res) => {
    const { amount } = req.body;
    if (!amount || amount < 0) {
        return res.status(400).send('Invalid deposit amount');
    }
    demoUser.deposit(amount);
    res.send(`Deposited: $${amount}. Current balance: $${demoUser.balance}`);
});

// Withdraw money
app.post('/withdraw', (req, res) => {
    const { amount } = req.body;
    try {
        demoUser.withdraw(amount);
        res.send(`Withdrew: $${amount}. Current balance: $${demoUser.balance}`);
    } catch (error) {
        res.status(400).send(error.message);
    }
});

// Check balance
app.get('/balance', (req, res) => {
    res.send(`The current balance is: $${demoUser.balance}`);
});

// Transaction history
app.get('/history', (req, res) => {
    res.send(`Transaction history: ${JSON.stringify(demoUser.transactions)}`);
});

app.listen(3000, () => {
    console.log("App is running on http://localhost:3000");
});
