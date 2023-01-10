// Alerts
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 6000);

// Footer copyright full year 
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
