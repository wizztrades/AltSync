# predictor.py
import gradio as gr
from predictor_logic import predict_altcoin_move

def predictor_tab():
    with gr.Tab("Predictor"):
        gr.Markdown("""
        <div style='text-align: center; padding-top: 1em;'>
            <h1 style='font-size: 2.6em;'>AltSync Predictor</h1>
            <p style='font-size: 1.2em; color: gray;'>Forecast altcoin moves based on BTC trend sensitivity.</p>
        </div>
        """)

        with gr.Group():
            with gr.Row():
                altcoin = gr.Textbox(label="Altcoin Symbol", placeholder="e.g., ETH, SOL")
                btc_move = gr.Number(label="Expected BTC % Move")

            predict_btn = gr.Button("🚀 Predict Move")

        prediction_box = gr.Markdown(value="", visible=True)

        predict_btn.click(
            fn=predict_altcoin_move,
            inputs=[altcoin, btc_move],
            outputs=prediction_box
        )