from playwright.async_api import async_playwright, expect

async def check():
    async with async_playwright() as p:
        chrome = await p.chromium.launch(headless=False, slow_mo=1500)