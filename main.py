import requests

def searchfordirs(url, wordlist):
    with open(wordlist, 'r') as f:
        directories = f.read().splitlines()

    for directory in directories:
        full_url = f"{url}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Directory is FOUND!: {full_url}")
        elif response.status_code == 404:
            print(f"Not found: {full_url}")
        else:
            print(f"Status code: {response.status_code} for the page that could not get reached: {full_url}")

if __name__ == '__main__':
    url = input("Enter the URL to search directories on: ")
    wordlist = input("Enter the wordlist file name (must include directory names): ")
    searchfordirs(url, wordlist)
