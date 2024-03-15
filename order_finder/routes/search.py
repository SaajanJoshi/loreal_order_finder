from fastapi import APIRouter
router = APIRouter()


@router.get("/search_product/")
def search_product(product_name: str):
    return {"product_name": product_name}