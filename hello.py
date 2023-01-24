#!/usr/bin/env python3

import os
import json

# print('Content-Type: application/json')
print('Content-Type: text/html')
print()
# j = json.dumps(dict(os.environ), indent=2)
print(f"QUERY_STRING = {os.environ['QUERY_STRING']}")

# print(j)
