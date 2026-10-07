from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

BASE = Path(__file__).resolve().parent
INDEX = BASE / "index.html"
app = FastAPI(title="AI Live Signal Bot V26 - Multi Source")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

SOURCES = [
 {"id":"binance","name":"Binance","category":"Crypto","status":"LIVE"},
 {"id":"bybit","name":"Bybit","category":"Crypto","status":"LIVE"},
 {"id":"okx","name":"OKX","category":"Crypto","status":"LIVE"},
 {"id":"coinbase","name":"Coinbase Exchange","category":"Crypto","status":"LIVE"},
 {"id":"kraken","name":"Kraken","category":"Crypto","status":"LIVE"},
]
for id_,name in [
 ("kucoin","KuCoin"),("bitget","Bitget"),("gateio","Gate.io"),("mexc","MEXC"),("bitfinex","Bitfinex"),("cryptocom","Crypto.com Exchange"),("deribit","Deribit"),("gemini","Gemini"),("hyperliquid","Hyperliquid"),("htx","HTX / Huobi"),("bitstamp","Bitstamp"),("bithumb","Bithumb"),("upbit","Upbit"),("phemex","Phemex"),("poloniex","Poloniex"),("dydx","dYdX"),("independentreserve","Independent Reserve"),("bitflyer","bitFlyer"),("coinex","CoinEx"),("lbank","LBank"),("whitebit","WhiteBIT"),("bitmart","BitMart"),("ascendex","AscendEX"),("coinw","CoinW"),("bingx","BingX")]:
    SOURCES.append({"id":id_,"name":name,"category":"Crypto","status":"LISTED"})
for id_,name,cat in [("oanda","OANDA","Forex / CFD"),("fxcm","FXCM","Forex / CFD"),("twelvedata","Twelve Data","Forex / Metals")]:
    SOURCES.append({"id":id_,"name":name,"category":cat,"status":"API KEY REQUIRED"})

CRYPTO={
 "binance":["BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","XRPUSDT","ADAUSDT","DOGEUSDT","AVAXUSDT","LINKUSDT","LTCUSDT"],
 "bybit":["BTCUSDT","ETHUSDT","SOLUSDT","XRPUSDT","DOGEUSDT","BNBUSDT","ADAUSDT","AVAXUSDT","LINKUSDT"],
 "okx":["BTC-USDT","ETH-USDT","SOL-USDT","XRP-USDT","DOGE-USDT","BNB-USDT","ADA-USDT","AVAX-USDT","LINK-USDT"],
 "coinbase":["BTC-USD","ETH-USD","SOL-USD","XRP-USD","DOGE-USD","ADA-USD","AVAX-USD","LINK-USD"],
 "kraken":["BTC/USD","ETH/USD","SOL/USD","XRP/USD","DOGE/USD","ADA/USD","AVAX/USD","LINK/USD"]}
FOREX=["EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","USDCHF","NZDUSD","EURGBP","EURJPY","GBPJPY"]
METALS=["XAUUSD","XAGUSD"]

@app.get("/")
async def home(): return FileResponse(INDEX)
@app.get("/api/health")
async def health(): return {"ok":True,"app":"AI Live Signal Bot V26","auto_trade":False,"live_adapters":["binance","bybit","okx","coinbase","kraken"]}
@app.get("/api/sources")
async def sources(): return {"sources":SOURCES}
@app.get("/api/instruments")
async def instruments(): return {"crypto":CRYPTO,"forex":FOREX,"metals":METALS}
