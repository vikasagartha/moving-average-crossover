## Config options

* syms: [string]
* show_plot: bool
* fast_rate: int (days) 
* slow_rate: int (days)
* tolerance: float

Most of the params are self-explanatory. But tolerance might be slightly confusing.

### Tolerance

Asset prices are discrete values. So when a crossover occurs, the asset values will likely never be exactly equal.

Tolerance represents the fraction of the price which is close enough to call an intersection.

consider a case where sma_fast is above sma_slow:

```
sma_fast = 31
sma_slow = 30
tolerance = 0.01
price: 35

delta = tolerance*price = 0.35
```

`sma_fast > sma_slow`. But this is not marked as an intersection, because `abs(sma_fast-sma_slow) > delta`.

Example config:

```
{
  "syms": [
    "GOOGL",
    "FB",
    "GOGO"
  ],
  "show_plot": true,
  "fast_rate": 20,
  "slow_rate": 50,
  "tolerance": 0.01
}
```

Setup is trival. Clone the repo. Change the `config.json` to suite your needs. Run `python main.py`.
