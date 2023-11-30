class User {
    constructor(username) {
        this.username = username;
        this.balance = 0;
        this.transactions = [];
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
