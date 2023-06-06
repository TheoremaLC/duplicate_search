const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser'); 
const port = process.env.PORT || 3000;

const app = express();
app.post('new-bug', (req, res) => {
    //create a new bug with title and description
    const bug = new Bug({
        title: req.body.title,
        description: req.body.description
        });
});


const uri = 'mongodb+srv://Petecute:Totoro2020@cluster0.agdmhzu.mongodb.net/?retryWrites=true&w=majority';

mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
.then(() => {
    console.log('Connected to MongoDB Atlas cluster');

    // Start your server after successful connection
    app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
    });

    // Perform database operations here
})
.catch((error) => {
    console.error('Error connecting to MongoDB Atlas:', error);
});
