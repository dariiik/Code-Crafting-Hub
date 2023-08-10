const express = require('express'); 

const PORT = 3000; 
const app = express(); 
app.use(express.json())
app.post('/players', (req, res) => {
  const { body: { name, number, position } } = req; 
  const playerId = createPlayer(name, number, position); 
  res.send({ playedId });
}); 

app.listen(PORT, () => {
  console.log('Example app listening on port ${PORT}')
});
