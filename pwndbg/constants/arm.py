#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .constant import Constant

__NR_OABI_SYSCALL_BASE = Constant('__NR_OABI_SYSCALL_BASE',0x900000)
__NR_SYSCALL_BASE = Constant('__NR_SYSCALL_BASE',0)
__NR_restart_syscall = Constant('__NR_restart_syscall',(0+  0))
__NR_exit = Constant('__NR_exit',(0+  1))
__NR_fork = Constant('__NR_fork',(0+  2))
__NR_read = Constant('__NR_read',(0+  3))
__NR_write = Constant('__NR_write',(0+  4))
__NR_open = Constant('__NR_open',(0+  5))
__NR_close = Constant('__NR_close',(0+  6))
__NR_creat = Constant('__NR_creat',(0+  8))
__NR_link = Constant('__NR_link',(0+  9))
__NR_unlink = Constant('__NR_unlink',(0+ 10))
__NR_execve = Constant('__NR_execve',(0+ 11))
__NR_chdir = Constant('__NR_chdir',(0+ 12))
__NR_time = Constant('__NR_time',(0+ 13))
__NR_mknod = Constant('__NR_mknod',(0+ 14))
__NR_chmod = Constant('__NR_chmod',(0+ 15))
__NR_lchown = Constant('__NR_lchown',(0+ 16))
__NR_lseek = Constant('__NR_lseek',(0+ 19))
__NR_getpid = Constant('__NR_getpid',(0+ 20))
__NR_mount = Constant('__NR_mount',(0+ 21))
__NR_umount = Constant('__NR_umount',(0+ 22))
__NR_setuid = Constant('__NR_setuid',(0+ 23))
__NR_getuid = Constant('__NR_getuid',(0+ 24))
__NR_stime = Constant('__NR_stime',(0+ 25))
__NR_ptrace = Constant('__NR_ptrace',(0+ 26))
__NR_alarm = Constant('__NR_alarm',(0+ 27))
__NR_pause = Constant('__NR_pause',(0+ 29))
__NR_utime = Constant('__NR_utime',(0+ 30))
__NR_access = Constant('__NR_access',(0+ 33))
__NR_nice = Constant('__NR_nice',(0+ 34))
__NR_sync = Constant('__NR_sync',(0+ 36))
__NR_kill = Constant('__NR_kill',(0+ 37))
__NR_rename = Constant('__NR_rename',(0+ 38))
__NR_mkdir = Constant('__NR_mkdir',(0+ 39))
__NR_rmdir = Constant('__NR_rmdir',(0+ 40))
__NR_dup = Constant('__NR_dup',(0+ 41))
__NR_pipe = Constant('__NR_pipe',(0+ 42))
__NR_times = Constant('__NR_times',(0+ 43))
__NR_brk = Constant('__NR_brk',(0+ 45))
__NR_setgid = Constant('__NR_setgid',(0+ 46))
__NR_getgid = Constant('__NR_getgid',(0+ 47))
__NR_geteuid = Constant('__NR_geteuid',(0+ 49))
__NR_getegid = Constant('__NR_getegid',(0+ 50))
__NR_acct = Constant('__NR_acct',(0+ 51))
__NR_umount2 = Constant('__NR_umount2',(0+ 52))
__NR_ioctl = Constant('__NR_ioctl',(0+ 54))
__NR_fcntl = Constant('__NR_fcntl',(0+ 55))
__NR_setpgid = Constant('__NR_setpgid',(0+ 57))
__NR_umask = Constant('__NR_umask',(0+ 60))
__NR_chroot = Constant('__NR_chroot',(0+ 61))
__NR_ustat = Constant('__NR_ustat',(0+ 62))
__NR_dup2 = Constant('__NR_dup2',(0+ 63))
__NR_getppid = Constant('__NR_getppid',(0+ 64))
__NR_getpgrp = Constant('__NR_getpgrp',(0+ 65))
__NR_setsid = Constant('__NR_setsid',(0+ 66))
__NR_sigaction = Constant('__NR_sigaction',(0+ 67))
__NR_setreuid = Constant('__NR_setreuid',(0+ 70))
__NR_setregid = Constant('__NR_setregid',(0+ 71))
__NR_sigsuspend = Constant('__NR_sigsuspend',(0+ 72))
__NR_sigpending = Constant('__NR_sigpending',(0+ 73))
__NR_sethostname = Constant('__NR_sethostname',(0+ 74))
__NR_setrlimit = Constant('__NR_setrlimit',(0+ 75))
__NR_getrlimit = Constant('__NR_getrlimit',(0+ 76))
__NR_getrusage = Constant('__NR_getrusage',(0+ 77))
__NR_gettimeofday = Constant('__NR_gettimeofday',(0+ 78))
__NR_settimeofday = Constant('__NR_settimeofday',(0+ 79))
__NR_getgroups = Constant('__NR_getgroups',(0+ 80))
__NR_setgroups = Constant('__NR_setgroups',(0+ 81))
__NR_select = Constant('__NR_select',(0+ 82))
__NR_symlink = Constant('__NR_symlink',(0+ 83))
__NR_readlink = Constant('__NR_readlink',(0+ 85))
__NR_uselib = Constant('__NR_uselib',(0+ 86))
__NR_swapon = Constant('__NR_swapon',(0+ 87))
__NR_reboot = Constant('__NR_reboot',(0+ 88))
__NR_readdir = Constant('__NR_readdir',(0+ 89))
__NR_mmap = Constant('__NR_mmap',(0+ 90))
__NR_munmap = Constant('__NR_munmap',(0+ 91))
__NR_truncate = Constant('__NR_truncate',(0+ 92))
__NR_ftruncate = Constant('__NR_ftruncate',(0+ 93))
__NR_fchmod = Constant('__NR_fchmod',(0+ 94))
__NR_fchown = Constant('__NR_fchown',(0+ 95))
__NR_getpriority = Constant('__NR_getpriority',(0+ 96))
__NR_setpriority = Constant('__NR_setpriority',(0+ 97))
__NR_statfs = Constant('__NR_statfs',(0+ 99))
__NR_fstatfs = Constant('__NR_fstatfs',(0+100))
__NR_socketcall = Constant('__NR_socketcall',(0+102))
__NR_syslog = Constant('__NR_syslog',(0+103))
__NR_setitimer = Constant('__NR_setitimer',(0+104))
__NR_getitimer = Constant('__NR_getitimer',(0+105))
__NR_stat = Constant('__NR_stat',(0+106))
__NR_lstat = Constant('__NR_lstat',(0+107))
__NR_fstat = Constant('__NR_fstat',(0+108))
__NR_vhangup = Constant('__NR_vhangup',(0+111))
__NR_syscall = Constant('__NR_syscall',(0+113))
__NR_wait4 = Constant('__NR_wait4',(0+114))
__NR_swapoff = Constant('__NR_swapoff',(0+115))
__NR_sysinfo = Constant('__NR_sysinfo',(0+116))
__NR_ipc = Constant('__NR_ipc',(0+117))
__NR_fsync = Constant('__NR_fsync',(0+118))
__NR_sigreturn = Constant('__NR_sigreturn',(0+119))
__NR_clone = Constant('__NR_clone',(0+120))
__NR_setdomainname = Constant('__NR_setdomainname',(0+121))
__NR_uname = Constant('__NR_uname',(0+122))
__NR_adjtimex = Constant('__NR_adjtimex',(0+124))
__NR_mprotect = Constant('__NR_mprotect',(0+125))
__NR_sigprocmask = Constant('__NR_sigprocmask',(0+126))
__NR_init_module = Constant('__NR_init_module',(0+128))
__NR_delete_module = Constant('__NR_delete_module',(0+129))
__NR_quotactl = Constant('__NR_quotactl',(0+131))
__NR_getpgid = Constant('__NR_getpgid',(0+132))
__NR_fchdir = Constant('__NR_fchdir',(0+133))
__NR_bdflush = Constant('__NR_bdflush',(0+134))
__NR_sysfs = Constant('__NR_sysfs',(0+135))
__NR_personality = Constant('__NR_personality',(0+136))
__NR_setfsuid = Constant('__NR_setfsuid',(0+138))
__NR_setfsgid = Constant('__NR_setfsgid',(0+139))
__NR__llseek = Constant('__NR__llseek',(0+140))
__NR_getdents = Constant('__NR_getdents',(0+141))
__NR__newselect = Constant('__NR__newselect',(0+142))
__NR_flock = Constant('__NR_flock',(0+143))
__NR_msync = Constant('__NR_msync',(0+144))
__NR_readv = Constant('__NR_readv',(0+145))
__NR_writev = Constant('__NR_writev',(0+146))
__NR_getsid = Constant('__NR_getsid',(0+147))
__NR_fdatasync = Constant('__NR_fdatasync',(0+148))
__NR__sysctl = Constant('__NR__sysctl',(0+149))
__NR_mlock = Constant('__NR_mlock',(0+150))
__NR_munlock = Constant('__NR_munlock',(0+151))
__NR_mlockall = Constant('__NR_mlockall',(0+152))
__NR_munlockall = Constant('__NR_munlockall',(0+153))
__NR_sched_setparam = Constant('__NR_sched_setparam',(0+154))
__NR_sched_getparam = Constant('__NR_sched_getparam',(0+155))
__NR_sched_setscheduler = Constant('__NR_sched_setscheduler',(0+156))
__NR_sched_getscheduler = Constant('__NR_sched_getscheduler',(0+157))
__NR_sched_yield = Constant('__NR_sched_yield',(0+158))
__NR_sched_get_priority_max = Constant('__NR_sched_get_priority_max',(0+159))
__NR_sched_get_priority_min = Constant('__NR_sched_get_priority_min',(0+160))
__NR_sched_rr_get_interval = Constant('__NR_sched_rr_get_interval',(0+161))
__NR_nanosleep = Constant('__NR_nanosleep',(0+162))
__NR_mremap = Constant('__NR_mremap',(0+163))
__NR_setresuid = Constant('__NR_setresuid',(0+164))
__NR_getresuid = Constant('__NR_getresuid',(0+165))
__NR_poll = Constant('__NR_poll',(0+168))
__NR_nfsservctl = Constant('__NR_nfsservctl',(0+169))
__NR_setresgid = Constant('__NR_setresgid',(0+170))
__NR_getresgid = Constant('__NR_getresgid',(0+171))
__NR_prctl = Constant('__NR_prctl',(0+172))
__NR_rt_sigreturn = Constant('__NR_rt_sigreturn',(0+173))
__NR_rt_sigaction = Constant('__NR_rt_sigaction',(0+174))
__NR_rt_sigprocmask = Constant('__NR_rt_sigprocmask',(0+175))
__NR_rt_sigpending = Constant('__NR_rt_sigpending',(0+176))
__NR_rt_sigtimedwait = Constant('__NR_rt_sigtimedwait',(0+177))
__NR_rt_sigqueueinfo = Constant('__NR_rt_sigqueueinfo',(0+178))
__NR_rt_sigsuspend = Constant('__NR_rt_sigsuspend',(0+179))
__NR_pread64 = Constant('__NR_pread64',(0+180))
__NR_pwrite64 = Constant('__NR_pwrite64',(0+181))
__NR_chown = Constant('__NR_chown',(0+182))
__NR_getcwd = Constant('__NR_getcwd',(0+183))
__NR_capget = Constant('__NR_capget',(0+184))
__NR_capset = Constant('__NR_capset',(0+185))
__NR_sigaltstack = Constant('__NR_sigaltstack',(0+186))
__NR_sendfile = Constant('__NR_sendfile',(0+187))
__NR_vfork = Constant('__NR_vfork',(0+190))
__NR_ugetrlimit = Constant('__NR_ugetrlimit',(0+191))
__NR_mmap2 = Constant('__NR_mmap2',(0+192))
__NR_truncate64 = Constant('__NR_truncate64',(0+193))
__NR_ftruncate64 = Constant('__NR_ftruncate64',(0+194))
__NR_stat64 = Constant('__NR_stat64',(0+195))
__NR_lstat64 = Constant('__NR_lstat64',(0+196))
__NR_fstat64 = Constant('__NR_fstat64',(0+197))
__NR_lchown32 = Constant('__NR_lchown32',(0+198))
__NR_getuid32 = Constant('__NR_getuid32',(0+199))
__NR_getgid32 = Constant('__NR_getgid32',(0+200))
__NR_geteuid32 = Constant('__NR_geteuid32',(0+201))
__NR_getegid32 = Constant('__NR_getegid32',(0+202))
__NR_setreuid32 = Constant('__NR_setreuid32',(0+203))
__NR_setregid32 = Constant('__NR_setregid32',(0+204))
__NR_getgroups32 = Constant('__NR_getgroups32',(0+205))
__NR_setgroups32 = Constant('__NR_setgroups32',(0+206))
__NR_fchown32 = Constant('__NR_fchown32',(0+207))
__NR_setresuid32 = Constant('__NR_setresuid32',(0+208))
__NR_getresuid32 = Constant('__NR_getresuid32',(0+209))
__NR_setresgid32 = Constant('__NR_setresgid32',(0+210))
__NR_getresgid32 = Constant('__NR_getresgid32',(0+211))
__NR_chown32 = Constant('__NR_chown32',(0+212))
__NR_setuid32 = Constant('__NR_setuid32',(0+213))
__NR_setgid32 = Constant('__NR_setgid32',(0+214))
__NR_setfsuid32 = Constant('__NR_setfsuid32',(0+215))
__NR_setfsgid32 = Constant('__NR_setfsgid32',(0+216))
__NR_getdents64 = Constant('__NR_getdents64',(0+217))
__NR_pivot_root = Constant('__NR_pivot_root',(0+218))
__NR_mincore = Constant('__NR_mincore',(0+219))
__NR_madvise = Constant('__NR_madvise',(0+220))
__NR_fcntl64 = Constant('__NR_fcntl64',(0+221))
__NR_gettid = Constant('__NR_gettid',(0+224))
__NR_readahead = Constant('__NR_readahead',(0+225))
__NR_setxattr = Constant('__NR_setxattr',(0+226))
__NR_lsetxattr = Constant('__NR_lsetxattr',(0+227))
__NR_fsetxattr = Constant('__NR_fsetxattr',(0+228))
__NR_getxattr = Constant('__NR_getxattr',(0+229))
__NR_lgetxattr = Constant('__NR_lgetxattr',(0+230))
__NR_fgetxattr = Constant('__NR_fgetxattr',(0+231))
__NR_listxattr = Constant('__NR_listxattr',(0+232))
__NR_llistxattr = Constant('__NR_llistxattr',(0+233))
__NR_flistxattr = Constant('__NR_flistxattr',(0+234))
__NR_removexattr = Constant('__NR_removexattr',(0+235))
__NR_lremovexattr = Constant('__NR_lremovexattr',(0+236))
__NR_fremovexattr = Constant('__NR_fremovexattr',(0+237))
__NR_tkill = Constant('__NR_tkill',(0+238))
__NR_sendfile64 = Constant('__NR_sendfile64',(0+239))
__NR_futex = Constant('__NR_futex',(0+240))
__NR_sched_setaffinity = Constant('__NR_sched_setaffinity',(0+241))
__NR_sched_getaffinity = Constant('__NR_sched_getaffinity',(0+242))
__NR_io_setup = Constant('__NR_io_setup',(0+243))
__NR_io_destroy = Constant('__NR_io_destroy',(0+244))
__NR_io_getevents = Constant('__NR_io_getevents',(0+245))
__NR_io_submit = Constant('__NR_io_submit',(0+246))
__NR_io_cancel = Constant('__NR_io_cancel',(0+247))
__NR_exit_group = Constant('__NR_exit_group',(0+248))
__NR_lookup_dcookie = Constant('__NR_lookup_dcookie',(0+249))
__NR_epoll_create = Constant('__NR_epoll_create',(0+250))
__NR_epoll_ctl = Constant('__NR_epoll_ctl',(0+251))
__NR_epoll_wait = Constant('__NR_epoll_wait',(0+252))
__NR_remap_file_pages = Constant('__NR_remap_file_pages',(0+253))
__NR_set_tid_address = Constant('__NR_set_tid_address',(0+256))
__NR_timer_create = Constant('__NR_timer_create',(0+257))
__NR_timer_settime = Constant('__NR_timer_settime',(0+258))
__NR_timer_gettime = Constant('__NR_timer_gettime',(0+259))
__NR_timer_getoverrun = Constant('__NR_timer_getoverrun',(0+260))
__NR_timer_delete = Constant('__NR_timer_delete',(0+261))
__NR_clock_settime = Constant('__NR_clock_settime',(0+262))
__NR_clock_gettime = Constant('__NR_clock_gettime',(0+263))
__NR_clock_getres = Constant('__NR_clock_getres',(0+264))
__NR_clock_nanosleep = Constant('__NR_clock_nanosleep',(0+265))
__NR_statfs64 = Constant('__NR_statfs64',(0+266))
__NR_fstatfs64 = Constant('__NR_fstatfs64',(0+267))
__NR_tgkill = Constant('__NR_tgkill',(0+268))
__NR_utimes = Constant('__NR_utimes',(0+269))
__NR_arm_fadvise64_64 = Constant('__NR_arm_fadvise64_64',(0+270))
__NR_pciconfig_iobase = Constant('__NR_pciconfig_iobase',(0+271))
__NR_pciconfig_read = Constant('__NR_pciconfig_read',(0+272))
__NR_pciconfig_write = Constant('__NR_pciconfig_write',(0+273))
__NR_mq_open = Constant('__NR_mq_open',(0+274))
__NR_mq_unlink = Constant('__NR_mq_unlink',(0+275))
__NR_mq_timedsend = Constant('__NR_mq_timedsend',(0+276))
__NR_mq_timedreceive = Constant('__NR_mq_timedreceive',(0+277))
__NR_mq_notify = Constant('__NR_mq_notify',(0+278))
__NR_mq_getsetattr = Constant('__NR_mq_getsetattr',(0+279))
__NR_waitid = Constant('__NR_waitid',(0+280))
__NR_socket = Constant('__NR_socket',(0+281))
__NR_bind = Constant('__NR_bind',(0+282))
__NR_connect = Constant('__NR_connect',(0+283))
__NR_listen = Constant('__NR_listen',(0+284))
__NR_accept = Constant('__NR_accept',(0+285))
__NR_getsockname = Constant('__NR_getsockname',(0+286))
__NR_getpeername = Constant('__NR_getpeername',(0+287))
__NR_socketpair = Constant('__NR_socketpair',(0+288))
__NR_send = Constant('__NR_send',(0+289))
__NR_sendto = Constant('__NR_sendto',(0+290))
__NR_recv = Constant('__NR_recv',(0+291))
__NR_recvfrom = Constant('__NR_recvfrom',(0+292))
__NR_shutdown = Constant('__NR_shutdown',(0+293))
__NR_setsockopt = Constant('__NR_setsockopt',(0+294))
__NR_getsockopt = Constant('__NR_getsockopt',(0+295))
__NR_sendmsg = Constant('__NR_sendmsg',(0+296))
__NR_recvmsg = Constant('__NR_recvmsg',(0+297))
__NR_semop = Constant('__NR_semop',(0+298))
__NR_semget = Constant('__NR_semget',(0+299))
__NR_semctl = Constant('__NR_semctl',(0+300))
__NR_msgsnd = Constant('__NR_msgsnd',(0+301))
__NR_msgrcv = Constant('__NR_msgrcv',(0+302))
__NR_msgget = Constant('__NR_msgget',(0+303))
__NR_msgctl = Constant('__NR_msgctl',(0+304))
__NR_shmat = Constant('__NR_shmat',(0+305))
__NR_shmdt = Constant('__NR_shmdt',(0+306))
__NR_shmget = Constant('__NR_shmget',(0+307))
__NR_shmctl = Constant('__NR_shmctl',(0+308))
__NR_add_key = Constant('__NR_add_key',(0+309))
__NR_request_key = Constant('__NR_request_key',(0+310))
__NR_keyctl = Constant('__NR_keyctl',(0+311))
__NR_semtimedop = Constant('__NR_semtimedop',(0+312))
__NR_vserver = Constant('__NR_vserver',(0+313))
__NR_ioprio_set = Constant('__NR_ioprio_set',(0+314))
__NR_ioprio_get = Constant('__NR_ioprio_get',(0+315))
__NR_inotify_init = Constant('__NR_inotify_init',(0+316))
__NR_inotify_add_watch = Constant('__NR_inotify_add_watch',(0+317))
__NR_inotify_rm_watch = Constant('__NR_inotify_rm_watch',(0+318))
__NR_mbind = Constant('__NR_mbind',(0+319))
__NR_get_mempolicy = Constant('__NR_get_mempolicy',(0+320))
__NR_set_mempolicy = Constant('__NR_set_mempolicy',(0+321))
__NR_openat = Constant('__NR_openat',(0+322))
__NR_mkdirat = Constant('__NR_mkdirat',(0+323))
__NR_mknodat = Constant('__NR_mknodat',(0+324))
__NR_fchownat = Constant('__NR_fchownat',(0+325))
__NR_futimesat = Constant('__NR_futimesat',(0+326))
__NR_fstatat64 = Constant('__NR_fstatat64',(0+327))
__NR_unlinkat = Constant('__NR_unlinkat',(0+328))
__NR_renameat = Constant('__NR_renameat',(0+329))
__NR_linkat = Constant('__NR_linkat',(0+330))
__NR_symlinkat = Constant('__NR_symlinkat',(0+331))
__NR_readlinkat = Constant('__NR_readlinkat',(0+332))
__NR_fchmodat = Constant('__NR_fchmodat',(0+333))
__NR_faccessat = Constant('__NR_faccessat',(0+334))
__NR_unshare = Constant('__NR_unshare',(0+337))
__NR_set_robust_list = Constant('__NR_set_robust_list',(0+338))
__NR_get_robust_list = Constant('__NR_get_robust_list',(0+339))
__NR_splice = Constant('__NR_splice',(0+340))
__NR_arm_sync_file_range = Constant('__NR_arm_sync_file_range',(0+341))
__NR_tee = Constant('__NR_tee',(0+342))
__NR_vmsplice = Constant('__NR_vmsplice',(0+343))
__NR_move_pages = Constant('__NR_move_pages',(0+344))
__NR_getcpu = Constant('__NR_getcpu',(0+345))
__NR_kexec_load = Constant('__NR_kexec_load',(0+347))
__NR_utimensat = Constant('__NR_utimensat',(0+348))
__NR_signalfd = Constant('__NR_signalfd',(0+349))
__NR_timerfd = Constant('__NR_timerfd',(0+350))
__NR_eventfd = Constant('__NR_eventfd',(0+351))
__NR_fallocate = Constant('__NR_fallocate',(0+352))
__NR_timerfd_settime = Constant('__NR_timerfd_settime',(0+353))
__NR_timerfd_gettime = Constant('__NR_timerfd_gettime',(0+354))
__SYS_NERR = Constant('__SYS_NERR',((129) + 1))
_SYS_TIME_H = Constant('_SYS_TIME_H',1)
SYS_accept = Constant('SYS_accept',(0+285))
SYS_access = Constant('SYS_access',(0+ 33))
SYS_acct = Constant('SYS_acct',(0+ 51))
SYS_add_key = Constant('SYS_add_key',(0+309))
SYS_adjtimex = Constant('SYS_adjtimex',(0+124))
SYS_alarm = Constant('SYS_alarm',(0+ 27))
SYS_arm_fadvise64_64 = Constant('SYS_arm_fadvise64_64',(0+270))
SYS_arm_sync_file_range = Constant('SYS_arm_sync_file_range',(0+341))
SYS_bdflush = Constant('SYS_bdflush',(0+134))
SYS_bind = Constant('SYS_bind',(0+282))
SYS_brk = Constant('SYS_brk',(0+ 45))
SYS_capget = Constant('SYS_capget',(0+184))
SYS_capset = Constant('SYS_capset',(0+185))
SYS_chdir = Constant('SYS_chdir',(0+ 12))
SYS_chmod = Constant('SYS_chmod',(0+ 15))
SYS_chown = Constant('SYS_chown',(0+182))
SYS_chown32 = Constant('SYS_chown32',(0+212))
SYS_chroot = Constant('SYS_chroot',(0+ 61))
SYS_clock_getres = Constant('SYS_clock_getres',(0+264))
SYS_clock_gettime = Constant('SYS_clock_gettime',(0+263))
SYS_clock_nanosleep = Constant('SYS_clock_nanosleep',(0+265))
SYS_clock_settime = Constant('SYS_clock_settime',(0+262))
SYS_clone = Constant('SYS_clone',(0+120))
SYS_close = Constant('SYS_close',(0+  6))
SYS_connect = Constant('SYS_connect',(0+283))
SYS_creat = Constant('SYS_creat',(0+  8))
SYS_delete_module = Constant('SYS_delete_module',(0+129))
SYS_dup = Constant('SYS_dup',(0+ 41))
SYS_dup2 = Constant('SYS_dup2',(0+ 63))
SYS_epoll_create = Constant('SYS_epoll_create',(0+250))
SYS_epoll_ctl = Constant('SYS_epoll_ctl',(0+251))
SYS_epoll_wait = Constant('SYS_epoll_wait',(0+252))
SYS_eventfd = Constant('SYS_eventfd',(0+351))
SYS_execve = Constant('SYS_execve',(0+ 11))
SYS_exit = Constant('SYS_exit',(0+  1))
SYS_exit_group = Constant('SYS_exit_group',(0+248))
SYS_faccessat = Constant('SYS_faccessat',(0+334))
SYS_fallocate = Constant('SYS_fallocate',(0+352))
SYS_fchdir = Constant('SYS_fchdir',(0+133))
SYS_fchmod = Constant('SYS_fchmod',(0+ 94))
SYS_fchmodat = Constant('SYS_fchmodat',(0+333))
SYS_fchown = Constant('SYS_fchown',(0+ 95))
SYS_fchown32 = Constant('SYS_fchown32',(0+207))
SYS_fchownat = Constant('SYS_fchownat',(0+325))
SYS_fcntl = Constant('SYS_fcntl',(0+ 55))
SYS_fcntl64 = Constant('SYS_fcntl64',(0+221))
SYS_fdatasync = Constant('SYS_fdatasync',(0+148))
SYS_fgetxattr = Constant('SYS_fgetxattr',(0+231))
SYS_flistxattr = Constant('SYS_flistxattr',(0+234))
SYS_flock = Constant('SYS_flock',(0+143))
SYS_fork = Constant('SYS_fork',(0+  2))
SYS_fremovexattr = Constant('SYS_fremovexattr',(0+237))
SYS_fsetxattr = Constant('SYS_fsetxattr',(0+228))
SYS_fstat = Constant('SYS_fstat',(0+108))
SYS_fstat64 = Constant('SYS_fstat64',(0+197))
SYS_fstatat64 = Constant('SYS_fstatat64',(0+327))
SYS_fstatfs = Constant('SYS_fstatfs',(0+100))
SYS_fstatfs64 = Constant('SYS_fstatfs64',(0+267))
SYS_fsync = Constant('SYS_fsync',(0+118))
SYS_ftruncate = Constant('SYS_ftruncate',(0+ 93))
SYS_ftruncate64 = Constant('SYS_ftruncate64',(0+194))
SYS_futex = Constant('SYS_futex',(0+240))
SYS_futimesat = Constant('SYS_futimesat',(0+326))
SYS_getcpu = Constant('SYS_getcpu',(0+345))
SYS_getcwd = Constant('SYS_getcwd',(0+183))
SYS_getdents = Constant('SYS_getdents',(0+141))
SYS_getdents64 = Constant('SYS_getdents64',(0+217))
SYS_getegid = Constant('SYS_getegid',(0+ 50))
SYS_getegid32 = Constant('SYS_getegid32',(0+202))
SYS_geteuid = Constant('SYS_geteuid',(0+ 49))
SYS_geteuid32 = Constant('SYS_geteuid32',(0+201))
SYS_getgid = Constant('SYS_getgid',(0+ 47))
SYS_getgid32 = Constant('SYS_getgid32',(0+200))
SYS_getgroups = Constant('SYS_getgroups',(0+ 80))
SYS_getgroups32 = Constant('SYS_getgroups32',(0+205))
SYS_getitimer = Constant('SYS_getitimer',(0+105))
SYS_get_mempolicy = Constant('SYS_get_mempolicy',(0+320))
SYS_getpeername = Constant('SYS_getpeername',(0+287))
SYS_getpgid = Constant('SYS_getpgid',(0+132))
SYS_getpgrp = Constant('SYS_getpgrp',(0+ 65))
SYS_getpid = Constant('SYS_getpid',(0+ 20))
SYS_getppid = Constant('SYS_getppid',(0+ 64))
SYS_getpriority = Constant('SYS_getpriority',(0+ 96))
SYS_getresgid = Constant('SYS_getresgid',(0+171))
SYS_getresgid32 = Constant('SYS_getresgid32',(0+211))
SYS_getresuid = Constant('SYS_getresuid',(0+165))
SYS_getresuid32 = Constant('SYS_getresuid32',(0+209))
SYS_getrlimit = Constant('SYS_getrlimit',(0+ 76))
SYS_get_robust_list = Constant('SYS_get_robust_list',(0+339))
SYS_getrusage = Constant('SYS_getrusage',(0+ 77))
SYS_getsid = Constant('SYS_getsid',(0+147))
SYS_getsockname = Constant('SYS_getsockname',(0+286))
SYS_getsockopt = Constant('SYS_getsockopt',(0+295))
SYS_gettid = Constant('SYS_gettid',(0+224))
SYS_gettimeofday = Constant('SYS_gettimeofday',(0+ 78))
SYS_getuid = Constant('SYS_getuid',(0+ 24))
SYS_getuid32 = Constant('SYS_getuid32',(0+199))
SYS_getxattr = Constant('SYS_getxattr',(0+229))
SYS_init_module = Constant('SYS_init_module',(0+128))
SYS_inotify_add_watch = Constant('SYS_inotify_add_watch',(0+317))
SYS_inotify_init = Constant('SYS_inotify_init',(0+316))
SYS_inotify_rm_watch = Constant('SYS_inotify_rm_watch',(0+318))
SYS_io_cancel = Constant('SYS_io_cancel',(0+247))
SYS_ioctl = Constant('SYS_ioctl',(0+ 54))
SYS_io_destroy = Constant('SYS_io_destroy',(0+244))
SYS_io_getevents = Constant('SYS_io_getevents',(0+245))
SYS_ioprio_get = Constant('SYS_ioprio_get',(0+315))
SYS_ioprio_set = Constant('SYS_ioprio_set',(0+314))
SYS_io_setup = Constant('SYS_io_setup',(0+243))
SYS_io_submit = Constant('SYS_io_submit',(0+246))
SYS_ipc = Constant('SYS_ipc',(0+117))
SYS_kexec_load = Constant('SYS_kexec_load',(0+347))
SYS_keyctl = Constant('SYS_keyctl',(0+311))
SYS_kill = Constant('SYS_kill',(0+ 37))
SYS_lchown = Constant('SYS_lchown',(0+ 16))
SYS_lchown32 = Constant('SYS_lchown32',(0+198))
SYS_lgetxattr = Constant('SYS_lgetxattr',(0+230))
SYS_link = Constant('SYS_link',(0+  9))
SYS_linkat = Constant('SYS_linkat',(0+330))
SYS_listen = Constant('SYS_listen',(0+284))
SYS_listxattr = Constant('SYS_listxattr',(0+232))
SYS_llistxattr = Constant('SYS_llistxattr',(0+233))
SYS__llseek = Constant('SYS__llseek',(0+140))
SYS_lookup_dcookie = Constant('SYS_lookup_dcookie',(0+249))
SYS_lremovexattr = Constant('SYS_lremovexattr',(0+236))
SYS_lseek = Constant('SYS_lseek',(0+ 19))
SYS_lsetxattr = Constant('SYS_lsetxattr',(0+227))
SYS_lstat = Constant('SYS_lstat',(0+107))
SYS_lstat64 = Constant('SYS_lstat64',(0+196))
SYS_madvise = Constant('SYS_madvise',(0+220))
SYS_mbind = Constant('SYS_mbind',(0+319))
SYS_mincore = Constant('SYS_mincore',(0+219))
SYS_mkdir = Constant('SYS_mkdir',(0+ 39))
SYS_mkdirat = Constant('SYS_mkdirat',(0+323))
SYS_mknod = Constant('SYS_mknod',(0+ 14))
SYS_mknodat = Constant('SYS_mknodat',(0+324))
SYS_mlock = Constant('SYS_mlock',(0+150))
SYS_mlockall = Constant('SYS_mlockall',(0+152))
SYS_mmap = Constant('SYS_mmap',(0+ 90))
SYS_mmap2 = Constant('SYS_mmap2',(0+192))
SYS_mount = Constant('SYS_mount',(0+ 21))
SYS_move_pages = Constant('SYS_move_pages',(0+344))
SYS_mprotect = Constant('SYS_mprotect',(0+125))
SYS_mq_getsetattr = Constant('SYS_mq_getsetattr',(0+279))
SYS_mq_notify = Constant('SYS_mq_notify',(0+278))
SYS_mq_open = Constant('SYS_mq_open',(0+274))
SYS_mq_timedreceive = Constant('SYS_mq_timedreceive',(0+277))
SYS_mq_timedsend = Constant('SYS_mq_timedsend',(0+276))
SYS_mq_unlink = Constant('SYS_mq_unlink',(0+275))
SYS_mremap = Constant('SYS_mremap',(0+163))
SYS_msgctl = Constant('SYS_msgctl',(0+304))
SYS_msgget = Constant('SYS_msgget',(0+303))
SYS_msgrcv = Constant('SYS_msgrcv',(0+302))
SYS_msgsnd = Constant('SYS_msgsnd',(0+301))
SYS_msync = Constant('SYS_msync',(0+144))
SYS_munlock = Constant('SYS_munlock',(0+151))
SYS_munlockall = Constant('SYS_munlockall',(0+153))
SYS_munmap = Constant('SYS_munmap',(0+ 91))
SYS_nanosleep = Constant('SYS_nanosleep',(0+162))
SYS__newselect = Constant('SYS__newselect',(0+142))
SYS_nfsservctl = Constant('SYS_nfsservctl',(0+169))
SYS_nice = Constant('SYS_nice',(0+ 34))
SYS_OABI_SYSCALL_BASE = Constant('SYS_OABI_SYSCALL_BASE',0x900000)
SYS_open = Constant('SYS_open',(0+  5))
SYS_openat = Constant('SYS_openat',(0+322))
SYS_pause = Constant('SYS_pause',(0+ 29))
SYS_pciconfig_iobase = Constant('SYS_pciconfig_iobase',(0+271))
SYS_pciconfig_read = Constant('SYS_pciconfig_read',(0+272))
SYS_pciconfig_write = Constant('SYS_pciconfig_write',(0+273))
SYS_personality = Constant('SYS_personality',(0+136))
SYS_pipe = Constant('SYS_pipe',(0+ 42))
SYS_pivot_root = Constant('SYS_pivot_root',(0+218))
SYS_poll = Constant('SYS_poll',(0+168))
SYS_prctl = Constant('SYS_prctl',(0+172))
SYS_pread64 = Constant('SYS_pread64',(0+180))
SYS_ptrace = Constant('SYS_ptrace',(0+ 26))
SYS_pwrite64 = Constant('SYS_pwrite64',(0+181))
SYS_quotactl = Constant('SYS_quotactl',(0+131))
SYS_read = Constant('SYS_read',(0+  3))
SYS_readahead = Constant('SYS_readahead',(0+225))
SYS_readdir = Constant('SYS_readdir',(0+ 89))
SYS_readlink = Constant('SYS_readlink',(0+ 85))
SYS_readlinkat = Constant('SYS_readlinkat',(0+332))
SYS_readv = Constant('SYS_readv',(0+145))
SYS_reboot = Constant('SYS_reboot',(0+ 88))
SYS_recv = Constant('SYS_recv',(0+291))
SYS_recvfrom = Constant('SYS_recvfrom',(0+292))
SYS_recvmsg = Constant('SYS_recvmsg',(0+297))
SYS_remap_file_pages = Constant('SYS_remap_file_pages',(0+253))
SYS_removexattr = Constant('SYS_removexattr',(0+235))
SYS_rename = Constant('SYS_rename',(0+ 38))
SYS_renameat = Constant('SYS_renameat',(0+329))
SYS_request_key = Constant('SYS_request_key',(0+310))
SYS_restart_syscall = Constant('SYS_restart_syscall',(0+  0))
SYS_rmdir = Constant('SYS_rmdir',(0+ 40))
SYS_rt_sigaction = Constant('SYS_rt_sigaction',(0+174))
SYS_rt_sigpending = Constant('SYS_rt_sigpending',(0+176))
SYS_rt_sigprocmask = Constant('SYS_rt_sigprocmask',(0+175))
SYS_rt_sigqueueinfo = Constant('SYS_rt_sigqueueinfo',(0+178))
SYS_rt_sigreturn = Constant('SYS_rt_sigreturn',(0+173))
SYS_rt_sigsuspend = Constant('SYS_rt_sigsuspend',(0+179))
SYS_rt_sigtimedwait = Constant('SYS_rt_sigtimedwait',(0+177))
SYS_sched_getaffinity = Constant('SYS_sched_getaffinity',(0+242))
SYS_sched_getparam = Constant('SYS_sched_getparam',(0+155))
SYS_sched_get_priority_max = Constant('SYS_sched_get_priority_max',(0+159))
SYS_sched_get_priority_min = Constant('SYS_sched_get_priority_min',(0+160))
SYS_sched_getscheduler = Constant('SYS_sched_getscheduler',(0+157))
SYS_sched_rr_get_interval = Constant('SYS_sched_rr_get_interval',(0+161))
SYS_sched_setaffinity = Constant('SYS_sched_setaffinity',(0+241))
SYS_sched_setparam = Constant('SYS_sched_setparam',(0+154))
SYS_sched_setscheduler = Constant('SYS_sched_setscheduler',(0+156))
SYS_sched_yield = Constant('SYS_sched_yield',(0+158))
SYS_select = Constant('SYS_select',(0+ 82))
SYS_semctl = Constant('SYS_semctl',(0+300))
SYS_semget = Constant('SYS_semget',(0+299))
SYS_semop = Constant('SYS_semop',(0+298))
SYS_semtimedop = Constant('SYS_semtimedop',(0+312))
SYS_send = Constant('SYS_send',(0+289))
SYS_sendfile = Constant('SYS_sendfile',(0+187))
SYS_sendfile64 = Constant('SYS_sendfile64',(0+239))
SYS_sendmsg = Constant('SYS_sendmsg',(0+296))
SYS_sendto = Constant('SYS_sendto',(0+290))
SYS_setdomainname = Constant('SYS_setdomainname',(0+121))
SYS_setfsgid = Constant('SYS_setfsgid',(0+139))
SYS_setfsgid32 = Constant('SYS_setfsgid32',(0+216))
SYS_setfsuid = Constant('SYS_setfsuid',(0+138))
SYS_setfsuid32 = Constant('SYS_setfsuid32',(0+215))
SYS_setgid = Constant('SYS_setgid',(0+ 46))
SYS_setgid32 = Constant('SYS_setgid32',(0+214))
SYS_setgroups = Constant('SYS_setgroups',(0+ 81))
SYS_setgroups32 = Constant('SYS_setgroups32',(0+206))
SYS_sethostname = Constant('SYS_sethostname',(0+ 74))
SYS_setitimer = Constant('SYS_setitimer',(0+104))
SYS_set_mempolicy = Constant('SYS_set_mempolicy',(0+321))
SYS_setpgid = Constant('SYS_setpgid',(0+ 57))
SYS_setpriority = Constant('SYS_setpriority',(0+ 97))
SYS_setregid = Constant('SYS_setregid',(0+ 71))
SYS_setregid32 = Constant('SYS_setregid32',(0+204))
SYS_setresgid = Constant('SYS_setresgid',(0+170))
SYS_setresgid32 = Constant('SYS_setresgid32',(0+210))
SYS_setresuid = Constant('SYS_setresuid',(0+164))
SYS_setresuid32 = Constant('SYS_setresuid32',(0+208))
SYS_setreuid = Constant('SYS_setreuid',(0+ 70))
SYS_setreuid32 = Constant('SYS_setreuid32',(0+203))
SYS_setrlimit = Constant('SYS_setrlimit',(0+ 75))
SYS_set_robust_list = Constant('SYS_set_robust_list',(0+338))
SYS_setsid = Constant('SYS_setsid',(0+ 66))
SYS_setsockopt = Constant('SYS_setsockopt',(0+294))
SYS_set_tid_address = Constant('SYS_set_tid_address',(0+256))
SYS_settimeofday = Constant('SYS_settimeofday',(0+ 79))
SYS_setuid = Constant('SYS_setuid',(0+ 23))
SYS_setuid32 = Constant('SYS_setuid32',(0+213))
SYS_setxattr = Constant('SYS_setxattr',(0+226))
SYS_shmat = Constant('SYS_shmat',(0+305))
SYS_shmctl = Constant('SYS_shmctl',(0+308))
SYS_shmdt = Constant('SYS_shmdt',(0+306))
SYS_shmget = Constant('SYS_shmget',(0+307))
SYS_shutdown = Constant('SYS_shutdown',(0+293))
SYS_sigaction = Constant('SYS_sigaction',(0+ 67))
SYS_sigaltstack = Constant('SYS_sigaltstack',(0+186))
SYS_signalfd = Constant('SYS_signalfd',(0+349))
SYS_sigpending = Constant('SYS_sigpending',(0+ 73))
SYS_sigprocmask = Constant('SYS_sigprocmask',(0+126))
SYS_sigreturn = Constant('SYS_sigreturn',(0+119))
SYS_sigsuspend = Constant('SYS_sigsuspend',(0+ 72))
SYS_socket = Constant('SYS_socket',(0+281))
SYS_socketcall = Constant('SYS_socketcall',(0+102))
SYS_socketpair = Constant('SYS_socketpair',(0+288))
SYS_splice = Constant('SYS_splice',(0+340))
SYS_stat = Constant('SYS_stat',(0+106))
SYS_stat64 = Constant('SYS_stat64',(0+195))
SYS_statfs = Constant('SYS_statfs',(0+ 99))
SYS_statfs64 = Constant('SYS_statfs64',(0+266))
SYS_stime = Constant('SYS_stime',(0+ 25))
SYS_swapoff = Constant('SYS_swapoff',(0+115))
SYS_swapon = Constant('SYS_swapon',(0+ 87))
SYS_symlink = Constant('SYS_symlink',(0+ 83))
SYS_symlinkat = Constant('SYS_symlinkat',(0+331))
SYS_sync = Constant('SYS_sync',(0+ 36))
SYS_syscall = Constant('SYS_syscall',(0+113))
SYS_SYSCALL_BASE = Constant('SYS_SYSCALL_BASE',0)
SYS__sysctl = Constant('SYS__sysctl',(0+149))
SYS_sysfs = Constant('SYS_sysfs',(0+135))
SYS_sysinfo = Constant('SYS_sysinfo',(0+116))
SYS_syslog = Constant('SYS_syslog',(0+103))
SYS_tee = Constant('SYS_tee',(0+342))
SYS_tgkill = Constant('SYS_tgkill',(0+268))
SYS_time = Constant('SYS_time',(0+ 13))
SYS_timer_create = Constant('SYS_timer_create',(0+257))
SYS_timer_delete = Constant('SYS_timer_delete',(0+261))
SYS_timerfd = Constant('SYS_timerfd',(0+350))
SYS_timerfd_gettime = Constant('SYS_timerfd_gettime',(0+354))
SYS_timerfd_settime = Constant('SYS_timerfd_settime',(0+353))
SYS_timer_getoverrun = Constant('SYS_timer_getoverrun',(0+260))
SYS_timer_gettime = Constant('SYS_timer_gettime',(0+259))
SYS_timer_settime = Constant('SYS_timer_settime',(0+258))
SYS_times = Constant('SYS_times',(0+ 43))
SYS_tkill = Constant('SYS_tkill',(0+238))
SYS_truncate = Constant('SYS_truncate',(0+ 92))
SYS_truncate64 = Constant('SYS_truncate64',(0+193))
SYS_ugetrlimit = Constant('SYS_ugetrlimit',(0+191))
SYS_umask = Constant('SYS_umask',(0+ 60))
SYS_umount = Constant('SYS_umount',(0+ 22))
SYS_umount2 = Constant('SYS_umount2',(0+ 52))
SYS_uname = Constant('SYS_uname',(0+122))
SYS_unlink = Constant('SYS_unlink',(0+ 10))
SYS_unlinkat = Constant('SYS_unlinkat',(0+328))
SYS_unshare = Constant('SYS_unshare',(0+337))
SYS_uselib = Constant('SYS_uselib',(0+ 86))
SYS_ustat = Constant('SYS_ustat',(0+ 62))
SYS_utime = Constant('SYS_utime',(0+ 30))
SYS_utimensat = Constant('SYS_utimensat',(0+348))
SYS_utimes = Constant('SYS_utimes',(0+269))
SYS_vfork = Constant('SYS_vfork',(0+190))
SYS_vhangup = Constant('SYS_vhangup',(0+111))
SYS_vmsplice = Constant('SYS_vmsplice',(0+343))
SYS_vserver = Constant('SYS_vserver',(0+313))
SYS_wait4 = Constant('SYS_wait4',(0+114))
SYS_waitid = Constant('SYS_waitid',(0+280))
SYS_write = Constant('SYS_write',(0+  4))
SYS_writev = Constant('SYS_writev',(0+146))
