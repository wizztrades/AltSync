# 📊 AltSync Predictor

**AltSync Predictor** is a crypto sensitivity forecasting tool that estimates how an altcoin may move based on an expected % move in Bitcoin (BTC). It uses real historical data and statistical modeling (beta correlation) to calculate each altcoin’s price sensitivity to BTC.

![AltSync Screenshot](https://huggingface.co/spaces/your-username/altsync-predictor/resolve/main/screenshot.png)

---

## 🚀 Features

- 🔍 **BTC-to-Altcoin Sensitivity Prediction**
- 📈 **Beta-based modeling** using 90-day rolling price data
- 📊 Clean, minimal Gradio UI
- 🔁 Real-time price data from CryptoCompare API
- 🧠 Ready for expansion with volatility, regression, and ensemble models

---

## 🧠 How It Works

1. User inputs an **altcoin symbol** (e.g., `ETH`, `SOL`)
2. User specifies an **expected % move in BTC**
3. App:
   - Fetches the last 90 days of price data for BTC and the altcoin
   - Calculates daily returns and beta correlation
   - Predicts the altcoin move as `Alt Move ≈ BTC Move × Beta`

---

## 📦 File Structure

```
.
├── app.py               # Gradio entry point
├── config.py            # API key and constants
├── predictor.py         # Gradio tab layout
├── predictor_logic.py   # Real prediction logic
├── requirements.txt     # Python dependencies
├── utils/
│   ├── api.py           # Fetch price history from CryptoCompare
│   └── models.py        # Beta, returns, volatility calculations
```

---

## 🔧 Installation (Local)

```bash
git clone https://github.com/yourusername/altsync-predictor.git
cd altsync-predictor
pip install -r requirements.txt
python app.py
```

---

## 🌐 Run Online (Hugging Face Spaces)

Deploy directly to [Hugging Face Spaces](https://huggingface.co/spaces):

- SDK: `Gradio`
- Entry point: `app.py`
- Add API key via **Secrets** → `API_KEY=your_key`

---

## 🔐 API Key Setup

Create a `.env` file or add it to Hugging Face Secrets:

```python
# config.py
import os
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://min-api.cryptocompare.com"
```

---

## 🧪 Coming Soon

- 🔁 Volatility multipliers
- 📉 Linear regression and ensemble averaging
- 🧪 Backtesting tab with real prediction error stats
- 📊 Performance charts and CSV export

---

## 🧑‍💻 Author

**WizzTrades**  
🚀 GitHub: [@wizztrades](https://github.com/wizztrades)

---

## 📄 License


MIT License – free to use, modify, and share.
