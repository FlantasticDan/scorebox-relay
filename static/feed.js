const socket = io()

socket.on('update', payload => {
    console.log(payload)
})