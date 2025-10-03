const quotes = [
    "Believe in yourself!",
    "You can do it!",
    "Every day is a new opportunity.",
    "Mistakes are proof that you are trying.",
    "Success is the sum of small efforts repeated daily."
];

function getRandomQuote() {
    const index = Math.floor(Math.random() * quotes.length);
    return quotes[index];
}

// Example usage
console.log("Here's your motivational quote:");
console.log(getRandomQuote());
