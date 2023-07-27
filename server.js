//creating a server// 

var http = require('http'); 

var host = '127.0.0.1'; 
var port = '3000'; 
//check if there is an html file// 
fs.readFile('./index.html', function(err, html){
    if(err){
        console.log(err);
        return;
    }
    
    var server = http.createServer(function(req, res){
        res.statusCode = 200; 
        res.setHeader('Content-Type', 'text/plain'); 
        res.write(html); 
        res.end();
    }); 
    server.listen(port, host, function(){
        console.log('Server running on port 3000');
    });
});
