import gradio as gr
from predictor import predictor_tab  # ✅ Add this line

def main():
    with gr.Blocks(title="AltSync Predictor", theme=gr.themes.Base()) as demo:
        predictor_tab()
    return demo

if __name__ == "__main__":
    main().launch()