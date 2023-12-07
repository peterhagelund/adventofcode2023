local cards = { "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A" }
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

local function hand_compare(hand1, hand2)
    local type1 = hand_type(hand1)
    local type2 = hand_type(hand2)
    if type1 < type2 then
        return true
    elseif type1 > type2 then
        return false
    else
        for i = 1, 5 do
            local strength1 = strengths[hand1:sub(i, i)]
            local strength2 = strengths[hand2:sub(i, i)]
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
    local hands = {}
    for line in f:lines() do
        local index = line:find(" ")
        local hand = line:sub(1, index - 1)
        local bid = tonumber(line:sub(index + 1, -1))
        hands[hand] = bid
    end
    f:close()
    local sorted_hands = {}
    for hand, _ in pairs(hands) do
        table.insert(sorted_hands, hand)
    end
    table.sort(sorted_hands, hand_compare)
    local total_winnings = 0
    for rank, hand in ipairs(sorted_hands) do
        total_winnings = total_winnings + hands[hand] * rank
    end
    print(string.format("total winnings = %d", total_winnings))
end

main()
