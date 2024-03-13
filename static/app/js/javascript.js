
console.log("connect")
// const groupName = JSON.parse(document.getElementById("groupName").textContent)
const user = document.getElementById('user').value;
console.log(user) ;
const receiver = 'admin';
var ws = new WebSocket(
    'ws://'+
    window.location.host+  
    '/ws/ac/'
    );
ws.onopen = (event)=>{
    // console.log("hello")
    // console.log(event)
}
ws.onmessage = (event)=>{
    console.log(event.data)
    const data = JSON.parse(event.data)
    let a = document.getElementById('msglist').value;
     let b = a.concat(data['user'] + " : " + data['msg'] + "\n")
    console.log(b)
    document.getElementById('msglist').value = b;
}
ws.onerror = (event)=>{
    console.log("errer")
}
ws.onclose = (event)=>{
    console.log("close")
}
document.getElementById('send').onclick = (event)=>{
    const user = document.getElementById('user').value;
    let msg = document.getElementById('msg').value;
    data = {'msg':msg,'user':user}
    parse_data = JSON.stringify(data)
    console.log(typeof(parse_data))
    ws.send(parse_data)
    document.getElementById('msg').value="";
}