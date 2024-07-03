from fastapi import FastAPI
import uvicorn

from app.routers import news

# app = FastAPI()

app = FastAPI(
    title="AI based News Summary API (Revised for Assignment by C201049_Naimul)",
    version="0.2",
    description="This is the API documentation for News Summary generating by AI.",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Kalim Amzad",
        "url": "https://growwithdata.net",
        "email": "kalim.amzad.chy@gmail.com",
    },
    # license_info = {
    #     "name": "MIT License",
    #     "url": "https://opensource.org/licenses/MIT",
    # },
    redoc_url="/documentation",
    docs_url="/try",
)

# Connecting all others routersin the List to find in FastAPI documentation
app.include_router(news.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API (Revised for Assignment by C201049_Naimul)!"}

if __name__ == "__main__":
    # uvicorn.run("main:app", host="localhost", port=8001, reload=True)
    uvicorn.run("main:app", host="localhost", port=8011, reload=True)