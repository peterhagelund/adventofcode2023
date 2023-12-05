local function main()
    local sum = 0
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local number_digits = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
    local word_digits = { one = 1, two = 2, three = 3, four = 4, five = 5, six = 6, seven = 7, eight = 8, nine = 9 }
    local digits = {}
    for _, v in ipairs(number_digits) do
        table.insert(digits, tostring(v))
    end
    for k, _ in pairs(word_digits) do
        table.insert(digits, k)
    end
    local line_no = 0
    for line in f:lines() do
        line_no = line_no + 1
        local first_index = #line + 1
        local first = nil
        local last_index = -1
        local last = nil
        for _, digit in pairs(digits) do
            local start_index = 0
            local end_index = 0
            while true do
                start_index, end_index = line:find(digit, start_index + 1)
                if not start_index then break end
                if start_index < first_index then
                    first_index = start_index
                    first = line:sub(start_index, end_index)
                end
                if start_index > last_index then
                    last_index = start_index
                    last = line:sub(start_index, end_index)
                end
            end
        end
        print(line_no, first, last)
        local first_digit = word_digits[first]
        if not first_digit then first_digit = tonumber(first) end
        local last_digit = word_digits[last]
        if not last_digit then last_digit = tonumber(last) end
        sum = sum + first_digit * 10 + last_digit
    end
    f:close()
    print("sum = ", sum)
end

main()
