local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local time = nil
    local distance = nil
    for line in f:lines() do
        if line:sub(1, 5) == "Time:" then
            local temp = ""
            for value in line:sub(6, -1):gmatch("%d+") do
                temp = temp .. value
            end
            time = tonumber(temp)
        elseif line:sub(1, 9) == "Distance:" then
            local temp = ""
            for value in line:sub(6, -1):gmatch("%d+") do
                temp = temp .. value
            end
            distance = tonumber(temp)
        end
    end
    f:close()
    local options = 0
    for hold_time = 0, time - 1 do
        local speed = hold_time
        local d = (time - hold_time) * speed
        if d > distance then
            options = options + 1
        end
    end
    print(string.format("options = %d", options))
end

main()
