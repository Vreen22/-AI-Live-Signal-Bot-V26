from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

BASE = Path(__file__).resolve().parent
INDEX = BASE / "index.html"

app = FastAPI(title="AI Live Signal Bot V27.5 - Trend-First Live 8 Sources")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SOURCES = [
    {"id":"binance","name":"Binance","category":"Crypto","status":"LIVE"},
    {"id":"bybit","name":"Bybit","category":"Crypto","status":"LIVE"},
    {"id":"okx","name":"OKX","category":"Crypto","status":"LIVE"},
    {"id":"coinbase","name":"Coinbase Exchange","category":"Crypto","status":"LIVE"},
    {"id":"kraken","name":"Kraken","category":"Crypto","status":"LIVE"},
    {"id":"bitget","name":"Bitget","category":"Crypto","status":"LIVE"},
    {"id":"gateio","name":"Gate.io","category":"Crypto","status":"LIVE"},
    {"id":"mexc","name":"MEXC","category":"Crypto","status":"LIVE"},

    {"id":"kucoin","name":"KuCoin","category":"Crypto","status":"LISTED"},
    {"id":"bitfinex","name":"Bitfinex","category":"Crypto","status":"LISTED"},
    {"id":"cryptocom","name":"Crypto.com Exchange","category":"Crypto","status":"LISTED"},
    {"id":"deribit","name":"Deribit","category":"Crypto","status":"LISTED"},
    {"id":"gemini","name":"Gemini","category":"Crypto","status":"LISTED"},
    {"id":"hyperliquid","name":"Hyperliquid","category":"Crypto","status":"LISTED"},
    {"id":"htx","name":"HTX / Huobi","category":"Crypto","status":"LISTED"},
    {"id":"bitstamp","name":"Bitstamp","category":"Crypto","status":"LISTED"},
    {"id":"bithumb","name":"Bithumb","category":"Crypto","status":"LISTED"},
    {"id":"upbit","name":"Upbit","category":"Crypto","status":"LISTED"},
    {"id":"phemex","name":"Phemex","category":"Crypto","status":"LISTED"},
    {"id":"poloniex","name":"Poloniex","category":"Crypto","status":"LISTED"},
    {"id":"dydx","name":"dYdX","category":"Crypto","status":"LISTED"},
    {"id":"bitflyer","name":"bitFlyer","category":"Crypto","status":"LISTED"},
    {"id":"coinex","name":"CoinEx","category":"Crypto","status":"LISTED"},
    {"id":"lbank","name":"LBank","category":"Crypto","status":"LISTED"},
    {"id":"whitebit","name":"WhiteBIT","category":"Crypto","status":"LISTED"},
    {"id":"bitmart","name":"BitMart","category":"Crypto","status":"LISTED"},
    {"id":"ascendex","name":"AscendEX","category":"Crypto","status":"LISTED"},
    {"id":"coinw","name":"CoinW","category":"Crypto","status":"LISTED"},
    {"id":"bingx","name":"BingX","category":"Crypto","status":"LISTED"},

    {"id":"oanda","name":"OANDA","category":"Forex / CFD","status":"API KEY REQUIRED"},
    {"id":"fxcm","name":"FXCM","category":"Forex / CFD","status":"API KEY REQUIRED"},
    {"id":"twelvedata","name":"Twelve Data","category":"Forex / Metals","status":"API KEY REQUIRED"},
]

CRYPTO_SYMBOLS = {
    "binance": [
        "BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","XRPUSDT",
        "ADAUSDT","DOGEUSDT","AVAXUSDT","LINKUSDT","LTCUSDT"
    ],
    "bybit": [
        "BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","DOGEUSDT",
        "BNBUSDT","ADAUSDT","AVAXUSDT","LINKUSDT"
    ],
    "okx": [
        "BTC-USDT","ETH-USDT","SOL-USDT","XRP-USDT","DOGE-USDT",
        "BNB-USDT","ADA-USDT","AVAX-USDT","LINK-USDT"
    ],
    "coinbase": [
        "BTC-USD","ETH-USD","SOL-USD","XRP-USD","DOGE-USD",
        "ADA-USD","AVAX-USD","LINK-USD"
    ],
    "kraken": [
        "BTC/USD","ETH/USD","SOL/USD","XRP/USD","DOGE/USD",
        "ADA/USD","AVAX/USD","LINK/USD"
    ],
    "bitget": [
        "BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","DOGEUSDT",
        "BNBUSDT","ADAUSDT","AVAXUSDT","LINKUSDT"
    ],
    "gateio": [
        "BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","DOGEUSDT",
        "BNBUSDT","ADAUSDT","AVAXUSDT","LINKUSDT"
    ],
    "mexc": [
        "BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","DOGEUSDT",
        "BNBUSDT","ADAUSDT","AVAXUSDT","LINKUSDT"
    ],
}

FOREX_SYMBOLS = [
    "EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD",
    "USDCHF","NZDUSD","EURGBP","EURJPY","GBPJPY"
]

METAL_SYMBOLS = [
    "XAUUSD",
    "XAGUSD"
]


@app.get("/")
async def home():
    return FileResponse(INDEX)


@app.get("/api/health")
async def health():
    return {
        "ok": True,
        "app": "AI Live Signal Bot V27.5",
        "auto_trade": False,
        "live_adapters": [
            "binance",
            "bybit",
            "okx",
            "coinbase",
            "kraken",
            "bitget",
            "gateio",
            "mexc"
        ]
    }


@app.get("/api/sources")
async def sources():
    return {
        "sources": SOURCES
    }


@app.get("/api/instruments")
async def instruments():
    return {
        "crypto": CRYPTO_SYMBOLS,
        "forex": FOREX_SYMBOLS,
        "metals": METAL_SYMBOLS
    }
