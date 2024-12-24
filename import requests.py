import requests

def get_status_code(url):
  """
  Fetches the HTTP status code of a given URL.

  Args:
    url: The URL to check.

  Returns:
    The HTTP status code as an integer, or None if an error occurs.
  """
  try:
    response = requests.get(url)
    return response.status_code
  except requests.exceptions.RequestException as e:
    print(f"Error fetching {url}: {e}")
    return None

def main():
  """
  Gets the HTTP status code for a list of URLs and logs the results.
  """
  urls = ["https://www.google.com/news", "https://www.example.com", "https://www.holman.com"]  # Add more URLs as needed

  for url in urls:
    status_code = get_status_code(url)
    if status_code:
      print(f"{url} returned {status_code}")

if __name__ == "__main__":
  main()