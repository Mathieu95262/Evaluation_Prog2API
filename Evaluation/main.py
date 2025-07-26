from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, PlainTextResponse
from typing import List
from models import Player

# Question 1
app = FastAPI()
@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return "<h1>Hello</h1>"

# Question 2
@app.get("/welcome", response_class=PlainTextResponse)
async def welcome(name: str = Query(..., description="Name to welcome")):
    return f"Welcome {name}"

#Question 3
players_db = []
@app.post("/players", status_code=201)
async def add_players(new_players: List[Player]):
    for p in new_players:
        if p not in players_db:
            players_db.append(p)
    return players_db

# Question 4
@app.get("/players", status_code=200)
async def get_players():
    return players_db

#Question 5
@app.put("/players")
async def update_or_add_player(player: Player):
    for index, existing in enumerate(players_db):
        if existing.Number == player.Number:
            if existing != player:
                players_db[index] = player
            return players_db
    players_db.append(player)
    return players_db