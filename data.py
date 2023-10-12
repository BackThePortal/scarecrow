def get_value():
    if os.path.exists('channel.txt'):
        f = open("channel.txt", "r")
        channel = client.get_channel(int(f.read()))
        f.close()
        return channel
    else:
        return None