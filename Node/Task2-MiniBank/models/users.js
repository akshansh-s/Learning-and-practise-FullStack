const bcrypt = require('bcrypt');

class User {
    constructor(username,password,balance) {
        this.username = username;
        this.balance = balance;
        this.initializePassword(password);
        this.transactions = [];
    }
    async initializePassword(password) {
        this.hashedPassword = await bcrypt.hash(password, 10);
    }

    deposit(amount) {
        this.balance += amount;
        this.transactions.push({ type: 'deposit', amount });
    }

    withdraw(amount) {
        if (amount > this.balance) {
            throw new Error('Insufficient funds');
        }
        this.balance -= amount;
        this.transactions.push({ type: 'withdraw', amount });
    }
}

module.exports = User;
