let expose = function(func) {
    let func_name = func.name;

    let data = JSON.stringify({
        method: 'expose',
        func_name: func_name
    });
    console.log(data);
}

export {expose};
