const MongoClient = require('mongodb').MongoClient; 
//connected url//
const url = 'mongodb://localhost:27017/myproject'; 
MongoClient.connect(url, function(err, db){
    if(err){
        return console.dir(err);
    }
    console.log('Connected to mongodb');

    InsertDocument(db, function(){
        db.close();
    });
    InsertDocuments(db, function(){
        db.close();
    });
    //use this to find the document and also see if the doc was updated//
    FindDocuments(db, function(){
        db.close();
    }); 
    QueryDocument(db, function(){
        db.close();
    });
    //remove document//

    RemoveDocument(db, function(){
        db.close();
    });
}); 
//the data// 
//inserting a single document//
const InsertDocument = function(db, callback){
    const collection = db.collection('users'); 
    collectionn.insert({
        name: 'Brad Traversy', 
        email: 'brad@test.com'
    }, function(err, result){
        if(err){
            return console.dir(err); 
        }
        console.log('inserted document'); 
        console.log(result); 
        callback(result); 
    });
}
//insert multiple docs// 
const InsertDocuments = function(db, callback){
    const collection = db.collection('users'); 
    collection.insertMany([
        {
            name: 'John Doe', 
            email: 'john@test.com'
        },
        {
            name: 'Sam Smith', 
            email: 'ssmith@test.com'
        }, 
        {
            name: 'Joze Gomes', 
            email: 'jgomez@test.com'
        }
    ],
    function(err, result){
        if(err){
            return console.dir(err);
        }
        console.log('Inserted '+result.ops.lenght+' documents');
        console.log(result); 
    });
}

//find documennts, find a variable, create multiple documents//
const QueryDocument = function(db, callback){
    const collection = db.collection('users');
    collection.find({'name': 'John Doe'}).toArray(function(err, docs){
        if(err){
            return console.dir(err);
        }
        console.log('Found the following records');
        console.log(docs); 
        callback(docs);
    });
}
//update documents//
const updateDocument = function(db, callback){
    const collection = db.collection('users');
    collectionn.updateOne({name: 'John Doe'}, 
        {$set: {email: 'john@something.com'}}, 
        function(err, result){
            if(err){
                return console.dir(err);
            }
            console.log('Updated Document'); 
            callback(result);
        });
}
//remove document//
const RemoveDocument = function(db, callback){
    const collection = db.collection('users'); 
    collection.deleteOne({name: 'John Doe'}, function(err, result){
        if(err){
            return console.dir(err);
        }
        console.log('removed document');
        console.log(result);
        callback(result);
    });
}
