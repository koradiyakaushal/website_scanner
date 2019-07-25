from tld import get_tld


def get_domain_name(url):
    domain_name = get_tld(url)
    # print(domain_name)
    return domain_name

# print(get_domain_name('https://youtube.com/'))
