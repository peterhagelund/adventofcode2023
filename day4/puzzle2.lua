local function process_card(sum, index, counts)
    sum = sum + 1
    local count = counts[index]
    for i = 1, count do
        local new_index = index + i
        if new_index <= #counts then
            sum = process_card(sum, new_index, counts)
        end
    end
    return sum
end

local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local counts = {}
    for line in f:lines() do
        local colon = line:find(":")
        local bar = line:find("|")
        local winning_numbers = {}
        for value in line:sub(colon + 1, bar):gmatch("%d+") do
            winning_numbers[tonumber(value)] = true
        end
        local my_numbers = {}
        for value in line:sub(bar + 1, -1):gmatch("%d+") do
            table.insert(my_numbers, tonumber(value))
        end
        local count = 0
        for _, n in ipairs(my_numbers) do
            if winning_numbers[n] then
                count = count + 1
            end
        end
        table.insert(counts, count)
    end
    f:close()
    local sum = 0
    for index = 1, #counts do
        sum = process_card(sum, index, counts)
    end
    print(string.format("sum = %d", sum))
end

main()
