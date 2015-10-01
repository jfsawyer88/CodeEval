## Code Eval
## File Size

import sys
import os

sys.stdout.write(str(os.stat(sys.argv[1]).st_size) + "\n")
