
# gradio_ui.py
import gradio as gr
import requests

API_BASE = "http://localhost:8000"  # Adjust to your FastAPI base URL

def execute_task(team: str, task: str, prompt: str):
    response = requests.post(f"{API_BASE}/execute", json={
        "team": team, "task": task, "prompt": prompt
    })
    return response.json().get("output", "No output")

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
