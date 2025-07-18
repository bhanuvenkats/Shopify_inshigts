from pydantic import BaseModel
from typing import List, Optional, Dict

class FAQ(BaseModel):
    question: str
    answer: str

class Contact(BaseModel):
    emails: List[str]
    phones: List[str]

class Policies(BaseModel):
    privacy: str
    return_refund: str

class Insights(BaseModel):
    product_catalog: List[Dict]
    hero_products: List[str]
    faqs: List[FAQ]
    social_links: Dict[str, str]
    contact: Contact
    about: str
    policies: Policies