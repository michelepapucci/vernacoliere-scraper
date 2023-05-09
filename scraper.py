import requests
from bs4 import BeautifulSoup
import csv

url = "https://vernacoliere.com/category/articoli/"
page = requests.get(url)

with open("output.csv", "w") as output_file:
    writer = csv.writer(output_file, delimiter="\t")
    writer.writerow(['topic', 'title', 'subtitle', 'texts'])
    try:
        while(True):
            print(f"Scraping articles from {url}")
            soup = BeautifulSoup(page.content, "html.parser")

            article_div = soup.find("div", class_="tdb-numbered-pagination")

            article_links = article_div.find_all("a", class_="td-image-wrap")

            for link in article_links:
                topic_text = ""
                title_text = ""
                subtitle_text = ""
                text = ""

                article_page = requests.get(link["href"])
                print(f"Visiting {link['href']}...")
                article_soup = BeautifulSoup(article_page.content, "html.parser")
                title = article_soup.find("h1", class_="tdb-title-text")
                topic = article_soup.find("p", class_="occhiello2021-single")
                subtitle = article_soup.find("p", class_="sommario2021-single")
                if topic:
                    topic_text = topic.text.strip()
                    # print(topic_text)
                if title:
                    title_text = title.text.strip()
                    print(title_text)
                else:
                    print(f"Title not found in {link['href']}")
                if subtitle:
                    subtitle_text = subtitle.text.strip()
                    # print(subtitle_text)
                
                text_soup = article_soup.find("div", class_="tdb_single_content")
                if text_soup:
                    texts = text_soup.findAll("p")
                    if(texts and len(texts)>1):
                        for t in texts:
                            if len(t.text.strip()) > 75:
                                text += t.text.strip()
                            else:
                                print(t.text.strip())
            
                writer.writerow([topic_text.replace("\n", " "), title_text.replace("\n", " "), subtitle_text.replace("\n", " "), text.replace("\n", " ")])
            
            div_navigation = soup.find("div", class_="page-nav td-pb-padding-side")

            next_page = div_navigation.find_all("a")[-1]
            
            url = next_page['href']

            if url == "https://vernacoliere.com/category/articoli/page/98/":
                break;

            page = requests.get(url)
            print("\n\n")
    except KeyboardInterrupt as e:
        output_file.close()