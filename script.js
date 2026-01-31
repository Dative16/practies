    console.log('Hello, World!');
    
    document.getElementById('greeting_bt').addEventListener('click', function() {
        let name = document.getElementById('username').value;
        //if statement
        if (name === '') {
            alert('Please enter your name.');
            return;
        }
        if (name != ""){
            confirm("Are you sure you want to proceed?");
        }
        const greetingMessage = greetUser(name);
        document.getElementById('greeting_ms').innerText = greetingMessage;
    });

    // .innerText to change text content of an element
    //.innerHTML to change html content of an element

    function greetUser(name) {
        return `Hello, ${name}! Welcome to our website.`;
    }