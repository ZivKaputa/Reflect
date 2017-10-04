var express = require('express');
var PythonShell = require('python-shell');
var app = express();

app.get('/flash', function (req, res) {
    PythonShell.run('flash.py', function (err) {
        if (err) {
            console.log(err);
        } else {
            console.log('Succesfully Ran Command.');
        }

    });
   res.send('Flashing');
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)

})
