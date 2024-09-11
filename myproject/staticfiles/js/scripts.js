document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is linked correctly!");

    // Select the form element
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Generate a 6-digit random representative code
        const repCode = Math.floor(100000 + Math.random() * 900000);

        // Display the alert with the generated code
        alert(`Your representative code has been generated successfully: ${repCode}`);

        // Submit the form
        this.submit();

        // Clear the form fields
        this.reset();
    });
});
