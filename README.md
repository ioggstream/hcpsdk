HCPsdk
======

HCPsdk provides a simple SDK to access an Hitachi Content Platform (HCP)
from Python3. It handles name resolution, multiple sessions spread across all
available HCP nodes, persistent connections and recovery from failing
connections.

It's that easy:

    >>> import hcpsdk

    >>> # initialize an *Authorization* object
    >>> auth = hcpsdk.NativeAuthorization('user', 'password')

    >>> # initialize a *Target* object
    >>> t = hcpsdk.Target("namespace.tenant.hcp.your.domain",
                          auth, port=443)

    >>> # initialize a Connection to the `Target``
    >>> c = hcpsdk.Connection(t)

    >>> # do something with the connection...
    >>> r = c.GET('/rest/your_file.txt')
    >>> c.response_status, c.response_reason
    (200, 'OK')
    >>> r.read()
    b'some data...'
    >>>
    >>> c.close()


Features
--------

- Handles HCP as a target object
- Replica-aware (replica can be part of a target object)
- Various strategies on how to use a replica
- Connection objects, while tied to a target object, allow
  access to HCP through the various http/REST dialects
  (native, HS3, HSwift)
- Higher level modules provide easy access to namespace
  statistics and some MAPI functionality, along with
  the ability to create unique object names / paths

Documentation
-------------

Hosted at [readthedocs.org](http://hcpsdk.readthedocs.org)


Dependencies
------------

**hcpsdk** depends on these packages:

* [dnspython3](http://www.dnspython.org) -  Used for non-cached name
        resolution when bypassing the system's resolver.
* [sphinx](http://sphinx-doc.org) -  Used for local documentation
        builds from source code and \*.rst files.

Installation
------------

Install hcpsdk by running:

    $ pip install hcpsdk

-or-

get the source from
  [GitHub](https://github.com/Simont3/hcpsdk/archive/master.zip), unzip the archive and run:
    
    $ python setup.py install

-or-

fork at [Github](https://github.com/Simont3/hcpsdk)

Contribute
----------

* [Issue Tracker](https://github.com/simont3/hcpsdk/issues)
* [Source Code](https://github.com/Simont3/hcpsdk)

Support
-------

If you find any bugs, please let us know via the Issue Tracker;
if you have comments or suggestions, send an email to
[sw@snomis.de](mailto:sw@snomis.de)

License
-------

The MIT License (MIT)

Copyright (c) 2014-2015 Thorsten Simons (sw@snomis.de)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
