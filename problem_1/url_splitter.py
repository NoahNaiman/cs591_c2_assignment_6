def url_split(url):
    protocol = ""
    domain = ""
    path = ""

    if url != "":
        split_url = url.split("/")
        split_url = [string for string in split_url if string != ""]
        
        protocol = split_url[0]
        if protocol[-1] == ":":
            protocol = protocol[:-1]

        domain = split_url[1]

        #Assume everything path domain is part of path, concat with "/"
        path = "/".join(split_url[2:])

    return protocol, domain, path
