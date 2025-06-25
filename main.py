from proxy import main

if __name__ == '__main__':
    main([
        '--hostname', '0.0.0.0',
        '--port', '3128',
        '--upstream-proxy', 'http://dolar2020:dolar2020@154.91.152.38:7777'
    ])
