local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local times = {}
    local distances = {}
    for line in f:lines() do
        if line:sub(1, 5) == "Time:" then
            for time in line:sub(6, -1):gmatch("%d+") do
                table.insert(times, tonumber(time))
            end
        elseif line:sub(1, 9) == "Distance:" then
            for distance in line:sub(10, -1):gmatch("%d+") do
                table.insert(distances, tonumber(distance))
            end
        end
    end
    f:close()
    local travels = {}
    for i = 1, #times do
        local options = 0
        for hold_time = 0, times[i] - 1 do
            local speed = hold_time
            local distance = (times[i] - hold_time) * speed
            if distance > distances[i] then
                options = options + 1
            end
        end
        table.insert(travels, options)
    end
    local margin_of_error = 1
    for _, travel in ipairs(travels) do
        margin_of_error = margin_of_error * travel
    end
    print(string.format("margin_of_error = %d", margin_of_error))
end

main()
