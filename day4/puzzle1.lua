local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local sum = 0
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
        local points = 0
        for _, n in ipairs(my_numbers) do
            if winning_numbers[n] then
                if points == 0 then
                    points = 1
                else
                    points = points * 2
                end
            end
        end
        sum = sum + points
    end
    f:close()
    print(string.format("sum = %d", sum))
end

main()
