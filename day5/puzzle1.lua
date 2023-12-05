local function source_to_dest(source, map)
    for _, r in ipairs(map) do
        if source >= r[2] and source < (r[2] + r[3]) then
            return r[1] + (source - r[2])
        end
    end
    return source
end

local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local line_no = 0
    local seeds = {}
    local maps = {}
    local map_index = 0
    for line in f:lines() do
        line_no = line_no + 1
        if #line > 0 then
            if line:sub(1, 7) == "seeds: " then
                for value in line:sub(8, -1):gmatch("%d+") do
                    table.insert(seeds, tonumber(value))
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
    local locations = {}
    for _, seed in ipairs(seeds) do
        local source = seed
        local dest = nil
        for map_index = 1, #maps do
            dest = source_to_dest(source, maps[map_index])
            source = dest
        end
        local location = dest
        table.insert(locations, { seed, location })
    end
    table.sort(locations, function(a, b) return a[2] < b[2] end)
    print(string.format("lowest location is %d for seed %d", locations[1][2], locations[1][1]))
end

main()
