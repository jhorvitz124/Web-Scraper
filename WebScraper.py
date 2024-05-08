import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(query):
    try:
        # Prepare the Wikipedia URL
        url = f"https://en.wikipedia.org/wiki/{query}"
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the main content of the page
        content = soup.find(id='mw-content-text')
        
        # Find the first paragraph in the content
        first_paragraph = content.find('p')
        
        # Extract the text from the first paragraph
        result = first_paragraph.get_text()
        
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    query = input("Enter what you want to search on Wikipedia: ")
    result = scrape_wikipedia(query)
    print(result)

if __name__ == "__main__":
    main()
