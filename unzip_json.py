
from zipfile import Zipfile
def unzipJSONAndLoad(filepath):
    """
    Args:
        file: str, local .zip file, with classic gzip compression (default) on Windows

    Returns:
        geoJson: dict, for input into choropleth mapbox
    """

    with Zipfile(filepath) as zip:
        _j = zip.read(file.replace("zip", "json"))  # folder is named same as file inside of it
        geoJson = json.loads(_j.decode('utf-8'))

    return geoJson