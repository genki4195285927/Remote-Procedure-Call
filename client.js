const net = require("net");

nums_received = 0;
json_datas = [
    {"method": "floor", "params": [3.14159265], "id": 0},
    // {"method": "nroot", "params": [3, 125], "id": 1},
    // {"method": "reverse", "params": ["abcdefg"], "id": 2},
    // {"method": "validAnagram", "params": ["acdeb", "bceda"], "id": 3},
    // {"method": "sort", "params": ["cfgabed"], "id": 4}
];

const client = new net.Socket();

client.setEncoding("utf8");

client.connect("/tmp/socket_file", "localhost", () => {
    console.log('connected to server');

    for (let i = 0; i < json_datas.length; i++) {
        client.write(JSON.stringify(json_datas[i]));
    }
});

client.on("data", (data) => {
    console.log("received data: " + data);

    nums_received++;
    
    if (nums_received == json_datas.length) {
        client.end();
    }
});

client.on("end", () => {
    console.log('disconnected from server');
});