from medix.server import mcp
from medix.schemas import Entity
from dotenv import load_dotenv
import requests_cache
import requests
import logging
import os

requests_cache.install_cache("medix_cache", expire_after=600)
load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL")
RELEASE_ID = os.getenv("RELEASE_ID")

@mcp.tool()
def autocode(clinical_notes: str):
    """Autocode turns ambiguous clinical notes into standardised, computable and verifiable Mortality and Mobidity Statistics (MMS) codes."""
    
    if not clinical_notes:
        logging.error("Clinical notes are required for the request to be processed.")

    try:
        response = requests.get(
            f"{BASE_URL}/icd/release/11/{RELEASE_ID}/mms/autocode",
            headers={
                "Accept": "application/json",
                "Accept-Language": "en",
                "API-Version": "v2",
            },
            params={
                "searchText": clinical_notes
            }
        )
        if response.status_code == 404:
            logging.error("Search text did not return any results.")

        if response.status_code == 200:
            data = response.json()
            matching_text = data["matchingText"]
            code = data["theCode"]
            foundation_uri = data["foundationURI"]
            linearization_uri = data["linearizationURI"]
            match_level = data["matchLevel"]
            match_score = data["matchScore"]
            match_type = data["matchType"]
            return Entity(
                matching_text=matching_text,
                code=code,
                foundation_uri=foundation_uri,
                linearization_uri=linearization_uri,
                match_level=match_level,
                match_score=match_score,
                match_type=match_type
            )
            
    except Exception as e:
        logging.error(f"Search failed.\n{e}")