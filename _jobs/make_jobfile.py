import random
from datetime import datetime
import pathlib
import string

this_dir = pathlib.Path(__file__).parent
keep_going = True
while keep_going:
    jobnum = random.randint(1000, 9999)
    year = datetime.utcnow().year
    jobid = f"{year}-{jobnum}"
    jobfile = this_dir / f"{jobid}.md"
    if not jobfile.exists():
        keep_going = False

with open(this_dir / "_template.md") as tmplt:
    template = string.Template(tmplt.read())

title = input("What is the job title for this job? ")
description = input("Finish this sentence: We are seeking a new teammate "
                    "to ... ")

with open(jobfile, mode='w') as f:
    f.write(template.substitute({
        'jobid': jobid,
        'jobtitle': title,
        'status': "open",
        'description': description,
    }))

print("Please add specific job requirements by editing the file at:\n"
      f"{jobfile.resolve()}")
# TODO: subprocess out a `git add $jobfile.resolve()`?
