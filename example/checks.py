from netwell.checkers import URL, DNS, Port

URL('http://fsf.org') \
    .redirects_to('http://www.fsf.org/') \
    .title_matches('Free Software Foundation')
Port('fsf.org', 443).ssl_valid_for(days=3000)
DNS('fsf.org', 'www.fsf.org').resolves_to('208.118.235.131')


def custom_check(response, outcome):
    data = response.json()
    if data:
        outcome.fail('Other data expected')

URL('http://httpbin.org/get').check_response(custom_check)
