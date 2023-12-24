.pc02
.include "monitor.inc"

.segment "STARTUP"

.proc main
    jsr     crlf
    lda     #>readymsg
    ldx     #<readymsg
    ldy     #6
    jsr     prtstr
    jsr     crlf
    stz     total
    stz     total + 1
read_line:
    ldx     #$00
read_char:
    jsr     getch
    bcc     not_done
    jmp     done
not_done:
    cmp     #$0d
    beq     parse_line
    sta     buffer,x
    inx
    jmp     read_char
parse_line:
    stx     buflen
    stz     first
    stz     last
    ldx     #$00
parse_char:
    lda     buffer,x
    cmp     #'1'
    bcc     char_done
    cmp     #'9'+1
    bcs     char_done
    sec
    sbc     #'0'
    sta     last
    lda     #$00
    cmp     first
    bne     char_done
    lda     last
    sta     first
char_done:
    inx
    cpx     buflen
    bne     parse_char
    jsr     makenum
    clc
    adc     total
    sta     total
    bcc     no_overflow
    inc     total + 1
no_overflow:
    jmp     read_line
done:
    jsr     crlf
    jsr     prttotal
    rts
.endproc

.proc makenum
    clc
    lda     first
    asl
    sta     temp
    asl
    asl
    clc
    adc     temp
    sta     temp
    lda     last
    adc     temp
    rts
.endproc

.proc prttotal
    lda     total + 1
    jsr     binasc
    sta     totalmsg + 8
    stx     totalmsg + 7
    lda     total
    jsr     binasc
    sta     totalmsg + 10
    stx     totalmsg + 9
    lda     #>totalmsg
    ldx     #<totalmsg
    ldy     #11
    jsr     prtstr
.endproc

.segment "DATA"

buffer:
.repeat 128
    .byte $00
.endrepeat
buflen:
    .byte $00
first:
    .byte ' '
last:
    .byte ' '
temp:
    .byte $00
total:
    .word $0000
readymsg:
    .asciiz "READY."
totalmsg:
    .asciiz "TOTAL: XXXX"