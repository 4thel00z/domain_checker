import argparse
import asyncio
import json
import pprint
import sys

import aiohttp

QUERY_URL = "https://api.domainsdb.info/search?query={query}"


async def _get_similiar_domains(*, query: str, loop):
    with aiohttp.ClientSession() as session:
        async with  session.get(QUERY_URL.format(query=query)) as response:
            return json.loads((await  response.content.read()).decode("UTF-8"))


def get_similiar_domains(*, query, loop):
    payload = loop.run_until_complete(_get_similiar_domains(query=query, loop=loop))
    return payload["domains"] if "domains" in payload else payload


if __name__ == '__main__':
    ARGS = argparse.ArgumentParser(description="GET url example")
    ARGS.add_argument('query', nargs=1, metavar='QUERY',
                      help="The name of the domain to look for")

    ARGS.add_argument('--print', default=True, action="store_true",
                      help="Print the result to stdout")

    ARGS.add_argument('--out',
                      help="Write the domains somewhere")

    options = ARGS.parse_args()
    asyncio.set_event_loop(None)
    loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
    try:
        result = get_similiar_domains(query=options.query.pop(), loop=loop)
    except:
        sys.exit(1)

    if options.print:
        pprint.pprint(result)

    if options.out:
        with open(options.out, mode="wb") as f:
            f.write(result)

    sys.exit(0)
