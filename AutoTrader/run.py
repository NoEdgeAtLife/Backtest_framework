from autotrader import AutoTrader
from sys import argv

if __name__ == '__main__':
    autotrader = AutoTrader()
    autotrader.configure(verbosity=1,show_plot=True,feed='yahoo',mode='periodic')
    autotrader.add_strategy(argv[1])
    autotrader.backtest(start = '1/1/2021', end = '1/9/2022')
    autotrader.virtual_account_config(initial_balance=1000000, leverage = 100,commission_scheme='percentage',commission=0.0002)
    autotrader.run()