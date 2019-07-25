import os


def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    process = os.popen("nmap {0} {1}".format(options, ip));
    results = str(process.read())
    return results


# print(get_nmap('-F', '54.221.207.100'))
