from ClusterShell.NodeSet import NodeSet
import json
import threading
import time
import datetime
import re
from apscheduler.schedulers.background import BackgroundScheduler
from utils.read_conf import read_conf
import math

run_end_scheduler = BackgroundScheduler()
_JOBID = read_conf()['slurm_sim']['first_jobid']
_TIMESPEED = read_conf()['slurm_sim']['timespeed']
GOBAL_LOCK = threading.Lock()


def get_jobid():
    GOBAL_LOCK.acquire()
    global _JOBID
    jobid = _JOBID
    _JOBID = _JOBID + 1
    GOBAL_LOCK.release()
    return jobid


def pd_check_to_run(idle_nodes, alloc_nodes, r_jobs, pd_jobs, fh_jobs):
    for jobid in pd_jobs.copy():
        cmd = {}
        cmd['submit_time'] = pd_jobs[jobid]['submit_time']
        cmd['nodelist'] = pd_jobs[jobid]['nodelist']
        cmd['real_runtime'] = pd_jobs[jobid]['real_runtime']
        cmd['username'] = pd_jobs[jobid]['username']
        cmd['exec_name'] = pd_jobs[jobid]['exec_name']
        res = srun(cmd, idle_nodes, alloc_nodes, jobid, r_jobs, pd_jobs, fh_jobs)
        if re.findall("run", res):
            GOBAL_LOCK.acquire()
            pd_jobs.pop(jobid)
            GOBAL_LOCK.release()


def sinfo(partition_name, idle_nodes, alloc_nodes):
    res = []
    if len(idle_nodes) > 0:
        res.append(
            {'partition_name': partition_name,
             'state': 'idle',
             'num': len(idle_nodes),
             'nodelist': str(idle_nodes)
             }
        )
    if len(alloc_nodes) > 0:
        res.append(
            {'partition_name': partition_name,
             'state': 'alloc',
             'num': len(alloc_nodes),
             'nodelist': str(alloc_nodes)
             }
        )
    return json.dumps(res)


# 分配节点
def distribution_nodes(nodelist, idle_nodes, alloc_nodes):
    GOBAL_LOCK.acquire()
    try:
        idle_nodes.remove(nodelist)
        alloc_nodes.update(nodelist)

    except KeyError:
        return False
    finally:
        GOBAL_LOCK.release()
    return True


# 释放节点的同时移除r_Jobs里面的这个任务同时在fh_jobs 添加完成的作业
def release_nodes(nodelist, idle_nodes, alloc_nodes, jobid, r_jobs, fh_jobs):

    GOBAL_LOCK.acquire()
    try:
        idle_nodes.update(nodelist)
        alloc_nodes.remove(nodelist)
        fh_jobs[jobid] = r_jobs.pop(jobid)
        fh_jobs[jobid]['end_time'] = (fh_jobs[jobid]['start_time'] + datetime.timedelta(seconds=_TIMESPEED *fh_jobs[jobid]['real_runtime'])).strftime("%Y%m%d %H%M%S")
        fh_jobs[jobid]['runtime'] = fh_jobs[jobid]['real_runtime'] * _TIMESPEED
        fh_jobs[jobid]['state'] = "COMP"
    except KeyError:
        return False
    finally:
        GOBAL_LOCK.release()
    return True


def squeue(r_jobs, pd_jobs):
    jobs = {}
    real_end_time = datetime.datetime.now()

    for key in r_jobs.copy():
        real_run_time = (real_end_time - r_jobs[key]['start_time']).seconds

        speed_end_time = r_jobs[key]['start_time'] + datetime.timedelta(seconds=_TIMESPEED*real_run_time)
        jobs[key] = {
            'nodelist': r_jobs[key]['nodelist'],
            'state': 'R',
            'runtime': str(speed_end_time - r_jobs[key]['start_time']),
            'username': r_jobs[key]['username'],
            'exec_name': r_jobs[key]['exec_name']
        }
    for key in pd_jobs.copy():
        jobs[key] = {
            'nodelist': pd_jobs[key]['nodelist'],
            'state': 'PD',
            'runtime': '00:00:00',
            'username': pd_jobs[key]['username'],
            'exec_name':pd_jobs[key]['exec_name']
        }

    return json.dumps(jobs)


def srun(cmd, idle_nodes, alloc_nodes, jobid, r_jobs, pd_jobs, fh_jobs):
    submit_time = cmd['submit_time']
    nodelist = cmd['nodelist']
    real_runtime = cmd['real_runtime']
    username = cmd['username']
    exec_name = cmd['exec_name']
    if idle_nodes.issuperset(nodelist):
        if distribution_nodes(nodelist, idle_nodes, alloc_nodes):
            start_time = datetime.datetime.now()
            run_date = start_time + datetime.timedelta(seconds=real_runtime)
            # threading.Timer(real_runtime,release_nodes,
            #                 (nodelist,idle_nodes,alloc_nodes,jobid,r_jobs,fh_jobs)).start()
            run_end_scheduler.add_job(release_nodes, "date",
                                      (nodelist, idle_nodes, alloc_nodes, jobid, r_jobs, fh_jobs),
                                      run_date=run_date)
            r_jobs[jobid] = {
                'state': 'R',
                'nodelist': nodelist,
                'start_time': start_time,
                'submit_time': submit_time,
                'real_runtime': real_runtime,
                'username': username,
                'exec_name': exec_name
            }
            return "run {}".format(jobid)
        else:
            pd_jobs[jobid] = {
                'state': 'PD',
                'nodelist': nodelist,
                'submit_time': submit_time,
                'real_runtime': real_runtime,
                'username': username,
                'exec_name': exec_name
            }

    else:
        pd_jobs[jobid] = {
            'state': 'PD',
            'nodelist': nodelist,
            'submit_time': submit_time,
            'real_runtime': real_runtime,
            'username': username,
            'exec_name':exec_name
        }
    return "wait {}".format(jobid)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    time.sleep(1)
    end_time = datetime.datetime.now()
    print(type((end_time - start_time).seconds))
