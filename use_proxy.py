from urllib import request


def get_proxy_response(url, data=None, header={}, proxy={}):
    """Get url data using proxy server.
    
    :param url:
    :param data: post data
    :param header: request header
    :param proxy: proxy server (key: protocol, value: proxy server address)
    :return: response data
    """
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)

    req = request.Request(url, data=data, headers=header)
    return opener.open(req).read()


def main():
    proxy = {'https':'192.168.123.210:8870', 'http':'192.168.123.208:9874'}
    res = get_proxy_response('https://www.google.com/', proxy=proxy)
    print('response : %s' % res.decode('utf-8'))


if __name__ == '__main__':
    main()