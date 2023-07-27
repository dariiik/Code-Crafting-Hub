var pug = require('pug'); 
var port = 3000; 
var app = express(); 
//var pug = require('pug')

app.use(function(req, res, next){
    console.log('Time: ', Date.now());
    next(); 
}); 

//app.set('view engine', 'pug'); 
app.set('view engine', 'ejs'); 
app.set('views', path.join(__dirname, 'views'));

app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({extended: false})); 
app.use(express.static(path.join(__dirname, 'public'))); 
//connecting the ejs syntax//
app.get('/', function(req, res){
    res.render('index', {
        title: 'Hello world', 
        showTitle: true, 
        people: ['John', 'steve', 'he']
    }); 
});


app.get('/about', function(req, res){
    res.send('about page'); 
});

app.listen(port); 
console.log('server started on port 3000');
module.exports = app;
