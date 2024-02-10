from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data model for Task with Pydantic
class Task(BaseModel):
    title: str
    name: str
    description: str
    price: float
    tax: Optional[float] = None
    status: bool = False

# Mock database
tasks_db = []

# Endpoint to get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

# Endpoint to get a specific task by id
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

# Endpoint to add a new task
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

# Endpoint to update a task by id
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task
    return task

# Endpoint to delete a task by id
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks_db.pop(task_id)
    return task

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)