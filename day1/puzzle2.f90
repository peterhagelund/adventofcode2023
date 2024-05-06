program puzzle2
    implicit none

    integer :: io, sum = 0
    integer :: index1, index2, len, first_index, first, last_index, last
    character(len=80) :: buffer
    character(len=5), dimension(20) :: digits

    digits = [character(len=5) :: "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", &
              "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

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
        do index1=1,len_trim(buffer)
            do index2=1,20
                len = len_trim(digits(index2))
                if (buffer(index1:index1+len-1) == digits(index2)(1:len)) then
                    if (index1 < first_index) then
                        first_index = index1
                        first = mod(index2-1, 10)
                    end if
                    if (index1 > last_index) then
                        last_index = index1
                        last = mod(index2-1, 10)
                    end if
                end if
            end do
        end do
        sum = sum + first * 10 + last
    end do
    close(1)
    print '("sum = ",i0)', sum
end program puzzle2
