// Alerts
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);

// Footer copyright full year 
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
