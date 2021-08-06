import speedtest

test = speedtest.Speedtest()

down = test.download()
up = test.upload()

print("Download Speed: {0}".format(down))
print("Upload Speed: {0}".format(up))