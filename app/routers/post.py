from fastapi import Body, Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy import func
from typing import List, Optional
import schemas, models, oauth2
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/posts", tags=['Posts'])


# @router.get("/", response_model=List[schemas.Post])
@router.get("/")
def get_all_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = "",):
    """
    Get all posts with optional search query and pagination.
    """
    query = db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
    query = query.join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
    query = query.group_by(models.Post.id)
    query = query.filter(models.Post.title.contains(search))
    query = query.limit(limit)
    query = query.offset(skip)
    posts = query.all()
    # Convert the list of tuples into a list of dictionaries
    posts_dicts = [
        {
            "post": post.__dict__,
            "votes": votes,
        }
        for post, votes in posts
    ]
    return posts_dicts

# get a single post from posts table using id column (PK)
@router.get("/{id}") #response_model=List[schemas.PostOut]  ye wala kaam rh rha h abhi user ka relationship nhi banpaa rha hai modles me to email wala column nhi aa rha h abhi
def get_one_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).outerjoin(
        models.Vote, models.Vote.post_id == models.Post.id).group_by(
        models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"status": "Failure", "message": "id not found"})
    return {"post": post[0].__dict__, "votes": post[1]}




# create a new post in the posts table in database
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):  # we can also use def fun(post:Body(...))

    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# update posts
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    # write logic to find id
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "id not found"})

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perform this action")

    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    # write logic to update
    return post_query.first()



# delete a post from database using id
@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id not found")

    if post.owner_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perform this action")

    db.delete(post)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)