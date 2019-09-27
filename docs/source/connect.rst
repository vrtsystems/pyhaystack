Connecting to a haystack server
===============================

Using Niagara AX
----------------
::

    from pyhaystack.client.niagara import NiagaraHaystackSession
    session = NiagaraHaystackSession(uri='http://ip:port',
                                    username='user',
                                    password='myPassword',
                                    *pint=True)

Note that pint parameter is optionnal and default to False.

Using Widesky
--------------
::

    from pyhaystack.client.widesky import WideskyHaystackSession
    session = SkysparkHaystackSession(uri='http://ip:port',
                                    username='user',
                                    password='my_password',
                                    client_id = 'my_id',
                                    client_secret = 'my_secret',
                                    *pint=True,
                                    *impersonate = 'user_id')

Note that the impersonate parameter is optionnal and is default to None.

If the impersonate parameter is set and the caller has the required permission to act as the target user. Then all subsequent requests coming from this HTTP session will be based on the target user's READ/WRITE permissions.

Using Skyspark
--------------
::

    from pyhaystack.client.skyspark import SkysparkHaystackSession
    session = SkysparkHaystackSession(uri='http://ip:port',
                                    username='user',
                                    password='my_password',
                                    project = 'my_project',
                                    *pint=True)

On-Demand connection
---------------------
Once the session is initialized, it won't connect until it needs to.
Pyhaystack will benefit from the asynchronous framework and connect on demand.
The session will be connected and the request will be sent to the server.

If, when making a request, pyhaystack detects that it has been disconnected,
it will re-connect automatically.

See next section to know more about requests.
