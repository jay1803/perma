from pywb import replay_views, replay_resolvers, archiveloader, indexreader, archivalrouter, wburl, handlers
import perma.settings


# include guid in CDX requests
class Route(archivalrouter.Route):
    def _add_filters(self, wbrequest, matcher):
        wbrequest.custom_params['guid'] = matcher.group(1)

# prevent timestamp and mod getting added to rewritten urls
class Url(wburl.WbUrl):
    def to_str(self, **overrides):
        overrides['mod'] = ''
        overrides['timestamp'] = ''
        return wburl.WbUrl.to_str(self, **overrides)

    def _init_replay(self, url):
        self.url = url
        self.type = self.LATEST_REPLAY
        return True


def pywb_config():
    """
        Configure server.
    """
    index_server = indexreader.RemoteCDXServer(perma.settings.CDX_SERVER_URL)

    # Loads warcs specified in cdx from these locations
    resolvers = [replay_resolvers.PrefixResolver('file://')]

    # Create rewriting replay handler to rewrite records
    replayer = replay_views.RewritingReplayView(resolvers=resolvers,
                                                archiveloader=archiveloader.ArchiveLoader(),
                                                buffer_response=True,
                                                redir_to_exact=False)

    # Finally, create wb router
    return archivalrouter.ArchivalRequestRouter(
        {
            Route(r'([a-zA-Z0-9\-]+)', handlers.WBHandler(index_server, replayer)),
        },
        # Specify hostnames that pywb will be running on
        # This will help catch occasionally missed rewrites that fall-through to the host
        # (See archivalrouter.ReferRedirect)
        hostpaths=['http://localhost:8000/'],
        archivalurl_class=Url
    )