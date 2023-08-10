app.patch('/players/:playerId', (req, res) => {
  const { params: {playerId }, body: { teamId } } = req;
  addPlayerToTeam(playerId, teamId); 
  res.send(); 
});
