local function main()
    local sum = 0
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local line_no = 0
    for line in f:lines() do
        line_no = line_no + 1
        local first = nil
        local last = nil
        for number in line:gmatch("%d") do
            if not first then
                first = tonumber(number)
            else
                last = tonumber(number)
            end
        end
        if not last then
            last = first
        end
        sum = sum + first * 10 + last
    end
    f:close()
    print("sum =", sum)
end

main()
