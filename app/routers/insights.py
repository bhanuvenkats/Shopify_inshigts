from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.scraper import fetch_store_insights
from app.db.database import SessionLocal
from app.db.schemas import BrandInsights
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)

class StoreRequest(BaseModel):
    website_url: str

# ✅ This is the missing part:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/extract-insights")
async def extract_insights(request: StoreRequest, db: Session = Depends(get_db)):
    try:
        data = fetch_store_insights(request.website_url)
        logging.info(f"Scraped data: {data}")

        if not data:
            raise HTTPException(status_code=401, detail="Invalid Shopify website or data not found")

        brand = BrandInsights(
            website_url=request.website_url,
            product_catalog=data.get("product_catalog"),
            hero_products=data.get("hero_products"),
            policies=data.get("policies"),
            faqs=data.get("faqs"),
            social_links=data.get("social_links"),
            contact=data.get("contact"),
            about=data.get("about")
        )

        db.add(brand)
        db.commit()
        db.refresh(brand)

        logging.info("Saved to DB")

        return {"message": "Data scraped and saved successfully", "data": data}

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
