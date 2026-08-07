import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        url = "https://sakthikrishna-ai.streamlit.app/"
        print(f"Visiting {url} ...")
        
        try:
            # Visit the page and wait for it to load
            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # Streamlit sleep screen has a button with text containing "Wake up"
            # Let's search for any button containing "Wake up"
            wake_btn = page.locator("button:has-text('Wake up')")
            if await wake_btn.count() > 0 and await wake_btn.first.is_visible():
                print("App is in sleep mode. Clicking the 'Wake up' button...")
                await wake_btn.first.click()
                # Wait for the app to wake up and reload
                await page.wait_for_timeout(20000)
                print("Wake up signal sent.")
            else:
                print("App is already active and running.")
                
            # Stay on the page for 5 seconds to ensure WebSocket connection registers
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"An error occurred during visit: {e}")
        finally:
            await browser.close()
            print("Session closed.")

if __name__ == "__main__":
    asyncio.run(main())
