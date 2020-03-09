	.arch armv5te
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 4
	.eabi_attribute 34, 0
	.eabi_attribute 18, 4
	.file	"chall.c"
	.text
	.align	2
	.global	logtime
	.syntax unified
	.arm
	.fpu softvfp
	.type	logtime, %function
logtime:
	@ args = 0, pretend = 0, frame = 80
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, lr}
	mov	r0, #0
	sub	sp, sp, #84
	bl	time(PLT)
	add	r5, sp, #4
	str	r0, [sp]
	mov	r0, sp
	bl	localtime(PLT)
	add	ip, sp, #36
	mov	lr, r0
	ldmia	lr!, {r0, r1, r2, r3}
	stmia	ip!, {r0, r1, r2, r3}
	ldmia	lr!, {r0, r1, r2, r3}
	stmia	ip!, {r0, r1, r2, r3}
	ldm	lr, {r0, r1, r2}
	stm	ip, {r0, r1, r2}
	ldr	r2, .L4
	add	r3, sp, #36
.LPIC0:
	add	r2, pc, r2
	mov	r1, #32
	mov	r0, r5
	bl	strftime(PLT)
	ldr	r1, .L4+4
	ldr	r0, .L4+8
.LPIC1:
	add	r1, pc, r1
.LPIC2:
	add	r0, pc, r0
	bl	fopen(PLT)
	subs	r4, r0, #0
	bne	.L2
	ldr	r0, .L4+12
.LPIC3:
	add	r0, pc, r0
	bl	puts(PLT)
	mov	r0, r4
	bl	fflush(PLT)
	mov	r0, #1
	bl	exit(PLT)
.L2:
	mov	r1, #0
	mov	r0, r1
	bl	dup2(PLT)
	ldr	r1, .L4+16
	mov	r2, r5
.LPIC4:
	add	r1, pc, r1
	mov	r0, r4
	bl	fprintf(PLT)
	mov	r0, r4
	bl	fclose(PLT)
	mov	r0, #0
	add	sp, sp, #84
	@ sp needed
	pop	{r4, r5, pc}
.L5:
	.align	2
.L4:
	.word	.LC0-(.LPIC0+8)
	.word	.LC1-(.LPIC1+8)
	.word	.LC2-(.LPIC2+8)
	.word	.LC3-(.LPIC3+8)
	.word	.LC4-(.LPIC4+8)
	.size	logtime, .-logtime
	.align	2
	.global	check
	.syntax unified
	.arm
	.fpu softvfp
	.type	check, %function
check:
	@ args = 0, pretend = 0, frame = 56
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, lr}
	sub	sp, sp, #56
	add	r4, sp, #4
	bl	logtime(PLT)
	mov	r1, r4
	mov	r2, #256
	mov	r0, #0
	bl	read(PLT)
	ldr	r1, .L8
	mov	r2, #26
.LPIC5:
	add	r1, pc, r1
	mov	r0, r4
	bl	strncmp(PLT)
	add	sp, sp, #56
	@ sp needed
	pop	{r4, pc}
.L9:
	.align	2
.L8:
	.word	.LC5-(.LPIC5+8)
	.size	check, .-check
	.section	.text.startup,"ax",%progbits
	.align	2
	.global	main
	.syntax unified
	.arm
	.fpu softvfp
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 0, uses_anonymous_args = 0
	push	{r4, r5, r6, lr}
	ldr	r4, .L15
	ldr	r3, .L15+4
.LPIC6:
	add	r4, pc, r4
	ldr	r3, [r4, r3]
	mov	r5, r0
	mov	r6, r1
	ldr	r0, [r3]
	mov	r1, #0
	bl	setbuf(PLT)
	ldr	r3, .L15+8
	mov	r1, #0
	ldr	r3, [r4, r3]
	ldr	r0, [r3]
	bl	setbuf(PLT)
	ldr	r3, .L15+12
	mov	r1, #0
	ldr	r3, [r4, r3]
	ldr	r0, [r3]
	bl	setbuf(PLT)
	ldr	r0, .L15+16
.LPIC7:
	add	r0, pc, r0
	bl	puts(PLT)
	mov	r0, #0
	bl	fflush(PLT)
	mov	r1, r6
	mov	r0, r5
	bl	check(PLT)
	subs	r4, r0, #0
	beq	.L11
	ldr	r0, .L15+20
.LPIC8:
	add	r0, pc, r0
	bl	puts(PLT)
	mov	r0, #0
.L14:
	bl	fflush(PLT)
	mov	r3, #0
	mov     r0, r3
	pop	{r4, r5, r6, pc}
.L11:
	ldr	r0, .L15+24
.LPIC9:
	add	r0, pc, r0
	bl	puts(PLT)
	mov	r0, r4
	b	.L14
.L16:
	.align	2
.L15:
	.word	_GLOBAL_OFFSET_TABLE_-(.LPIC6+8)
	.word	stdin(GOT)
	.word	stdout(GOT)
	.word	stderr(GOT)
	.word	.LC6-(.LPIC7+8)
	.word	.LC7-(.LPIC8+8)
	.word	.LC8-(.LPIC9+8)
	.size	main, .-main
	.section	.rodata.str1.1,"aMS",%progbits,1
.LC0:
	.ascii	"%Y-%m-%d %H:%M:%S\000"
.LC1:
	.ascii	"a+\000"
.LC2:
	.ascii	"/tmp/log.txt\000"
.LC3:
	.ascii	"Error: cannot open /tmp/log.txt!\000"
.LC4:
	.ascii	"%s\012\000"
.LC5:
	.ascii	"ChAnG3_My_D3f4u1t_Pa$$w0rD\000"
.LC6:
	.ascii	"Welcome. Please enter your password:\000"
.LC7:
	.ascii	"Wrong password. Bye.\000"
.LC8:
	.ascii	"Welcome back!\000"
	.ident	"GCC: (Debian 8.3.0-2) 8.3.0"
	.section	.note.GNU-stack,"",%progbits
