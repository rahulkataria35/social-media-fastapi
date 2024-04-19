from fastapi import Body, FastAPI, Response,status, HTTPException
from pydantic import BaseModel
from typing import Optional 
import psycopg2
from psycopg2.extras import RealDictCursor
import time

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True

# create app instance
app = FastAPI()

# try to connect database
while True:
    try:
        conn = psycopg2.connect(host='localhost', database= 'postgres',
                                user = 'postgres', password='rahul', cursor_factory=RealDictCursor )
        cursor = conn.cursor()
        print("Database Connection has been made....")
        break

    except Exception as error:
        print("Unable to connect to database")
        print("Error: ", error)
        time.sleep(2)


# check health status
@app.get("/status")
def root():
    return HTTPException(status_code=status.HTTP_200_OK, detail= {"status":"up"})


# get a single post from posts table using id column (PK)
@app.get("/posts/{id}")
def get_one_post(id:int):
    cursor.execute('''SELECT * FROM posts WHERE id = %s ''',(str(id)))
    data = cursor.fetchone()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= {"status":"Failure", "message": "id not found"})
    return {"status":"Success" ,"data": data}
        

# get all the data from posts table
@app.get("/posts")
def get_all_posts():
    cursor.execute('''SELECT * FROM posts ORDER BY id''')
    posts = cursor.fetchall()
    return {"msg":"S", "data":posts}

# create a new post in the posts table in database
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:Post):     # we can also use def fun(post:Body(...))
    
    cursor.execute('''INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *;''', (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"message": "Success",
            "data": new_post}


# delete a post from database using id
@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute('''DELETE FROM posts WHERE id = %s RETURNING *''',(str(id)))
    deleted_data = cursor.fetchone()
    conn.commit()

    if not deleted_data:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"msg":"not found"})
    
    # write logic
    return {"message": "Success",
            "data": deleted_data} 

# update posts
@app.put("/posts/{id}")
def update_post(id: int,post:Post):

    cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE ID = %s  RETURNING * 
                    """,(post.title, post.content, post.published, str(id)))
    updated_data = cursor.fetchone()
    conn.commit()
    # write logic to find id
    if updated_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg":"id not found"})
    
    # write logic to update
    return {'data':updated_data, "response":"Success"}




