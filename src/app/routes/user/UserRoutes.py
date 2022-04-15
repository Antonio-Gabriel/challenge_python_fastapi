from fastapi import APIRouter, status, Depends

from ...adapter import UserAdapter
from ...config import AuthMiddleware
from ...repositories import UserRepository
from ...decorators.Authorization import Authorization

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .schemas.UserResponseModel import (
    UserCreateModels,
    UserResponseModel,
    UserByIdResponseModel,
)

from .schemas.AuthSchema import AuthSchema, AuthResponseModel

from ...handlers import (
    AuthUserHandler,
    CreateUserHandler,
    UpdateUserHandler,
    DeleteUserHandler,
    GetAllUserHandlers,
    GetUsersByIdHandler,
    GetUserByNameHandler,
    GetUserByStateHandler,
)

user_routes = APIRouter(
    prefix="/api",
    tags=["User Staff"],
)


@user_routes.post("/auth", response_model=AuthResponseModel)
async def auth(credentials: AuthSchema):
    """Authenticate user"""

    auth_handle = AuthUserHandler(UserRepository)
    response = auth_handle.handle(
        email=credentials.email, password=credentials.password
    )
    error = response.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=jsonable_encoder(
                {
                    "detail": error,
                }
            ),
        )

    return {
        "access_token": AuthMiddleware.encode_token(
            response.get_value().user_type.value
        ),
        "token_type": "Bearer",
        "user": response.get_value(),
    }


@user_routes.get("/", response_model=UserResponseModel)
@Authorization("staff")
async def get(auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get all users"""
    user_handler = GetAllUserHandlers(UserRepository)
    result = user_handler.handle()

    return {"users": result.get_value()}


@user_routes.get("/search/", response_model=UserResponseModel)
@Authorization("staff")
async def get_by_name(name: str, auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get user by name"""
    filtered_user_handle = GetUserByNameHandler(UserRepository)
    results = filtered_user_handle.handle(name)

    return {"users": results.get_value()}


@user_routes.get("/actives", response_model=UserResponseModel)
@Authorization("staff")
async def get_by_actives(auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get all active users"""
    filtered_user_handle = GetUserByStateHandler(UserRepository)
    results = filtered_user_handle.handle(True)

    return {"users": results.get_value()}


@user_routes.get("/desactives", response_model=UserResponseModel)
@Authorization("staff")
async def get_by_desactive(auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get all desactive users"""
    filtered_user_handle = GetUserByStateHandler(UserRepository)
    results = filtered_user_handle.handle(False)

    return {"users": results.get_value()}


@user_routes.get("/{id}", response_model=UserByIdResponseModel)
@Authorization("staff")
async def get_by_id(id: str, auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get user by id"""
    user_handler = GetUsersByIdHandler(UserRepository)
    result = user_handler.handle(id)

    if result.get_value():
        return {"user": result.get_value()}

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "detail": {"msg": "User not found!"},
            }
        ),
    )


@user_routes.post("/create")
async def create(user_props: UserCreateModels):
    """Create user staff"""

    user_result = UserAdapter.create(
        name=user_props.name,
        email=user_props.email,
        surname=user_props.surname,
        password=user_props.password,
        city=user_props.city,
        state=user_props.state,
        user_type="staff",
    )

    error_entity = user_result.error_value()
    if error_entity:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error_entity},
                }
            ),
        )

    user_handler = CreateUserHandler(UserRepository)
    result = user_handler.handle(user_result.get_value())

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error},
                }
            ),
        )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            {
                "detail": {"msg": "Successfully user created!"},
            }
        ),
    )


@user_routes.put("/update/{id}")
@Authorization("staff")
async def update(
    id: str, user_props: UserCreateModels, auth=Depends(AuthMiddleware.auth_wrapper)
):
    """Update user staff"""

    user_result = UserAdapter.create(
        name=user_props.name,
        email=user_props.email,
        surname=user_props.surname,
        password=user_props.password,
        city=user_props.city,
        state=user_props.state,
        user_type="staff",
        id=id,
    )

    error_entity = user_result.error_value()
    if error_entity:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error_entity},
                }
            ),
        )

    user_handler = UpdateUserHandler(UserRepository)
    result = user_handler.handle(user_result.get_value())

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error},
                }
            ),
        )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            {
                "detail": {"msg": "Successfully user updated!"},
            }
        ),
    )


@user_routes.delete("/delete/{id}")
@Authorization("staff")
async def delete(id: str, auth=Depends(AuthMiddleware.auth_wrapper)):
    """Delete user staff"""

    user_handler = DeleteUserHandler(UserRepository)
    result = user_handler.handle(id)

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error},
                }
            ),
        )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            {
                "detail": {"msg": "Successfully user deleted!"},
            }
        ),
    )
