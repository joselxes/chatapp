document.addEventListener('DOMContentLoaded', () => {
    var vara=null;
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    // document.querySelector('#yes').disabled = true;
    // document.querySelector('#task').onkeyup = ()=>{
    //
    // }
//
    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelector('#forma').onsubmit = () => {
                // const request = new XMLHttpRequest();
                const contenido = document.querySelector('#mensaje').value;
                const userName = document.querySelector('#yes').dataset.vote;
                const nombreCanal = document.querySelector('#nombreCanal').innerHTML;
                vara=nombreCanal;
                socket.emit('submit mensaje', {'contenido': contenido,'userName':userName,'nombreCanal':nombreCanal});
                return false;
            };

    });

    // When a new vote is announced, add to the unordered list
    socket.on('announce mensaje', data => {
        const li = document.createElement('li');
        const paragraph = document.createElement('p');
        paragraph.appendChild(li);
        const hola=vara==`${data.roomName}`;
        if (hola){
          li.innerHTML = `${data.userName}: ${data.contenido} `;
          document.querySelector('#votes').append(paragraph);
          document.querySelector('#mensaje').value="";}
    });
});

//
// document.addEventListener('DOMContentLoaded', () => {
//
//     // Connect to websocket
//     var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
//
//     // When connected, configure buttons
//     socket.on('connect', () => {
//
//         // Each button should emit a "submit vote" event
//         document.querySelector('#yes').onclick = () => {
//                 const contenido = document.querySelector('#mensaje').value;
//                 const user = "jose";
//                 socket.emit('submit mensaje', {'contenido': contenido,'user':user});
//
//             };
//
//     });
//
//     // When a new vote is announced, add to the unordered list
//     socket.on('announce mensaje', data => {
//         const li = document.createElement('li');
//         li.innerHTML = `${data.user}: ${data.contenido}`;
//         document.querySelector('#votes').append(li);
//         document.querySelector('#mensaje').value="";
//     });
// });
