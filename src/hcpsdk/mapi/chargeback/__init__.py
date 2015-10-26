# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) 2014-2015 Thorsten Simons (sw@snomis.de)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from datetime import datetime
from io import StringIO
import logging
import hcpsdk


__all__ = ['ChargebackError', 'ChargeBack']

logging.getLogger('hcpsdk.mapi.chargeback').addHandler(logging.NullHandler())

class ChargebackError(Exception):
    """
    Base Exception used by the *hcpsdk.mapi.Chargeback()* class.
    """
    def __init__(self, reason):
        """
        :param reason: An error description
        """
        self.args = (reason,)


class ChargeBack(object):
    '''
    Access to HCP chargeback reports
    '''

    C_TOTAL = 'total'
    C_DAY = 'day'
    C_HOUR = 'hour'
    C_ALL = [C_TOTAL, C_DAY, C_HOUR]

    def __init__(self, target, debuglevel=0):
        '''
        :param target:      an hcpsdk.Target object
        :param debuglevel:  0..9 (used in *http.client*)
        '''
        self.logger = logging.getLogger(__name__ + '.Chargeback')
        hcpsdk.checkport(target, hcpsdk.P_MAPI)
        self.target = target
        self.debuglevel = debuglevel
        self.connect_time = 0.0
        self.service_time = 0.0

        try:
            self.con = hcpsdk.Connection(self.target, debuglevel=self.debuglevel)
        except Exception as e:
            raise hcpsdk.HcpsdkError(str(e))


    def request(self, start=None, end=None, intervall=C_TOTAL):
        '''
        Request a chargeback report for
        :param start:       starttime (a datetime object)
        :param end:         endtime (a datetime object)
        :param intervall:   one out of [C_TOTAL, C_DAY, C_HOUR]
        :return:
        '''
        if start and type(start) != datetime:
            raise ValueError('start not of type(datetime.datetime)')
        else:
            self.start = start or datetime(1970,month=1,day=1,
                                           hour=0,minute=0,second=0)
        if end and type(end) != datetime:
            raise ValueError('end not of type(datetime.datetime)')
        else:
            self.end = end or datetime.now()
        if intervall not in ChargeBack.C_ALL:
            raise ValueError('interval not in {}'.format(ChargeBack.C_ALL))
        else:
            self.intervall = intervall




        # ToDo: remove test code
        return('{}')
