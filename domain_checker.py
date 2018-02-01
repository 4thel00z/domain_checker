import argparse
import asyncio
import json
import pprint
import sys

import aiohttp

QUERY_URL = "https://api.domainsdb.info/search?query={query}"


async def _get_similiar_domains(*, options: argparse.Namespace, query: str, loop: asyncio.AbstractEventLoop):
    with aiohttp.ClientSession(loop=loop) as session:
        async with  session.get(QUERY_URL.format(query=query)) as response:
            if options.out:
                return await  response.content.read()
            return json.loads((await  response.content.read()).decode("UTF-8"))


def get_similiar_domains(*, options: argparse.Namespace, query: str, loop: asyncio.AbstractEventLoop):
    payload = loop.run_until_complete(_get_similiar_domains(options=options, query=query, loop=loop))
    return payload["domains"] if not options.out and "domains" in payload   else payload


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
    result = get_similiar_domains(options=options, query=options.query.pop(), loop=loop)

    if options.print:
        pprint.pprint(result)

    if options.out:
        with open(options.out, mode="wb") as f:
            f.write(result)

    sys.exit(0)
