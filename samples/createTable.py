#!/usr/bin/python
#
# Copyright 2010 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Placemat sample program.

API features used:
    SHOW TABLES
"""


import sys


from placemat import ftclient


def main():
    if (len(sys.argv) > 1):
      auth_token = ftclient.GetAuthToken(sys.argv)
    else:
      auth_token = ftclient.GetAuthToken()
  
    ft = ftclient.FTClient(auth_token)
  
    print ft.runGetQuery('SHOW TABLES')


if __name__ == '__main__':
    main()
