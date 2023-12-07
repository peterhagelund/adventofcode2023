local cards = { "J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A" }
local strengths = {}
for i, v in ipairs(cards) do
    strengths[v] = i
end

local function hand_type(hand)
    local counts = {}
    for i = 1, #hand do
        local card = hand:sub(i, i)
        if counts[card] then
            counts[card] = counts[card] + 1
        else
            counts[card] = 1
        end
    end
    local sorted_counts = {}
    for _, count in pairs(counts) do
        table.insert(sorted_counts, count)
    end
    table.sort(sorted_counts, function(a, b) return a > b end)
    if #sorted_counts == 1 then
        return 7 -- Five of a kind
    elseif #sorted_counts == 2 then
        if sorted_counts[1] == 4 then
            return 6 -- Four of a kind
        else
            return 5 -- Full house
        end
    elseif #sorted_counts == 3 then
        if sorted_counts[1] == 3 then
            return 4 -- Three of a kind
        else
            return 3 -- Two pairs
        end
    else
        if sorted_counts[1] == 2 then
            return 2 -- One pair
        else
            return 1 -- High card
        end
    end
end

local function upgrade_hand(game)
    if game.original_type == 7 then
        return
    end
    if not string.find(game.original_hand, "J") then
        return
    end
    for i = #cards, 2, -1 do
        local upgraded_hand = string.gsub(game.original_hand, "J", cards[i])
        local upgraded_type = hand_type(upgraded_hand)
        if upgraded_type > game.upgraded_type then
            game.upgraded_hand = upgraded_hand
            game.upgraded_type = upgraded_type
        end
    end
end

local function game_compare(game1, game2)
    if game1.upgraded_type < game2.upgraded_type then
        return true
    elseif game1.upgraded_type > game2.upgraded_type then
        return false
    else
        for i = 1, 5 do
            local strength1 = strengths[game1.original_hand:sub(i, i)]
            local strength2 = strengths[game2.original_hand:sub(i, i)]
            if strength1 < strength2 then
                return true
            elseif strength1 > strength2 then
                return false
            end
        end
    end
    return false
end

local function main()
    local f = io.open("puzzle_input.txt", "r")
    if not f then
        os.exit(1)
    end
    local games = {}
    for line in f:lines() do
        local index = line:find(" ")
        local original_hand = line:sub(1, index - 1)
        local bid = tonumber(line:sub(index + 1, -1))
        local original_type = hand_type(original_hand)
        local game = {
            original_hand = original_hand,
            original_type = original_type,
            upgraded_hand = original_hand,
            upgraded_type = original_type,
            bid = bid,
        }
        upgrade_hand(game)
        table.insert(games, game)
    end
    f:close()
    local total_winnings = 0
    table.sort(games, game_compare)
    for rank, game in ipairs(games) do
        total_winnings = total_winnings + game.bid * rank
    end
    print(string.format("total winnings = %d", total_winnings))
end

main()
