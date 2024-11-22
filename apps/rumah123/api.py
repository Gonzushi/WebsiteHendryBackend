from fastapi import APIRouter, HTTPException, Depends, Request
import aiohttp
import asyncio
import pandas as pd
from apps.rumah123 import crud, schemas

router = APIRouter(
    prefix="/rumah123",
    tags=["Rumah 123"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

# Session getter function for dependency injection
async def get_session(request: Request):
    return request.app.state.session

# Reset session function
async def reset_session(request: Request):
    """Reset the session in the app's state."""
    old_session = request.app.state.session
    await old_session.close()  # Close the old session
    session = aiohttp.ClientSession()  # Create a new session
    request.app.state.session = session  # Update app state with new session

# Main route to fetch data
@router.get("/", response_model=list[schemas.PropertyDetails])
async def get_data(
    request: Request, 
    base: str = "jual/depok/rumah",
    minPrice: int = 400_000_000,
    minLandArea: int = 150,
    minBuiltupSize: int = 300,
    maxLandArea: int = 2_000,
    maxBuiltupSize: int = 2_000,
    max_page: int = 0,
    session: aiohttp.ClientSession = Depends(get_session),
):
    df = await crud.main(
        session,
        base,
        minPrice,
        minLandArea,
        minBuiltupSize,
        maxLandArea,
        maxBuiltupSize,
        max_page,
    )

    # If dataframe is empty, reset session and retry
    if df.empty:
        print("-" * 130, "\n", session,"\n", "-" * 130)
        await reset_session(request)  # Reset the session in the app state
        session = request.app.state.session  # Get the new session
        print("-" * 130, "\n", session,"\n", "-" * 130)


        # Retry fetching the data with the new session
        df = await crud.main(
            session,
            base,
            minPrice,
            minLandArea,
            minBuiltupSize,
            maxLandArea,
            maxBuiltupSize,
            max_page,
        )

        # If still empty after retry, raise 404 error
        if df.empty:
            raise HTTPException(status_code=404, detail="No data found after retrying")

    return df.to_dict(orient="records")
