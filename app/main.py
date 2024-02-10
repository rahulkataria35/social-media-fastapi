from fastapi import FastAPI,status, HTTPException
import uvicorn
import models
from database import engine
from routers import user, post, auth, vote
from fastapi.middleware.cors import CORSMiddleware


## below line is told the sqlalchemy to run the all the create commands to create tables when it start it up

# models.Base.metadata.create_all(bind=engine)     

## after using alembic we don't use this command   ## isko uncomment bhi kr sakte h koi dikkt nhi hai waise

# create app instance
app = FastAPI()

# origins = ["https://www.google.com", "https://www.youtube.com"]  # specific domains can access our apis

origins = ["*"]  ## if we want to set our APIs as Public means every domain can access it

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



# check health status
@app.get("/")
def root():
    return HTTPException(status_code=status.HTTP_200_OK, detail= {"status":"up"})


if __name__ == "__main__":
    uvicorn.run(app)




