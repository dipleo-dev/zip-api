from fastapi import APIRouter, Query
from .scripts.image_processing import run_script, parse_command_line_args

router = APIRouter()

@router.get("/createZip")
async def create_zip(source: str = Query(..., description="Path to the source directory"),
                     destination: str = Query(..., description="Path to the destination directory")):
    # Parse command-line arguments
    src_base, dest_base = parse_command_line_args(["-s", source, "-d", destination])
    
    # Call the script with the parsed source and destination directories
    run_script(src_base, dest_base)
    
    return {"message": "Zip and CSV creation initiated."}