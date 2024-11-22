from fastapi import APIRouter, HTTPException
import asyncio

from apps.rumah123 import crud, schemas

router = APIRouter(
    prefix="/rumah123",
    tags=["Rumah 123"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.PropertyDetails])
def get_data(
    base: str = "jual/depok/rumah",
    minPrice: int = 400_000_000,
    minLandArea: int = 150,
    minBuiltupSize: int = 300,
    maxLandArea: int = 2_000,
    maxBuiltupSize: int = 2_000,
    max_page: int = 0,
):
    df = asyncio.run(
        crud.main(
            base,
            minPrice,
            minLandArea,
            minBuiltupSize,
            maxLandArea,
            maxBuiltupSize,
            max_page,
        )
    )

    if df is None:
        raise HTTPException(status_code=404, detail="Cannot retrieve data")

    print("Halo", type(df.to_json(orient="records")))
    return df.to_dict(orient="records")
