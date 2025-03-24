from database import engine, Base

# Create tables in SQLite
Base.metadata.create_all(bind=engine)

print("✅ Database & Tables Created Successfully!")