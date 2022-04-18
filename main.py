import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.routes.user.UserRoutes import user_routes
from src.app.routes.teacher.TeacherRoutes import teacher_routes
from src.app.routes.course.CourseRoute import course_routes

app = FastAPI(redoc_url=False)

app.title = "WeDev Learning"
app.description = "Documentation of wedev learning"

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["About"])
def say_hello():
    """Greeting"""
    return {"msg": "The test of wedev software company"}


app.include_router(user_routes)
app.include_router(teacher_routes)
app.include_router(course_routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
