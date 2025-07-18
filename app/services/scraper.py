import requests
from bs4 import BeautifulSoup
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_store_insights(website_url: str):
    insights = {}

    if not website_url.startswith("http"):
        website_url = f"https://{website_url}"

    product_url = website_url.rstrip('/') + "/products.json"
    products_response = requests.get(product_url, headers=HEADERS)
    if products_response.status_code == 200:
        insights["product_catalog"] = products_response.json().get("products", [])
    else:
        return None

    # Fetch HTML content
    home_response = requests.get(website_url, headers=HEADERS)
    soup = BeautifulSoup(home_response.text, "html.parser")

    # Hero Products (basic implementation)
    insights["hero_products"] = [a.text.strip() for a in soup.find_all("a", href=re.compile("/products/"))][:5]

    # Social Handles
    social = {}
    for link in soup.find_all("a", href=True):
        href = link['href']
        if "instagram.com" in href:
            social["instagram"] = href
        elif "facebook.com" in href:
            social["facebook"] = href
        elif "tiktok.com" in href:
            social["tiktok"] = href
    insights["social_links"] = social

    # Contact Details
    contact = {"emails": [], "phones": []}
    text = soup.get_text()
    contact["emails"] = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    contact["phones"] = re.findall(r"\+?\d[\d -]{8,}\d", text)
    insights["contact"] = contact

    # About (try /about)
    try:
        about_page = requests.get(website_url + "/about", headers=HEADERS)
        about_soup = BeautifulSoup(about_page.text, "html.parser")
        insights["about"] = about_soup.get_text(" ", strip=True)[:500]
    except:
        insights["about"] = ""

    # Policies
    def fetch_policy(path):
        try:
            r = requests.get(website_url + path, headers=HEADERS)
            return BeautifulSoup(r.text, "html.parser").get_text(" ", strip=True)[:800]
        except:
            return ""
    insights["policies"] = {
        "privacy": fetch_policy("/policies/privacy-policy"),
        "return_refund": fetch_policy("/policies/refund-policy")
    }

    # FAQs (simple guess-based)
    faqs = []
    for question in soup.find_all(text=re.compile(r"\b(Do|How|What|Can|Why)\b.*\?")):
        parent = question.find_parent()
        answer = parent.find_next_sibling("p") if parent else None
        if answer:
            faqs.append({"question": question.strip(), "answer": answer.text.strip()})
    insights["faqs"] = faqs[:5]

    return insights