from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from apps.env import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET

router = APIRouter(
    prefix="/google_auth",
    tags=["Google Auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    client_kwargs={
        "scope": "email openid profile",
        "redirect_url": "http://localhost:8000/auth",
    },
)

templates = Jinja2Templates(directory="apps/google_auth/templates")


@router.get("/")
def google_auth_home_page(request: Request):
    user = request.session.get("user")
    if user:
        return {"message": "Welcome"}

    return templates.TemplateResponse(name="home.html", context={"request": request})


@router.get("/login")
async def login(request: Request):
    url = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, url)


@router.get("/auth")
async def auth(request: Request):
    return {"message": "auth"}
    # try:
    #     token = await oauth.google.authorize_access_token(request)
    # except OAuthError as e:
    #     return templates.TemplateResponse(
    #         name="error.html", context={"request": request, "error": e.error}
    #     )
    # user = token.get("userinfo")
    # if user:
    #     request.session["user"] = dict(user)
    # return RedirectResponse("welcome")
