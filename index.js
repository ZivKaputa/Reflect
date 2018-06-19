var express = require('express');
var PythonShell = require('python-shell');
var app = express();

app.use('/static', express.static('public'));

app.get('/flash', function (req, res) {
    var options = {
      args: [req.query.red, req.query.green, req.query.blue]
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
