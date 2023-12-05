local function dest_to_source(dest, map)
    for _, r in ipairs(map) do
        if dest >= r[1] and dest < r[1] + r[3] then
            return r[2] + (dest - r[1])
        end
    end
    return dest
end

local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local line_no = 0
    local seed_ranges = {}
    local maps = {}
    local map_index = 0
    for line in f:lines() do
        line_no = line_no + 1
        if #line > 0 then
            if line:sub(1, 7) == "seeds: " then
                local values = {}
                for value in line:sub(8, -1):gmatch("%d+") do
                    table.insert(values, tonumber(value))
                end
                for i = 0, (#values / 2) - 1 do
                    table.insert(seed_ranges, { values[2 * i + 1], values[2 * i + 2] })
                end
            elseif line:sub(-5, -1) == " map:" then
                map_index = map_index + 1
                table.insert(maps, {})
            else
                local values = {}
                for value in line:gmatch("%d+") do
                    table.insert(values, tonumber(value))
                end
                table.insert(maps[map_index], values)
            end
        end
    end
    f:close()
    local location = -1
    local found = false
    while not found do
        location = location + 1
        local dest = location
        for map_index = 7, 1, -1 do
            dest = dest_to_source(dest, maps[map_index])
        end
        for _, seed_range in ipairs(seed_ranges) do
            if dest >= seed_range[1] and dest < seed_range[1] + seed_range[2] then
                print(string.format("seed = %d, location = %d", dest, location))
                found = true
                break
            end
        end
    end
end

main()
