function playGame(choice) {
    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ choice: choice }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `
            You chose: ${data.user_choice}
            Computer chose: ${data.computer_choice}
            Result: ${data.result}
        `;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
