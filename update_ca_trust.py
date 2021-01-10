#!/usr/bin/env python3

import sys
import os
import subprocess
import shutil

src_file = os.path.abspath(sys.argv[1])
trust_path = '/etc/pki/ca-trust/source/anchors/'

def ca_trust():
  dest = shutil.copy(src_file, trust_path)
  subprocess.run(['/usr/bin/update-ca-trust', 'extract'])
ca_trust()
