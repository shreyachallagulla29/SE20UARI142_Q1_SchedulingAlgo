def fcfs(ar_t,br_t):
    wtd = {}
    tat = []
    wt = []
    d = {}

    for i in range(len(ar_t)):
        d[ar_t[i]] = br_t[i]
    ar_tsort = sorted(ar_t)
    br_tsort = []
    for i in ar_tsort:
        br_tsort.append(d[i])
    current = 0

    for i in range(len(ar_tsort)):
        current = current + br_tsort[i]
        wtd[ar_tsort[i]] = current - ar_tsort[i] - br_tsort[i]
    for i in ar_t:
        wt.append(wtd[i])

    for i in range(len(wt)):
        tat.append(wt[i]+br_t[i])

    return sum(wt)/len(wt), sum(tat)/len(tat)


def sjf(ar_t, br_t):


    wt = [0] * len(ar_t)
    tat = [0] * len(ar_t)
    n = len(ar_t)
    done = [False] * n
    total_t = 0
    remaining_bt = br_t.copy()
    while True:
        min_bt = float('inf')
        short = -1
        for i in range(n):
            if not done[i] and ar_t[i] <= total_t and remaining_bt[i] < min_bt:
                min_bt = remaining_bt[i]
                short = i
        if short == -1:
            break

        done[short] = True
        total_t += br_t[short]
        wt[short] = total_t - ar_t[short] - br_t[short]
        tat[short] = wt[short] + br_t[short]
    return sum(wt)/len(wt), sum(tat)/len(tat)


def ps(ar_t, br_t, priority):

    n = len(ar_t)
    wt = [0] * n
    tat = [0] * n

    processes = [(i, ar_t[i], br_t[i], priority[i]) for i in range(n)]
    processes.sort(key=lambda x: x[3])
    tot_t = 0
    for i in range(n):
        p_id, arr_time, burst_time, _ = processes[i]
        if arr_time > tot_t:
            tot_t = arr_time
        wt[p_id] = tot_t - arr_time
        tot_t += burst_time
        tat[p_id] = wt[p_id] + burst_time
    return sum(wt)/len(wt), sum(tat)/len(tat)


def rr(ar_t, br_t, quant):

    n = len(ar_t)
    wt = [0] * n
    tat = [0] * n
    remaining_bt = br_t.copy()
    time = 0
    while any(remaining_bt):
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] <= quant:
                    time += remaining_bt[i]
                    wt[i] = time - ar_t[i] - br_t[i]
                    remaining_bt[i] = 0

                else:
                    time += quant
                    remaining_bt[i] -= quant
                tat[i] = wt[i] + br_t[i]
    return sum(wt)/len(wt), sum(tat)/len(tat)

def avgwt(wt):
    return sum(wt)/len(wt)

def avgtat(tat):
    return sum(tat)/len(tat)

ar_t = [0,4,5,6]
br_t = [24,3,3,12]
p = [3,1,4,2]

wt_fcfs,tat_fcfs = fcfs(ar_t,br_t)

wt_sjf,tat_sjf = sjf(ar_t,br_t)

wt_ps,tat_ps = ps(ar_t,br_t,p)

wt_rr,tat_rr = rr(ar_t,br_t,4)

wt_fcfs,tat_fcfs = fcfs(ar_t,br_t)
print([wt_fcfs,wt_sjf,wt_ps,wt_rr])
print([tat_fcfs,tat_sjf,tat_ps,tat_rr])