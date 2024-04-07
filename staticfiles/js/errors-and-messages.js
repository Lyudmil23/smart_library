setTimeout(function() {
    let messageList = document.getElementsByClassName('messages')[0]
    while (messageList.firstChild) {
        messageList.removeChild(messageList.firstChild);
    }
    messageList.style.display = 'none';
}, 7000);


$(document).ready(function(){
    setTimeout(function(){
        $('.errorlist').fadeOut('slow');
    }, 7000);
});
