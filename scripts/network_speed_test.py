from pyspeedtest import SpeedTest


st: SpeedTest = SpeedTest('www.speedtest.net')
print(f"Ping: {st.ping()}, Download: {st.download()}")
