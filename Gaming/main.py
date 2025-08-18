from spinner import spin
from checker import checking_results
from new import nxt

playing = True

while playing:
    result = spin()
    counts = checking_results()
    playing = nxt(counts)
