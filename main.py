from fastapi import FastAPI
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler

app = FastAPI()

class RequestInput(BaseModel):
    url: str

@app.post("/scrape")
async def scrape(input: RequestInput):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=input.url)
    return {"html": result.html or result.markdown or "Failed to extract content"}