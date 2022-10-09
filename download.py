##### Registry file download #####
import requests

# Registry URL for assets (not projects)
url = "https://registry.verra.org/uiapi/asset/asset/search?$skip=0&count=true&$format=csv"

# Filter for assets
data_filter = {
    "program":"VCS",
    "issuanceTypeCodes":["ISSUE"]
}

# Rest is download process
headers = {
    "Content-Type": "application/json",
    "Host": "registry.verra.org",
    "Origin": "https://registry.verra.org",
    "Referrer": "https://registry.verra.org/app/search/vcs",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
print("Download Started ...")
req = requests.post(url, json = data_filter, headers = headers, stream = True)


with open("download.csv",'wb') as output_file:
    for chunk in req.iter_content(chunk_size=1025):
        if chunk:
            output_file.write(chunk)
 
print("Download Completed !!!")