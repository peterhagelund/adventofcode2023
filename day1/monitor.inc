.struct clock
second  .byte
minute  .byte
hour    .byte
day     .byte
month   .byte
year    .byte
weekday .byte
.endstruct

; *****************************************************************************
; * Monitor zero-page RAM locations.
; *****************************************************************************

time_of_day = $0063
dst = $006a
alarm = $006b
flags = $0072
tmp0 = $007b
len0 = $007d
tmp2 = $007e
len2 = $0080
tmp4 = $0081
tmp6 = $0083
errors = $0085

; *****************************************************************************
; * Monitor entry points.
; *****************************************************************************

version = $f000
aci_init = $f003
rd_char = $f006
ck_contc = $f009
getch = $f00c
outch = $f00f
crlf = $f012
spac = $f015
ascbin = $f018
binasc = $f01b
prtstr = $f01e
rdoa = $f021
rdob = $f024
wr_addr = $f027
wrob = $f02a
isum = $f02d
ifasc = $f030
upper_case = $f033
mvdata = $f036
start = $f039
hexin = $f03c
bin2dec = $f03f
ms19out = $f042
ms28in = $f045
chk_sum = $f048
rd_clock = $f04B
wr_clock = $f04e
rtc_mode = $f051
wr_aclock = $f054
extreset = $f057
