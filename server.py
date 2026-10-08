from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


BASE = Path(__file__).resolve().parent
INDEX = BASE / "index.html"


app = FastAPI(
    title="AI Live Signal Bot V33 - Verified Live Sources"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SOURCES = [

    {
        "id": "binance",
        "name": "Binance",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "bybit",
        "name": "Bybit",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "okx",
        "name": "OKX",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "coinbase",
        "name": "Coinbase Exchange",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "kraken",
        "name": "Kraken",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "bitget",
        "name": "Bitget",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "gateio",
        "name": "Gate.io",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "mexc",
        "name": "MEXC",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "kucoin",
        "name": "KuCoin",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "bitfinex",
        "name": "Bitfinex",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "cryptocom",
        "name": "Crypto.com Exchange",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "hyperliquid",
        "name": "Hyperliquid",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "htx",
        "name": "HTX / Huobi",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "upbit",
        "name": "Upbit",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "poloniex",
        "name": "Poloniex",
        "category": "Crypto",
        "status": "NOT TESTED"
    },

    {
        "id": "coinex",
        "name": "CoinEx",
        "category": "Crypto",
        "status": "NOT TESTED"
    },


    {
        "id": "deribit",
        "name": "Deribit",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "gemini",
        "name": "Gemini",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "bitstamp",
        "name": "Bitstamp",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "bithumb",
        "name": "Bithumb",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "phemex",
        "name": "Phemex",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "dydx",
        "name": "dYdX",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "bitflyer",
        "name": "bitFlyer",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "lbank",
        "name": "LBank",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "whitebit",
        "name": "WhiteBIT",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "bitmart",
        "name": "BitMart",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "ascendex",
        "name": "AscendEX",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "coinw",
        "name": "CoinW",
        "category": "Crypto",
        "status": "LISTED"
    },

    {
        "id": "bingx",
        "name": "BingX",
        "category": "Crypto",
        "status": "LISTED"
    },


    {
        "id": "oanda",
        "name": "OANDA",
        "category": "Forex / CFD",
        "status": "API KEY REQUIRED"
    },

    {
        "id": "fxcm",
        "name": "FXCM",
        "category": "Forex / CFD",
        "status": "API KEY REQUIRED"
    },

    {
        "id": "twelvedata",
        "name": "Twelve Data",
        "category": "Forex / Metals",
        "status": "API KEY REQUIRED"
    }

]


CRYPTO_SYMBOLS = {

    "binance": [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "ADAUSDT",
        "DOGEUSDT",
        "AVAXUSDT",
        "LINKUSDT",
        "LTCUSDT"
    ],

    "bybit": [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "BNBUSDT",
        "ADAUSDT",
        "AVAXUSDT",
        "LINKUSDT"
    ],

    "okx": [
        "BTC-USDT",
        "ETH-USDT",
        "SOL-USDT",
        "XRP-USDT",
        "DOGE-USDT",
        "BNB-USDT",
        "ADA-USDT",
        "AVAX-USDT",
        "LINK-USDT"
    ],

    "coinbase": [
        "BTC-USD",
        "ETH-USD",
        "SOL-USD",
        "XRP-USD",
        "DOGE-USD",
        "ADA-USD",
        "AVAX-USD",
        "LINK-USD"
    ],

    "kraken": [
        "BTC/USD",
        "ETH/USD",
        "SOL/USD",
        "XRP/USD",
        "DOGE/USD",
        "ADA/USD",
        "AVAX/USD",
        "LINK/USD"
    ],

    "bitget": [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "BNBUSDT",
        "ADAUSDT",
        "AVAXUSDT",
        "LINKUSDT"
    ],

    "gateio": [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "BNBUSDT",
        "ADAUSDT",
        "AVAXUSDT",
        "LINKUSDT"
    ],

    "mexc": [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "BNBUSDT",
        "ADAUSDT",
        "AVAXUSDT",
        "LINKUSDT"
    ],

    "kucoin": [
        "BTC-USDT",
        "ETH-USDT",
        "SOL-USDT",
        "XRP-USDT",
        "DOGE-USDT",
        "BNB-USDT",
        "ADA-USDT",
        "AVAX-USDT"
    ],

    "bitfinex": [
        "BTCUSD",
        "ETHUSD",
        "SOLUSD",
        "XRPUSD",
        "DOGEUSD",
        "LTCUSD"
    ],

    "cryptocom": [
        "BTC_USDT",
        "ETH_USDT",
        "SOL_USDT",
        "XRP_USDT",
        "DOGE_USDT",
        "BNB_USDT",
        "ADA_USDT"
    ],

    "hyperliquid": [
        "BTC",
        "ETH",
        "SOL",
        "XRP",
        "DOGE",
        "AVAX",
        "LINK"
    ],

    "htx": [
        "btcusdt",
        "ethusdt",
        "solusdt",
        "xrpusdt",
        "dogeusdt",
        "bnbusdt",
        "adausdt"
    ],

    "upbit": [
        "USDT-BTC",
        "USDT-ETH",
        "USDT-SOL",
        "USDT-XRP",
        "USDT-DOGE",
        "USDT-ADA"
    ],

    "poloniex": [
        "BTC_USDT",
        "ETH_USDT",
        "SOL_USDT",
        "XRP_USDT",
        "DOGE_USDT",
        "BNB_USDT"
    ],

    "coinex": [
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "BNBUSDT",
        "ADAUSDT"
    ]

}


FOREX_SYMBOLS = [

    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCAD",
    "USDCHF",
    "NZDUSD",
    "EURGBP",
    "EURJPY",
    "GBPJPY"

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

        "app":
        "AI Live Signal Bot V33",

        "auto_trade":
        True,

        "auto_trade_demo":
        True,

        "real_mode_available":
        True,

        "real_orders":
        False,

        "real_orders_reason":
        "REAL execution requires secure exchange API credentials; none are configured by default.",

        "live_adapters": [

            "binance",
            "bybit",
            "okx",
            "coinbase",
            "kraken",
            "bitget",
            "gateio",
            "mexc",
            "kucoin",
            "bitfinex",
            "cryptocom",
            "hyperliquid",
            "htx",
            "upbit",
            "poloniex",
            "coinex"

        ]

    }


@app.get("/api/sources")
async def sources():

    return {
        "sources": SOURCES
    }


@app.get("/api/trading-config")
async def trading_config():

    return {

        "demo_auto":
        True,

        "real_mode_available":
        True,

        "real_orders_enabled":
        False,

        "reason":
        "Real orders require secure exchange API credentials configured on the server."

    }


@app.get("/api/instruments")
async def instruments():

    return {

        "crypto":
        CRYPTO_SYMBOLS,

        "forex":
        FOREX_SYMBOLS,

        "metals":
        METAL_SYMBOLS

    }
