program puzzle1
    implicit none

    integer :: io, sum = 0
    integer :: index, first_index, first, last_index, last
    character(80) :: buffer

    open(1, file="puzzle_input.txt", status="old", action="read", iostat=io)
    if (io /= 0) then
        print '("error opening file: ",i0)', io
        call exit(io)
    end if
    do while (io == 0)
        read(1, '(a)', iostat=io) buffer
        if (io /= 0) exit
        first_index = 80
        last_index = 0
        do index=1,len_trim(buffer)
            if (buffer(index:index) >= '0' .and. buffer(index:index) <= '9') then
                if (index < first_index) first_index = index
                if (index > last_index) last_index = index
            end if
        end do
        first = ichar(buffer(first_index:first_index)) - ichar('0')
        last = ichar(buffer(last_index:last_index)) - ichar('0')
        sum = sum + first * 10 + last
    end do
    close(1)
    print '("sum = ",i0)', sum
end program puzzle1
