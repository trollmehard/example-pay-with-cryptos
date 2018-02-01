# example-pay-with-cryptos

Calculation of whether it was profitable to convert a portion of its daily expenditure into cryptographic currencies in 2017 and pay for it.

The results will be displayed in the console.

By https://steemit.com/@chkoenig 2018

This is a code example for the following blog post: https://steemit.com/cryptocurrency/@chkoenig/kryptowaehrungen-per-kreditkarte-ausgeben-lohnt-sich-4281eur-jahr-und-geringem-risiko-inkl-rechenbeispiel

## Requirements

* Python 2.7+
* git

## Run the script

```
git clone https://github.com/trollmehard/example-pay-with-cryptos.git
cd example-pay-with-cryptos
python calculate.py
```

## Output

```
## Profit if you don't reinvest the money

That means if you make +20 $ gains, you spend 120 $ this month

> BTC: Profit for month: 1 ---> -2.17 $ / Remaining coins: -0.00221873933811 BTC
> BTC: Profit for month: 2 ---> 7.01 $ / Remaining coins: 0.00591235548415 BTC
> BTC: Profit for month: 3 ---> -7.6 $ / Remaining coins: -0.00711023749472 BTC
> BTC: Profit for month: 4 ---> 7.46 $ / Remaining coins: 0.00571077661266 BTC
> BTC: Profit for month: 5 ---> 35.44 $ / Remaining coins: 0.0149164431873 BTC
> BTC: Profit for month: 6 ---> -1.22 $ / Remaining coins: -0.000494605421613 BTC
> BTC: Profit for month: 7 ---> 1.48 $ / Remaining coins: 0.000547542843313 BTC
> BTC: Profit for month: 8 ---> 33.73 $ / Remaining coins: 0.00701027266463 BTC
> BTC: Profit for month: 9 ---> -8.02 $ / Remaining coins: -0.00186606927694 BTC
> BTC: Profit for month: 10 ---> 22.41 $ / Remaining coins: 0.00338472980697 BTC
> BTC: Profit for month: 11 ---> 25.66 $ / Remaining coins: 0.00240712208948 BTC
> BTC: Profit for month: 12 ---> 9.08 $ / Remaining coins: 0.000677662344936 BTC
------------------------------
> BTC: Profit for month: ALL ---> 123.27 $ / Remaining coins: 0 BTC
------------------------------
> ETH: Profit for month: 1 ---> 12.22 $ / Remaining coins: 1.13295086907 ETH
> ETH: Profit for month: 2 ---> 18.69 $ / Remaining coins: 1.18530803375 ETH
> ETH: Profit for month: 3 ---> 98.21 $ / Remaining coins: 1.974913104 ETH
> ETH: Profit for month: 4 ---> 25.65 $ / Remaining coins: 0.320415903048 ETH
> ETH: Profit for month: 5 ---> 84.18 $ / Remaining coins: 0.368388016058 ETH
> ETH: Profit for month: 6 ---> 8.66 $ / Remaining coins: 0.0303737098769 ETH
> ETH: Profit for month: 7 ---> -13.32 $ / Remaining coins: -0.0598215152054 ETH
> ETH: Profit for month: 8 ---> 32.3 $ / Remaining coins: 0.0828701520396 ETH
> ETH: Profit for month: 9 ---> -13.84 $ / Remaining coins: -0.0461475870784 ETH
> ETH: Profit for month: 10 ---> -3.27 $ / Remaining coins: -0.0109537965819 ETH
> ETH: Profit for month: 11 ---> 24.11 $ / Remaining coins: 0.0512746120848 ETH
> ETH: Profit for month: 12 ---> 26.86 $ / Remaining coins: 0.0349295028849 ETH
------------------------------
> ETH: Profit for month: ALL ---> 300.46 $ / Remaining coins: 0 ETH
------------------------------
> ALL: Profit for month: ALL ---> 423.73 $ / Remaining coins: 0 ALL


## Profit if you reinvest the money

That means if you make +20 $ gains, you only spend 100 $ this month and take the profit to the next month

> BTC: Profit for month: 1 ---> -2.17 $ / Remaining coins: -0.00221873933811 BTC
> BTC: Profit for month: 2 ---> 4.38 $ / Remaining coins: 0.00369361614604 BTC
> BTC: Profit for month: 3 ---> -3.65 $ / Remaining coins: -0.00341662134868 BTC
> BTC: Profit for month: 4 ---> 3.0 $ / Remaining coins: 0.00229415526398 BTC
> BTC: Profit for month: 5 ---> 40.89 $ / Remaining coins: 0.0172105984513 BTC
> BTC: Profit for month: 6 ---> 41.22 $ / Remaining coins: 0.0167159930297 BTC
> BTC: Profit for month: 7 ---> 46.63 $ / Remaining coins: 0.017263535873 BTC
> BTC: Profit for month: 8 ---> 116.81 $ / Remaining coins: 0.0242738085376 BTC
> BTC: Profit for month: 9 ---> 96.31 $ / Remaining coins: 0.0224077392607 BTC
> BTC: Profit for month: 10 ---> 170.8 $ / Remaining coins: 0.0257924690676 BTC
> BTC: Profit for month: 11 ---> 300.61 $ / Remaining coins: 0.0281995911571 BTC
> BTC: Profit for month: 12 ---> 386.96 $ / Remaining coins: 0.028877253502 BTC
------------------------------
> BTC: Profit for month: ALL ---> 386.96 $ / Remaining coins: 0.028877253502 BTC
------------------------------
> ETH: Profit for month: 1 ---> 12.22 $ / Remaining coins: 1.13295086907 ETH
> ETH: Profit for month: 2 ---> 36.56 $ / Remaining coins: 2.31825890283 ETH
> ETH: Profit for month: 3 ---> 213.5 $ / Remaining coins: 4.29317200683 ETH
> ETH: Profit for month: 4 ---> 369.27 $ / Remaining coins: 4.61358790988 ETH
> ETH: Profit for month: 5 ---> 1138.38 $ / Remaining coins: 4.98197592594 ETH
> ETH: Profit for month: 6 ---> 1429.52 $ / Remaining coins: 5.01234963581 ETH
> ETH: Profit for month: 7 ---> 1102.43 $ / Remaining coins: 4.95252812061 ETH
> ETH: Profit for month: 8 ---> 1962.8 $ / Remaining coins: 5.03539827265 ETH
> ETH: Profit for month: 9 ---> 1496.28 $ / Remaining coins: 4.98925068557 ETH
> ETH: Profit for month: 10 ---> 1484.53 $ / Remaining coins: 4.97829688899 ETH
> ETH: Profit for month: 11 ---> 2364.9 $ / Remaining coins: 5.02957150107 ETH
> ETH: Profit for month: 12 ---> 3894.09 $ / Remaining coins: 5.06450100396 ETH
------------------------------
> ETH: Profit for month: ALL ---> 3894.09 $ / Remaining coins: 5.06450100396 ETH
------------------------------
> ALL: Profit for month: ALL ---> 4281.05 $ / Remaining coins: 0 ALL
```

## License

MIT