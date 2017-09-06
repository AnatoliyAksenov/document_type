const request = require('request')
const fs = require('fs');

let f = fs.readFileSync('1.jpg');

request({
    method: 'POST',
    uri: 'http://127.0.0.1:5000/api/document/gettype',
    //encoding: null,
    json: {file: f.toString('base64')}    

}, (err, response, data) => {
    if ( err ){
        console.error(err);
    } else {
        console.log(data);
    }
});