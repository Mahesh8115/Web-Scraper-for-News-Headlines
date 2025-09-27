import requests
from bs4 import BeautifulSoup


def scrape_headlines(url, output_file="headlines.txt"):
    try:
        # Send GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request failed

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines (commonly <h2>, but may differ per site)
        headlines = []
        # checking common headline tags
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            text = tag.get_text(strip=True)
            if text:  # avoid empty text
                headlines.append(text)

        # Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            for line in headlines:
                f.write(line + "\n")

        print(f"✅ {len(headlines)} headlines saved to {output_file}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Example: BBC News
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
