
# app.py (FastAPI)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class TaskRequest(BaseModel):
    team: str
    task: str
    prompt: str

@app.post("/execute")
def execute_task(req: TaskRequest):
    # You can route tasks to different modules here
    if req.team == "Red" and req.task == "Exploit":
        # Stub: Replace with AI logic or subprocess
        output = f"Running red team exploit with prompt: {req.prompt}"
    elif req.team == "Blue" and req.task == "Analyze Logs":
        # Example: Call AI model or subprocess
        output = f"Parsing logs with AI assist: {req.prompt}"
    else:
        raise HTTPException(status_code=400, detail="Invalid task")
    return {"output": output}

def execute_tasks(team: str, task: str, prompt: str):
    # You can route tasks to different modules here
    if team == "Red" and task == "Exploit":
        # Stub: Replace with AI logic or subprocess
        output = f"Running red team exploit with prompt: {prompt}"
    elif team == "Blue" and task == "Analyze Logs":
        # Example: Call AI model or subprocess
        output = f"Parsing logs with AI assist: {prompt}"
    else:
        raise HTTPException(status_code=400, detail="Invalid task")
    return {"output": output}


import gradio as gr
import requests

API_BASE = "http://localhost:8000"  # Adjust to your FastAPI base URL

def execute_task(team: str, task: str, prompt: str):
 
    return execute_tasks(team, task, prompt)

iface = gr.Interface(
    fn=execute_task,
    inputs=[
        gr.Dropdown(["Red", "Blue"], label="Team"),
        gr.Dropdown(["Recon", "Exploit", "Analyze Logs", "Generate Rule"], label="Task"),
        gr.Textbox(label="Prompt / Parameters")
    ],
    outputs="text",
    title="AI-Driven CyberOps Interface"
)

if __name__ == "__main__":
    iface.launch(share=True, debug=True)