document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelector('#submit').onclick= ()=> {
                const selection = document.querySelector('#mensaje').value;
                socket.emit('submit mensaje', {'mss': selection});
        };
    });

    // When a new vote is announced, add to the unordered list
    socket.on('announce mensaje', data => {
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.mss}`;
        document.querySelector('#mensajes').append(li);
    });
