# economy

earn coins, spend them in the [shop](shop.md), climb the leaderboard. amounts below are approximate ranges, not guarantees.

---

## cooldowns

| command | cooldown |
|---|---|
| `/daily` | 24h |
| `/work` | 1h |
| `/beg` | 5m |
| `/mine` | 30m |
| `/fish` | 20m |
| `/crime` | 2h |
| `/slut` | 6h |
| `/rob` | 30m |

run `/cooldowns` to see what's ready and what isn't.

---

## earning

### safe

these can't lose you coins.

| command | payout |
|---|---|
| `/daily` | 500 coins, once every 24h |
| `/work` | ~30 to 300 |
| `/mine` | ~30 to 300 |
| `/fish` | ~30 to 300 |
| `/beg` | 5m cooldown, payout not documented yet |

`/mine` and `/fish` pay 25% more with the iron pickaxe and fishing rod from the shop.

### risky

bigger payout, but they can go wrong.

| command | win | lose |
|---|---|---|
| `/crime` | ~800 to 2,000 | ~100 to 500 |
| `/slut` | ~800 to 2,000 | ~100 to 500 |

- **`/crime`** can fail in a few ways: you trip, you set off an alarm, you pay a fine.
- **`/slut`** can simply not work out, and you lose coins.
- a lucky clover makes your next `/crime` or `/slut` 20% less likely to fail.

---

## robbing

`/rob` steals coins from another user, usually ~100 to 500.

- base success chance is **40%**.
- a **lockpick** raises your next attempt to **65%**.
- a **padlock** protects the target for 12 hours and blocks the next `/rob` against them.

---

## other commands

| command | what it does |
|---|---|
| `/balance` | check your coins |
| `/give` | give coins to another user |
| `/leaderboard` | the server leaderboard. your position shows as rank on your profile |
| `/cooldowns` | see every cooldown at once |
| `/profile` | see your profile card |

---

## profile

`/profile` renders a card with:

- coins
- rank
- items
- wins, losses and win rate
- your collection of flex items from the shop
- your title, if you have one, in the top right

titles are earned, not bought. see the [readme](../README.md#titles).

---

## notes

- balances aren't guaranteed to survive downtime or data issues. see the [changelog](../changelog.md#known-issues).
