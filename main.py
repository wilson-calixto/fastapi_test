from typing import Optional

from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()
# The brainiac system ignore the first and last caracters on respose string
service_tags={"TR50278":"JQ8F2W2"}

#getServiceTagbySN/
@app.get("/getServiceTagbySN/{pallet_id}")
def read_item(pallet_id: str, q: Optional[str] = None):
    data = """<?xml version="1.0" encoding="utf-8"?>
    <string
    xmlns="http://sfis.tpvaoc.com/COMMON" >{}</string>
        """
    try:
        data = data.format(service_tags[pallet_id])
    except Exception as e:
        print (e)

    return Response(content=data, media_type="application/xml")
    
''' to run this code type: uvicorn main:app --reload'''