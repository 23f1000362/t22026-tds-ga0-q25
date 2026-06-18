from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 186.14,
    "uptime_pct": 98.581,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 101.29,
    "uptime_pct": 99.287,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 195.57,
    "uptime_pct": 97.626,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 128.23,
    "uptime_pct": 97.459,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 142.22,
    "uptime_pct": 98.039,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 113.7,
    "uptime_pct": 98.617,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 193.29,
    "uptime_pct": 98.74,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 219.81,
    "uptime_pct": 98.405,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 145.86,
    "uptime_pct": 98.742,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 186.95,
    "uptime_pct": 98.704,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 192.66,
    "uptime_pct": 97.363,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 119.44,
    "uptime_pct": 97.811,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 232.68,
    "uptime_pct": 98.061,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 160.45,
    "uptime_pct": 97.674,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 224.45,
    "uptime_pct": 99.35,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 208.14,
    "uptime_pct": 98.939,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 181.96,
    "uptime_pct": 98.783,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 236.26,
    "uptime_pct": 98.053,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 230.54,
    "uptime_pct": 98.686,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 142.45,
    "uptime_pct": 97.475,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 213.96,
    "uptime_pct": 97.449,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 114.52,
    "uptime_pct": 97.749,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 150.57,
    "uptime_pct": 97.133,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 124.45,
    "uptime_pct": 97.858,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 133.9,
    "uptime_pct": 98.469,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 205.69,
    "uptime_pct": 98.637,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 140.03,
    "uptime_pct": 98.417,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 162.84,
    "uptime_pct": 98.087,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 153.08,
    "uptime_pct": 98.887,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 152.19,
    "uptime_pct": 97.563,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 103.18,
    "uptime_pct": 97.162,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 182.53,
    "uptime_pct": 99.419,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 150.37,
    "uptime_pct": 98.768,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 118.55,
    "uptime_pct": 98.675,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 159.25,
    "uptime_pct": 99.061,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 217.41,
    "uptime_pct": 97.747,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
