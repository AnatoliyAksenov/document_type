# Document type detection using document image
## Table of conetent

This project is the REST server for detecting document type using document image.

Project tree:
* app.py - REST implementation
* model.py - model api 
* model/doc_classification.h5 - trained model for image classification
* model/model.json - structure of model
* images - untracked images

## Usage

Example for usage this REST service:

First, need unzip weights file:
```bash
cd document_type
cat ./model/doc_classificatio.h5.gz.* > ./model/doc_classification.h5.gz
gunzip ./model/doc_classification.h5.gz
```

Running REST server:
```bash
export PORT=5000
python ./app.py
```

Create file or get from examples folder:
```javascript
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
```

And running this file:
```bash
node ./examples/gettype
```

## TODO

I need more examples of popular forms of documents to add to the model.

* post documents
* invoices
* bills

**Image requirements**: 640*640, grayscale.

Images will be added to the model as soon as possible.
