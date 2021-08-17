import {get_module_name, sum, sum_list} from '/moray/py/sample_module'

get_module_name().then(
    v => console.log(v)
);

sum(5, 8).then(
    v => console.log(v)
);
sum_list([2, 7, 11]).then(
    v => console.log(v)
);

