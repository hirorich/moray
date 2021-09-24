let moray = new Object();
moray.onclose = function(evt){};
moray.expose = function(func) {
    let func_name = func.name;

    let data = JSON.stringify({
        method: 'expose',
        func_name: func_name
    });
    console.log(data);
}

export default moray;
