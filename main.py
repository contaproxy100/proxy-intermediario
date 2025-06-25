import sys
from proxy import main

if __name__ == '__main__':
    sys.argv = [
        'proxy.py',
        '--hostname', '0.0.0.0',
        '--port', '3128',
        '--plugins', 'upstream_plugin.UpstreamProxyPlugin'
    ]
    main()
