I have yet to write a proper README, so here's my prompt into ChatGPT (after already solving a version of the problem - to double check my reasoning):

```
I have a problem that I want to model mathematically and solve:

You have a laundry basket with some (pairs of) socks, but you don't know how many. Let's assume, all pairs are distinct (we don't have 2 pairs of socks, where we could pair any one of the 4 socks with any of the other for example) and we pull (single) socks one at a time from the basket. At each time step we either pull out a new sock and put it aside for later pairing (we denote this by 1) or pull out a sock that matches with some previously pulled out unpaired sock and pair it with it (denote this action by 0). Therefore we can represent this as a binary sequence. At each time step we want to calculate what is the most likely number of pairs of socks in the basket?
```
