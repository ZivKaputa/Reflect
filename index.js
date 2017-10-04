var express = require('express');
var PythonShell = require('python-shell');
var app = express();

app.get('/flash', function (req, res) {
    var options = {
      args: ['0', '200', '0']
    };

    PythonShell.run('LED_Control/set_rgb.py', options, function (err, results) {
        if (err) {
            console.log(err);
        } else {
            console.log('Succesfully Ran Command.');
        }
    });

   res.send('Color set.');
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)

})
