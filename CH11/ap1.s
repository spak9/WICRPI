                                @ ap1.s
          .text                 @ start of read-only segment
          .global _start
_start:
          ldr r0,x              @ load r0 from x
          mov r7, #1            @ mov 1 into r7
          svc 0                 @ supervisor call to terminate program

x:        .word 14              @ the variable x

