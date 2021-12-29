from speedtest import Speedtest # pip install speedtest-cli

st = Speedtest()

print("Your Connection's Download speed is:", st.download())

print("Your Connection's upload speed is:", st.upload())


