from sqlalchemy import Column, Integer, String, Text, JSON
from app.db.database import Base

class BrandInsights(Base):
    __tablename__ = "brand_insights"

    id = Column(Integer, primary_key=True, index=True)
    website_url = Column(String(255), nullable=False)
    product_catalog = Column(JSON)
    hero_products = Column(JSON)
    policies = Column(JSON)
    faqs = Column(JSON)
    social_links = Column(JSON)
    contact = Column(JSON)
    about = Column(Text)
