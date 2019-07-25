import os


def get_whois(url):
    command = "whois " + url[12:]
    process = os.popen(command)
    results = str(process.read())
    return results

# print(get_whois("https://www.reddit.com"))
