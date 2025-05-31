# backend/app/services/sacred_service.py
from fastapi import HTTPException

class SacredService:
    def __init__(self):
        self.sacred_elements = {
            "mantras": {
                "om": {"frequency": 432, "duration": 60},
                "gayatri": {"frequency": 528, "duration": 108}
            },
            "geometries": {
                "sri_yantra": True,
                "flower_of_life": True,
                "metatron_cube": True
            }
        }

    async def get_sacred_elements(self):
        try:
            return self.sacred_elements
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
