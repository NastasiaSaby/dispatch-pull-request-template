#!/usr/bin/python

import os
import sys
from urlparse import urlparse

if len(sys.argv) > 1:
   projectName = sys.argv[1]
else:
  projectName = raw_input("Git url : ")

split = projectName.split("/")

path = split[-1].replace(".git", "")

os.system('git clone {0}'.format(projectName))
os.system('cd {0} && git checkout -b feature/add-pull-request-template'.format(path))
os.system('cd {0} && echo "## Why?\n<!-- Explain the purpose of your modifications -->\n\n## How?\n<!-- Explain in few words your solution choices to help your team mates \"enter\" the code -->\n\n## US\n<!-- Paste the US link -->\n\n## MEP\n<!-- List what you have to do before deploying (if needed) -->\n* [x] TODO 1\n* [ ] TODO 2" > PULL_REQUEST_TEMPLATE.md'.format(path))
os.system('cd {0} && git add PULL_REQUEST_TEMPLATE.md'.format(path))
os.system('cd {0} && git commit -m "Add pull request template"'.format(path))
os.system('cd {0} && git push origin feature/add-pull-request-template'.format(path))
