#!/usr/bin/env python3

import sys
import base64

if len(sys.argv) < 2:
    print("No code to run")
    sys.exit(1)

try:
    code = base64.b64decode(sys.argv[1]).decode('utf-8')
except base64.binascii.Error:
    print("Error encountered running code")
    sys.exit(1)

if not code:
    print("Error encountered running code")
    sys.exit(1)

exec(code)
