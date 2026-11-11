from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import Survey

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Pokemon Survey"}


@app.get("/surveys/{id}")
async def read_surveys(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        survey = session.get(Survey, id)
        return {"message": survey}
    

@app.post("/surveys")
async def root(survey  : Survey):
    with Session(engine) as session:
        session.add(survey)
        session.commit()
        session.refresh(survey)
        return {"message": survey}
    
@app.get("/surveys")
async def get_surveys():
        with Session(engine) as session:
            surveys = session.exec(select(Survey)).all()
            return {"message": surveys}

        statement = select(Survey)
        results = session.exec(statement)

        # if(results)

        # print('-----------------------------')
        # print(Users.password , users.password)
        # print('-----------------------------')

        result = results.first()
        print(result)

        if (result == None):
            return {"status":"failed"}


        return {
            "status":"success",
            "data": result
            }
    
