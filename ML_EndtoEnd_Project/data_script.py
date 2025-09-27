import os
import tarfile
import urllib.request # Changed this line

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Downloads and extracts the housing data TGZ file.
    """
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    
    print(f"Downloading data from {housing_url} to {tgz_path}")
    urllib.request.urlretrieve(housing_url, tgz_path)
    
    print("Extracting data...")
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    print("Data downloaded and extracted successfully.")

# Call the function to execute the download and extraction
fetch_housing_data()
