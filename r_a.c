
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define process_count (3)

typedef struct
{
    int timestamp[process_count];
    int deferred[process_count];
    int reply[process_count];
    int critical_section;
} P;

P p[process_count] = {0};

static void AcquireTimeS    tamp(int *timeStamp);
static RequestProcess(int pid, int req_pid);
static void ReplySend(int pid, int req_pid);
static void CSExecute(int pid);

void RequestCS(int pid, int *clock);
void ReceiveReqCS(int pid, int req_pid, int clock);
void ReceiveReplyCS(int pid, int fromProcessId);

void RequestCS(int pid, int *clock)
{
    AcquireTimeStamp(clock);

    p[pid].timestamp[pid] = *clock;

    printf("PROCESS (%d) {TIMESTAMP (%d)} ==> BROADCAST ==> REQUEST.\n", pid, *clock);
}

void ReceiveReqCS(int pid, int req_pid, int clock)
{
    printf("PROCESS (%d) {TIMESTAMP (%d)} ==> REQUEST ==> PROCESS (%d)  ## RECEIVED## .\n", req_pid, clock, pid);

    p[pid].timestamp[req_pid] = clock;

    RequestProcess(pid, req_pid);
}

void ReceiveReplyCS(int pid, int fromProcessId)
{
    int exe_cs = 1;

    p[pid].reply[fromProcessId] = 1;

    printf("PROCESS (%d) ==> REPLY ==> PROCESS (%d).\n", fromProcessId, pid);

    for (int i = 0; i < process_count; i++)
    {
        if ((i != pid) && (p[pid].reply[i] != 1))
        {
            exe_cs = 0;
        }
    }

    if (exe_cs == 1)
    {
        printf("PROCESS (%d) ==> REPLY from all others.\n", pid);
        CSExecute(pid);
    }
}

static RequestProcess(int pid, int req_pid)
{
    if ((p[pid].critical_section == 1) || (p[pid].timestamp[pid] != 0))
    {
        if (p[pid].timestamp[req_pid] < p[pid].timestamp[pid])
        {
            ReplySend(pid, req_pid);
        }
        else
        {
            p[pid].deferred[req_pid] = 1;
            printf("PROCESS (%d) ==> REQUEST ==> PROCESS (%d) ## DEFFERED ##.\n", req_pid, pid);
        }
    }
}

static void ReplySend(int pid, int req_pid)
{
    p[pid].timestamp[req_pid] = 0;
    p[pid].deferred[req_pid] = 0;
}

static void CSExecute(int pid)
{
    p[pid].critical_section = 1;
    printf("\nPROCESS (%d) ==>> ==>> ENTER Critical Section.\n", pid);
    sleep(1);
    printf("PROCESS (%d) ==>> EXECUTING <<== Critical Section.\n", pid);
    sleep(1);
    printf("PROCESS (%d) EXIT ==>> ==>> Critical Section.\n\n", pid);

    p[pid].critical_section = 0;

    for (int i = 0; i < process_count; i++)
    {
        if ((i != pid) && (p[pid].deferred[i] != 0))
        {
            ReplySend(pid, p[pid].deferred[i]);
            p[pid].deferred[i] = 0;
            p[pid].reply[i] = 0;
        }
    }
}

static void AcquireTimeStamp(int *timestamp)
{
    time_t tx = time(NULL);
    struct tm tm = *localtime(&tx);

    *timestamp = tm.tm_sec + tm.tm_min * 60 + tm.tm_hour * 60 * 60;
}

int main(void)
{
    int time[process_count] = {0};
    RequestCS(0, &time[0]);

    sleep(1);

    RequestCS(1, &time[1]);

    ReceiveReqCS(2, 1, time[1]);

    sleep(2);

    ReceiveReqCS(2, 0, time[1]);

    sleep(2);

    ReceiveReqCS(0, 1, time[1]);

    sleep(2);

    ReceiveReqCS(1, 0, time[0]);

    sleep(2);

    ReceiveReplyCS(0, 1);

    sleep(2);

    ReceiveReplyCS(1, 2);

    sleep(2);

    ReceiveReplyCS(0, 2);

    sleep(2);

    ReceiveReplyCS(1, 0);

    sleep(5);
}