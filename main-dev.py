# Server startup command: uvicorn main-dev:app --reload

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'name': 'You reached the base path. Nothing to look here buddy.'}

@app.get('/blog/unpublished')
def unpublished():
    # This route needs to defined before /blog/{id}
    return {'data': 'All unpublished blogs are now shown!'}

@app.get('/blog/{id}')
def about(id: int):
    return {'data': f'Now showing Blog with ID: {id}'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished blogs are now shown!'}

@app.get('/blog/{id}/comments')
def comments(id: int):
    # Fetch comments of blog with id = id
    return {'data': {f'Now showing the comments for blog with ID: {id}'}}