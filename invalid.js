app.post('/players, (req, res) => {
      const { body: { name, number, position } } = req; 
      if (!(parseInt(number) >= 0)) {
        res.status(400).send('Number must be a non-negative integer');
        return;
      } 
      const playerId = createPlayer(name, number, position);
      res.send({ playerId }); 
}); 
