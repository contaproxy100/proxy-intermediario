from proxy.http.proxy import HttpProxyBasePlugin
from proxy.common.utils import build_http_request
from typing import Optional

class UpstreamProxyPlugin(HttpProxyBasePlugin):
    def before_upstream_connection(self, request: build_http_request) -> Optional[str]:
        # Endereço do proxy upstream com autenticação
        return 'http://dolar2020:dolar2020@154.91.152.38:7777'
