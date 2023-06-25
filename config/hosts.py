from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'127.0.0.1', 'config.urls', name='localhost'),
    host(r'api', 'config.api_urls', name='api'),
    host(r'admin', 'config.urls', name='admin'),
)