import {py_func, py_func2} from './my_module.js'

py_func('test', 123).then(
    v => console.log(v)
);

py_func2('test2').then(
    v => console.log(v)
);
py_func(456).then(
    v => console.log(v)
);

