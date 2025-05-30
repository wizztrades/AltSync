# predictor_logic.py
from utils.api import get_price_series
from utils.models import calc_returns, compute_beta

def predict_altcoin_move(altcoin: str, btc_move: float, lookback: int = 90) -> str:
    try:
        btc_prices = get_price_series("BTC", limit=lookback)
        alt_prices = get_price_series(altcoin, limit=lookback)

        btc_returns = calc_returns(btc_prices)
        alt_returns = calc_returns(alt_prices)

        beta = compute_beta(btc_returns, alt_returns)
        predicted_move = btc_move * beta
        return f"### 📈 Predicted Move for `{altcoin.upper()}`: **~{round(predicted_move, 2)}%**"
    except Exception as e:
        return f"❌ Error during prediction: {str(e)}"
