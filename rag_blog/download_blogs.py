"""Download the HTML content from the pages and save them as txt files."""
import os
from typing import List

from llama_index.readers.web import TrafilaturaWebReader


def download_and_save(url: str, dir_path: str) -> None:
    """Download the HTML content from the web page and save it as a markdown file."""
    # Extract a filename from the URL
    if url.endswith("/"):
        url = url[:-1]

    filename = url.split("/")[-1] + ".md"
    print(f"Downloading {url} into {filename}...")

    documents = TrafilaturaWebReader().load_data([url])

    # Write the content to a file
    filename = os.path.join(dir_path, filename)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(documents[0].text)


def download(pages: List[str]) -> str:
    """Download the HTML content from the pages and save them as txt files."""
    # Create the content/notion directory if it doesn't exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_dir, ".content", "blogs")
    os.makedirs(dir_path, exist_ok=True)
    for page in pages:
        download_and_save(page, dir_path)
    return dir_path


PAGES = [
    "https://mlops.community/building-the-future-with-llmops-the-main-challenges/",
]

if __name__ == "__main__":
    download(PAGES)
