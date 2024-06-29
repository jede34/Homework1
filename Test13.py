is_available = False 

is_first_section = True
is_prev_sec_completed = True
is_prev_sec_graded = True

import pdb; pdb.set_trace()
if is_first_section:
    is_first_section = True
elif is_prev_sec_completed:
    if   is_prev_sec_graded: 
        is_available = True
else:
    print('penis')