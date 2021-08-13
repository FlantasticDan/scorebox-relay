const socket = io()

const content = document.getElementById('content')

socket.on('update', payload => {
    html = ''
    Object.entries(payload).forEach(item => {
        html += `<h3>${item[0]}</h3><h1>${item[1]}</h1>`
    })
    content.innerHTML = html
})