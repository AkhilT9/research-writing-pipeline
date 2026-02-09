import gradio as gr
from dotenv import load_dotenv
load_dotenv()

from crew import crew

def run_crew(user_input):
    result = crew.kickoff(inputs={"topic": user_input})
    return result

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 CrewAI – Research & Writing Agents")

    topic = gr.Textbox(
        label="Enter topic",
        placeholder="e.g. Explain CrewAI"
    )

    output = gr.Textbox(
        label="Crew Output",
        lines=15
    )

    btn = gr.Button("Run Crew")

    btn.click(
        fn=run_crew,
        inputs=topic,
        outputs=output
    )

demo.launch()
