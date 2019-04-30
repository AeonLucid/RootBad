#include "daemon.c"
#include <stdio.h>

int main()
{
    run_daemon();

    while (1) {
        // TODO: Do daemon stuff..

        syslog(LOG_NOTICE, "RootBad Injector daemon started.");
        sleep(20);
        break;
    }

    syslog (LOG_NOTICE, "RootBad Injector daemon terminated.");
    closelog();

    return EXIT_SUCCESS;
}