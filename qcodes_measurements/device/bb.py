from qcodes import Instrument, InstrumentChannel, ChannelList


class BB(Instrument):
    def __init__(self, name):
        super().__init__(name)

        channels = ChannelList(self, "channels", BBChan)
        for i in range(25):
            channel = BBChan(self, f"ch{i+1:02}")
            channels.append(channel)
            self.add_submodule(f"ch{i+1:02}", channel)
        channels.lock()
        self.add_submodule("channels", channels)


class BBChan(InstrumentChannel):
    def __init__(self, parent, name, dac_source=None):
        super().__init__(parent, name)
        self.dac_source = dac_source

    def __getattr__(self, name):
        if self.dac_source:
            return getattr(self.dac_source, name)
        raise AttributeError()

    def connect_dac(self, dac_source):
        self.dac_source = dac_source
        return self
