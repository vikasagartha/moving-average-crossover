## Config options

* syms: [string]
* show_plot: bool
* fast_rate: int (days) 
* slow_rate: int (days)

example:
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
