#!python
# -*- coding: utf-8 -*-
"""
VRT Widesky low-level Password mix-in.
"""
import json
import hszinc
from six import string_types
from .....util.asyncexc import AsynchronousException

class PasswordOpsMixin(object):
    """
    The Password operations mix-in implements low-level support for
    modifying the current Widesky user's password.
    """
    def updatePassword(self, newPassword, callback=None):
        """
        Change the current logged in user's password.

        If the update is successful then True is returned.
        Otherwise the AsynchronousException is reraised.

        :param newPassword: Password value.
        :param callback: The function to call after this operation
        is complete.
        """
        def onResp(response):
            if isinstance(response, AsynchronousException):
                response.reraise()

            return callback(True)

        headers = self._client.headers.copy()
        headers["Content-Type"] = "application/json"

        return self._post(uri='user/updatePassword',
                        callback=onResp,
                        body=json.dumps({ "newPassword": newPassword }),
                        headers=headers,
                        api=False)
