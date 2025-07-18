from app.db.database import Base, engine
from app.db.schemas import BrandInsights

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
